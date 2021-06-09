import json

from traitlets import Any

from .gwb_model import GWBModel
from component  import parameter as cp

class ParcModel(GWBModel):
    
    # the init file
    file = Any(None).tag(sync=True)

    # the process 
    connectivity = Any(cp.connectivity[0]['value']).tag(sync=True)
    res = Any(None).tag(sync=True)
    thresholds = Any("[]").tag(sync=True)
    options = Any(cp.acc_options[0]['value']).tag(sync=True)
    
    def __init__(self):
        
        super().__init__(process = 'parc')
    
    def update_byte_list(self):
        """manually update the byte_list"""
        
        return super().update_byte_list([])
    
    def update_params_list(self):
        """manually update the params list"""
        
        return super().update_params_list([self.connectivity])
    
    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)"""
        
        self.update_params_list()
        
        return super().get_params_list(self.params_list)