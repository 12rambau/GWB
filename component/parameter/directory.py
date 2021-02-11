from pathlib import Path

##########################
##     directories      ##
##########################

def get_result_dir(process):
    """get the result dir for each process"""
    
    # create the general result dir
    result_dir = Path('~', 'gwb_results').expanduser()
    result_dir.mkdir(exist_ok = True)
    
    # create the subresult dir 
    result_dir = result_dir.joinpath(process)
    result_dir.mkdir(exist_ok = True)
    
    return result_dir
    
def get_tmp_dir():
    """get or create the tmp dir corresponding to each process"""
    tmp_dir = Path('~', 'gwb_results', 'tmp').expanduser()
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






