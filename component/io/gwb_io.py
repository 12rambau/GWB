import json 

class GWBIo():
    """
    Mother class of all the other io. 
    The process will be launched thanks to this object parameters 
    """

    def __init__(self, tile_id = 'tile', process = 'gwb', byte_list = [], params_list=[], bin_map=None):
    
        # to make sure that each tile of each process have 1 name 
        self.tile_id = tile_id
        self.process = process
    
        # if applicable 
        # the list of the bytes values 
        # the first one will be indexed as 1
        self.byte_list = byte_list
        
        # the list of the parameter 
        # each sublist will be considered as a line
        self.params_list = params_list
        
        self.bin_map = bin_map
        
    def join_attr(self, attr, sep=' '):
        """
        join the values of a list using the separator
        lot of them are stored as int and cannot be joined easily
        
        Args: 
            attr (list): list of attr that need to be on 1 line in the parameter file
            sep (str): the strin to use as separator 
            
        return:
            (str): the joined str 
        """
        
        # will raise an error if the attribute doesn't exist
        params_list = getattr(self, attr)
        
        # transform into str list 
        params_list = json.loads(params_list)
        params_list = [str(p) for p in params_list]
        
        return sep.join(params_list)
    
    def set_bin_map(self, path):
        
        self.bin_map = path
        
        return self
    
    def update_byte_list(self, list_):
        
        self.byte_list = list_
        
        return self
    
    def update_params_list(self, list_):
        
        self.params_list = list_
        
        return self
    
    def get_params_list(self, list_=None):
        
        list_ = list_ or self.params_list
        list_ = [str(e) for e in list_]
        
        return '_'.join(list_)
        
    
    