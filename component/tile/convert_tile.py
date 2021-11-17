from sepal_ui import sepalwidgets as sw
from sepal_ui.scripts import utils as su
import ipyvuetify as v
import rasterio as rio

from component.message import cm
from component import scripts as cs
from component import parameter as cp


class ConvertByte(sw.Tile):
    def __init__(self, model, nb_class):

        # gather the model
        self.model = model

        # create the download layout
        mkd_txt = sw.Markdown(cm.bin.default.tooltip)
        self.down_test = sw.Btn(
            cm.bin.default.btn,
            icon="mdi-cloud-download-outline",
            small=True,
            outlined=True,
            class_="mb-5",
        )

        # create the widgets

        self.file = sw.FileInput([".tif", ".tiff"])
        self.classes = [
            v.Select(
                label=cp.convert[nb_class]["label"][i],
                items=None,
                v_model=[],
                chips=True,
                small_chips=True,
                multiple=True,
                dense=True,
                deletable_chips=True,
            )
            for i in range(len(cp.convert[nb_class]["label"]))
        ]
        requirements = sw.Markdown(cm.requirement[nb_class])

        # bind it to the model
        self.model.bind(self.file, "file")
        for i in range(len(cp.convert[nb_class]["label"])):
            self.model.bind(self.classes[i], cp.convert[nb_class]["io"][i])

        super().__init__(
            self.model.tile_id,
            cm.bin.title,
            inputs=[mkd_txt, self.down_test, v.Divider(), requirements, self.file]
            + self.classes,
            alert=sw.Alert(),
            btn=sw.Btn(cm.bin.btn),
        )

        # bind js event
        self.btn.on_event("click", self._on_click)
        self.file.observe(self._on_change, "v_model")
        self.down_test.on_event("click", self._on_download)

    @su.loading_button(debug=True)
    def _on_click(self, widget, event, data):

        # check variables
        if not self.alert.check_input(self.model.file, cm.bin.no_file):
            return

        # update byte list
        self.model.update_byte_list()

        # create a bin map
        bin_map = cs.set_byte_map(
            self.model.byte_list, self.model.file, self.model.process, self.alert
        )

        self.model.set_bin_map(bin_map)

        return self

    def _on_change(self, change):
        """update the list according to the file selection"""

        # get the nb_class
        nb_class = len(self.classes)

        # empty all select
        for i in range(nb_class):
            self.classes[i].v_model = []

        # get all unique values from the image
        features = cs.unique(change["new"])

        # add the new list as items
        for i in range(nb_class):
            self.classes[i].items = features

        return self

    @su.loading_button()
    def _on_download(self, widget, event, data):

        cs.download_test(self.alert)

        return self
