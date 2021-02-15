import json

from .gwb_io import GWBIo
from component  import parameter as cp

class RecIo(GWBIo):
    
    def __init__(self):
        
        # the init file
        self.file = None
        
        # the process 
        self.recode_json = json.dumps({i: i for i in range(256)})
        self.res = None
        self.thresholds = "[]"
        self.options = cp.acc_options[0]['value']
        
        super().__init__(process = 'rec')
    
    def update_byte_list(self):
        """manually update the byte_list"""
        
        byte_list = []
        
        return super().update_byte_list(byte_list)
    
    def update_params_list(self):
        """manually update the params list"""
        
        # uncode the recode.json string
        recode = json.loads(self.recode_json)
        
        # create the param list
        params_list = [f'{recode[str(i)]} {i}' for i in range (256)]
        
        return super().update_params_list(params_list)
    
    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)"""
        
        self.update_params_list()
        
        params = []
        
        return super().get_params_list(params)