from .gwb_io import GWBIo
from component  import parameter as cp

class AccIo(GWBIo):
    
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
        self.res = None
        self.thresholds = "[]"
        self.option = cp.options[0]['value']
        
        super().__init__(
            tile_id = 'acc_tile',
            process = 'acc',
            byte_list = [
                self.background,
                self.foreground,
                self.spe_background_1,
                self.spe_background_2,
            ]
        )
        
    def update_byte_list(self):
        """manually update the byte_list"""
        
        self.byte_list = [
            self.background,
            self.foreground,
            self.spe_background_1,
            self.spe_background_2,
        ]
        
        return self
        