import json

from traitlets import Any

from .gwb_model import GWBModel
from component  import parameter as cp

class RecIo(GWBModel):
    
    # the init file
    file = Any(None).tag(sync=True)

    # the process 
    recode_json = Any(json.dumps({i: i for i in range(256)})).tag(sync=True)
    res = Any(None).tag(sync=True)
    thresholds = Any("[]").tag(sync=True)
    options = Any(cp.acc_options[0]['value']).tag(sync=True)
    
    def __init__(self):
        
        super().__init__(process = 'rec')
    
    def update_byte_list(self):
        """manually update the byte_list"""
        
        return super().update_byte_list([])
    
    def update_params_list(self):
        """manually update the params list"""
        
        # uncode the recode.json string
        recode = json.loads(self.recode_json)
        
        return super().update_params_list([f'{recode[str(i)]} {i}' for i in range (256)])
    
    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)"""
        
        self.update_params_list()
        
        return super().get_params_list([])