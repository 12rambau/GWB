import json

from traitlets import Any

from .gwb_model import GWBModel
from component  import parameter as cp

class AccModel(GWBModel):
    
    # the init file
    file = Any(None).tag(sync=True)

    # all the bytes values 
    background = Any([]).tag(sync=True)
    foreground = Any([]).tag(sync=True)
    spe_background_1 = Any([]).tag(sync=True)
    spe_background_2 = Any([]).tag(sync=True)

    # the process 
    connectivity = Any(cp.connectivity[0]['value']).tag(sync=True)
    res = Any(None).tag(sync=True)
    thresholds = Any("[]").tag(sync=True)
    options = Any(cp.acc_options[0]['value']).tag(sync=True)
    big_3_pink = Any(True).tag(sync=True)
    
    def __init__(self):
        
        super().__init__(process = 'acc')
    
    def update_byte_list(self):
        """manually update the byte_list"""
        
        return super().update_byte_list([
            self.background,
            self.foreground,
            self.spe_background_1,
            self.spe_background_2,
        ])
    
    def update_params_list(self):
        """manually update the params list""" 
        
        return super().update_params_list([
                self.connectivity,
                self.res,
                self.join_attr('thresholds'),
                self.options,
                int(self.big_3_pink)
            ])
    
    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)"""
        
        self.update_params_list()
        
        params = self.params_list
        params[2] = self.join_attr('thresholds', '_')
        
        return super().get_params_list(params)