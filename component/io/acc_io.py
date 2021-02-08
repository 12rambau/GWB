from .gwb_io import GWBIo

class AccIo(GWBIo):
    
    def __init__(self):
        
        # the ini file
        self.file = None
        
        # all the bytes values 
        self.background = []
        self.foreground = []
        self.spe_background_1 = []
        self.spe_background_2 = []
        
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
        