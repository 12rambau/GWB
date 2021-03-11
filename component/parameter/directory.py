from pathlib import Path

##########################
##     directories      ##
##########################

# this directory is the root directory of all sepal dashboard app.
# please make sure that any result that you produce is embeded inside this folder 
# create a folder adapted to your need inside this folder to save anything in sepal 
module_dir = Path('~','module_results').expanduser()
module_dir.mkdir(exist_ok=True)

# create the general result dir
result_dir = module_dir.joinpath('gwb_results')
result_dir.mkdir(exist_ok = True)

def get_result_dir(process):
    """get the result dir for each process"""
    
    # create the subresult dir 
    dir_ = result_dir.joinpath(process)
    dir_.mkdir(exist_ok = True)
    
    return dir_
    
def get_tmp_dir():
    """get or create the tmp dir corresponding to each process"""
    
    tmp_dir = result_dir.joinpath('tmp')
    tmp_dir.mkdir(exist_ok = True)
    
    return tmp_dir

def get_licence_dir():
    licence_dir = Path('~', '.gwb').expanduser()
    licence_dir.mkdir(exist_ok = True)
    
    return licence_dir

utils_dir = Path(__file__).parent.parent.parent.joinpath('utils')
template_dir = utils_dir.joinpath('template')

#####################
##      files      ##
#####################

eula_txt = utils_dir.joinpath('EULA.txt')
eula_md = utils_dir.joinpath('EULA.md')






