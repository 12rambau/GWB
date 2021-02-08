from pathlib import Path

# add all the directory that will be used in the app.
def get_result_dir(process):
    """get the result dir for each process"""
    
    # create the general result dir
    result_dir = Path('~', 'gwb_results').expanduser()
    result_dir.mkdir(exist_ok = True)
    
    # create the subresult dir 
    result_dir = result_dir.joinpath(process)
    result_dir.mkdir(exist_ok = True)
    
    return result_dir
    
def get_tmp_dir(process):
    """get or create the tmp dir corresponding to each process"""
    tmp_dir = get_result_dir(process).joinpath('tmp')
    tmp_dir.mkdir(exist_ok = True)
    
    return tmp_dir



