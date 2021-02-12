import json

from .gwb_io import GWBIo
from component  import parameter as cp

class FadIo(GWBIo):
    
    def __init__(self):
        
        # the init file
        self.file = None
        
        # all the bytes values 
        self.background = []
        self.foreground = []
        self.spe_background_1 = []
        self.spe_background_2 = []
        
        # the process 
        self.connectivity = cp.connectivity[0]
        self.prescision = None
        self.options = cp.fad_options[0]['value']
        
        super().__init__(process = 'fad')
    
    def update_byte_list(self):
        """manually update the byte_list"""
        
        byte_list = [
            self.background,
            self.foreground,
            self.spe_background_1,
            self.spe_background_2,
        ]
        
        return super().update_byte_list(byte_list)
    
    def update_params_list(self):
        """manually update the params list"""
        
        params_list = [
                self.options,
                self.connectivity,
                self.prescision,
            ]
        
        return super().update_params_list(params_list)
    
    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)"""
        
        self.update_params_list()
        
        params = self.params_list
        
        return super().get_params_list(params)