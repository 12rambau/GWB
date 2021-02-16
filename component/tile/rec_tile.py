import json
import shutil

from sepal_ui import sepalwidgets as sw 
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw
from component import scripts as cs

from .gwb_tile import GwbTile

class RecTile(GwbTile):

    def __init__(self, io, convert_tile):
        
        # create the widgets
        self.rec_table = cw.RecTable()        
        
        # bind to the io
        self.output = sw.Alert() \
            .bind(self.rec_table.save, io, 'recode_json')
        
        super().__init__(
            io = io,
            inputs = [self.rec_table],
            output = self.output,
        )
        
        # link js behaviours
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
        
        super()._on_click(widget, event, data)
        
        return