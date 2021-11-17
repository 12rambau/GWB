from pathlib import Path

##########################
##     directories      ##
##########################

# this directory is the root directory of all sepal dashboard app.
# please make sure that any result that you produce is embeded inside this folder
# create a folder adapted to your need inside this folder to save anything in sepal
module_dir = Path.home() / "module_results"
module_dir.mkdir(exist_ok=True)

# create the general result dir
result_dir = module_dir / "gwb"
result_dir.mkdir(exist_ok=True)

# create a donwloads dir
down_dir = Path.home() / "downloads"
down_dir.mkdir(exist_ok=True)


def get_result_dir(process):
    """get the result dir for each process"""

    # create the subresult dir
    dir_ = result_dir / process
    dir_.mkdir(exist_ok=True)

    return dir_


def get_tmp_dir():
    """get or create the tmp dir corresponding to each process"""

    tmp_dir = result_dir / "tmp"
    tmp_dir.mkdir(exist_ok=True)

    return tmp_dir


def get_licence_dir():
    licence_dir = Path.home() / ".gwb"
    licence_dir.mkdir(exist_ok=True)

    return licence_dir


utils_dir = Path(__file__).parents[2] / "utils"
template_dir = utils_dir / "template"
backup_dir = utils_dir / "backup"

#####################
##      files      ##
#####################

eula_txt = utils_dir / "EULA.txt"
eula_md = utils_dir / "EULA.md"
