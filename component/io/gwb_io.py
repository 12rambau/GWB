# mother class of all the other io. 
# the process will be launched thanks to this object parameters 

class GWBIo():

    def __init__(self, tile_id = 'tile', process = 'gwb', byte_list = []):
    
        # to make sure that each tile of each process have 1 name 
        self.tile_id = tile_id
        self.process = process
    
        # if applicable 
        # the list of the bytes values 
        # the first one will be indexed as 1
        self.byte_list = byte_list
    
    