from pathlib import Path
from itertools import combinations

import rasterio as rio
import numpy as np

from component import parameter as cp
from component.message import cm


def is_overlap(class_list):
    """check if the lists overlaps"""

    overlap = False

    for a, b in combinations(class_list, 2):

        # don't test empty lists
        if a == [] or b == []:
            continue

        # if the two lists intersects, I stop
        if bool(set(a) & set(b)):
            overlap = True
            break

    return overlap


def set_byte_map(class_list, raster, process, output):
    """
    reclassify a map using the provided class list

    Args:
        class_list (list(list(int))): each list of the root list represent a byte value starting at 1.
            each nested list is the value of the class that need to be included into each byte value.
        raster (pathlib.Path): the path to the original image
    """
    # check that the inputs are all separated
    if is_overlap(class_list):
        raise Exception(cm.bin.overlap)

    # output for the user
    output.add_live_msg(cm.bin.running)

    # get the final file name
    filename = Path(raster).stem
    bin_map = cp.get_result_dir(process) / f"{filename}_bin_map.tif"

    if bin_map.is_file():
        output.add_live_msg(cm.bin.file_exist.format(bin_map), "warning")
        return bin_map

    # create the bin map using the values provided by the end user
    with rio.open(raster) as src:

        out_meta = src.meta.copy()
        out_meta.update(compress="lzw", dtype=np.uint8)
        raw_data = src.read()

        if class_list == []:
            data = raw_data
        else:
            data = np.zeros_like(raw_data, dtype=np.uint8)
            total_class = sum([len(c) for c in class_list])
            c = 0
            output.update_progress(0)
            for index, class_ in enumerate(class_list):

                bool_data = np.zeros_like(raw_data, dtype=np.bool_)
                for val in class_:
                    bool_data = bool_data + (raw_data == val)

                    # display the advancement
                    c += 1
                    output.update_progress(c / total_class)

                data_value = (bool_data * (index + 1)).astype(np.uint8)
                data = data + data_value

            data = data.astype(out_meta["dtype"])

        with rio.open(bin_map, "w", **out_meta) as dst:
            dst.write(data)

    output.add_live_msg(cm.bin.finished, "success")

    return bin_map


def unique(raster):
    """Retreive all the existing feature in the byte file"""

    features = []

    if raster:
        raster = Path(raster)
    else:
        raise Exception("no raster given")

    with rio.open(raster) as src:

        data = src.read(1)
        count = np.bincount(data.flatten())
        del data

        features = np.where(count != 0)[0]
        features = features.tolist()

    return features


def reclassify_from_map(in_raster, map_values, dst_raster=None, overwrite=False):
    """Remap raster values from map_values dictionary. If the
    are missing values in the dictionary 0 value will be returned

    Args:
        in_raster (path to raster): Input raster to reclassify
        map_values (dict): Dictionary with origin:target values
    """

    # Get reclassify path raster
    filename = Path(in_raster).stem
    dst_raster = dst_raster or Path.home() / f"downloads/{filename}_reclassified.tif"

    if not overwrite:
        if dst_raster.is_file():
            raise Warning(cm.bin.reclassify_exist.format(dst_raster))
        else:
            raise Exception(cm.bin.no_exists.format(dst_raster))

    if not all(list(map_values.values())):
        raise Exception("All new values has to be filled, try it again.")

    # Cast to integer map_values

    map_values = {k: int(v) for k, v in map_values.items()}

    with rio.open(in_raster) as src:

        raw_data = src.read()
        profile = src.profile
        profile.update(compress="lzw", dtype=np.uint8)

        data = np.zeros_like(raw_data, dtype=np.uint8)

        for origin, target in map_values.items():

            bool_data = np.zeros_like(raw_data, dtype=np.bool_)
            bool_data = bool_data + (raw_data == origin)

            data_value = (bool_data * target).astype(np.uint8)

            data += data_value

            with rio.open(dst_raster, "w", **profile) as dst:
                dst.write(data)

    return data
