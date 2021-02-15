import json

from .gwb_io import GWBIo
from component  import parameter as cp

class LmIo(GWBIo):
    
    def __init__(self):
        
        # the init file
        self.file = None
        
        # all the bytes values 
        self.lc_1 = []
        self.lc_2 = []
        self.lc_3 = []
        
        # the process 
        self.kdim = None
        
        super().__init__(process = 'lm')
    
    def update_byte_list(self):
        """manually update the byte_list"""
        
        byte_list = [
            self.lc_1,
            self.lc_2,
            self.lc_3
        ]
        
        return super().update_byte_list(byte_list)
    
    def update_params_list(self):
        """manually update the params list"""
        
        params_list = [
                self.kdim
            ]
        
        return super().update_params_list(params_list)
    
    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)"""
        
        self.update_params_list()
        
        params = self.params_list
        
        return super().get_params_list(params)