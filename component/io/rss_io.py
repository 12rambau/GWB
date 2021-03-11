import json

from .gwb_io import GWBIo
from component  import parameter as cp

class RssIo(GWBIo):
    
    def __init__(self):
        
        # the init file
        self.file = None
        
        # all the bytes values 
        self.background = []
        self.foreground = []
        
        # the process 
        self.connectivity = cp.connectivity[0]['value']
        
        super().__init__(process = 'rss')
    
    def update_byte_list(self):
        """manually update the byte_list"""
        
        return super().update_byte_list([
            self.background, 
            self.foreground
        ])
    
    def update_params_list(self):
        """manually update the params list"""
        
        return super().update_params_list([self.connectivity])
    
    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)"""
        
        self.update_params_list()
        
        return super().get_params_list(self.params_list)