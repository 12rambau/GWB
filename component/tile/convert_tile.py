from sepal_ui import sepalwidgets as sw
import ipyvuetify as v
import rasterio as rio

from component.message import cm
from component import scripts as cs
from component import parameter as cp

class ConvertByte(sw.Tile):
    
    def __init__(self, io, nb_class):
        
        # gather the io 
        self.io = io
        
        # create the widgets 
        self.file = sw.FileInput(['.tif', '.tiff'])
        self.classes = [v.Select(
            label = cp.convert[nb_class]['label'][i], 
            items = None, 
            v_model = None, 
            chips = True, 
            multiple = True
        ) for i in range(len(cp.convert[nb_class]['label']))]
        requirements = sw.Markdown(cm.requirement[nb_class])
        
        # bind it to the io 
        self.output = sw.Alert().bind(self.file, self.io, 'file')
        for i in range(len(cp.convert[nb_class]['label'])):
            self.output.bind(self.classes[i], self.io, cp.convert[nb_class]['io'][i])
        
        # create the btn
        btn = sw.Btn(cm.bin.btn)
        
        super().__init__(
            self.io.tile_id,
            cm.bin.title,
            inputs = [requirements, self.file] + self.classes,
            output = self.output,
            btn = btn
        )
        
        # bind js event
        btn.on_event('click', self._on_click)
        self.file.observe(self._on_change, 'v_model')
        
    def _on_click(self, widget, event, data):
            
        # silence the btn 
        widget.toggle_loading()
            
        # check variables
        if not self.output.check_input(self.io.file, cm.bin.no_file): return widget.toggle_loading()
        #if not self.output.check_input(len(self.io.foreground), cm.bin.no_classes): return widget.toggle_loading()
            
        # compute the bin map
        try:
        
            # update byte list 
            self.io.update_byte_list()
        
            # create a bin map 
            bin_map = cs.set_byte_map(
                self.io.byte_list, 
                self.io.file, 
                self.io.process, 
                self.output
            )
            
            self.io.set_bin_map(bin_map)
            
            # add the bin map to the download btn
            
        except Exception as e:
            self.output.add_live_msg(str(e), 'error')
                
            
        # release the btn 
        widget.toggle_loading()
            
        return self
    
    def _on_change(self, change):
        """update the list according to the file selection"""

        # get the nb_class 
        nb_class = len(self.classes)
        
        # empty all select
        for i in range(nb_class):
            self.classes[i].v_model = None
                
        # get all unique values from the image
        features = cs.unique(change['new'])
        
        # add the new list as items 
        for i in range(nb_class):
            self.classes[i].items = features
        
        return self