import shutil

from sepal_ui import sepalwidgets as sw 

from component.message import cm
from component import scripts as cs
from component import parameter as cp

class GwbTile(sw.Tile):

    def __init__(self, io, output, inputs):
        
        # gather io 
        self.io = io         
        
        # create the btn 
        btn = sw.Btn(cm.process.btn.format(io.process))
        
        super().__init__(
            self.io.tile_id,
            "Run Process",
            inputs = inputs,
            output = output,
            btn = btn
        )
        
        # link js behaviours
        btn.on_event('click', self._on_click)
        
    def _on_click(self, widget, event, data):
        
        # the btn will be sience in the tiles
        # widget.toggle_loading()
        
        try:
            
            # update the params list 
            self.io.update_params_list()
        
            # compute acc process 
            files = cs.run_gwb_process(
                process = self.io.process, 
                raster = self.io.bin_map, 
                params_list = self.io.params_list, 
                title = self.io.get_params_list(), 
                output = self.output,
                offset = self.io.offset
            )
            
            # add the files to the download links
            
        except Exception as e:
            self.output.add_live_msg(str(e), 'error')
        
        # remove the tmp directory 
        # whatever the result
        shutil.rmtree(cp.get_tmp_dir())
        
        # release the btn 
        widget.toggle_loading()
        
        return