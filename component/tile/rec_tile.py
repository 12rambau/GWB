import json
import shutil

from sepal_ui import sepalwidgets as sw 
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw
from component import scripts as cs

class RecTile(sw.Tile):

    def __init__(self, io, convert_tile):
        
        # gather io 
        self.io = io 
        
        # create the widgets
        self.rec_table = cw.RecTable()        
        
        # bind to the io
        self.output = sw.Alert() \
            .bind(self.rec_table.save, self.io, 'recode_json')
        
        # create the btn 
        btn = sw.Btn(cm.process.btn.format(io.process))
        
        super().__init__(
            self.io.tile_id,
            "Run Process",
            inputs = [
                self.rec_table
            ],
            output = self.output,
            btn = btn
        )
        
        # link js behaviours
        btn.on_event('click', self._on_click)
        convert_tile.output.observe(self._on_class_change, 'class')
        
    def _on_class_change(self, change):
        """update the table when a new file is loaded"""
        
        if any(class_ in change['new'] for class_ in ['success', 'warning']):
            self.rec_table.reload_body(self.io.bin_map)
            
        return self
        
    def _on_click(self, widget, event, data):
        
        # silence the btn
        widget.toggle_loading()
        
        # check inputs 
        if not self.output.check_input(self.io.bin_map, cm.bin.no_bin): return widget.toggle_loading()
        
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