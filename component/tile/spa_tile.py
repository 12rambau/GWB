import json
import shutil

from sepal_ui import sepalwidgets as sw 
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw
from component import scripts as cs

from .gwb_tile import GwbTile

class SpaTile(GwbTile):

    def __init__(self, io): 
        
        # create the widgets
        options = v.Select(
            label = cm.spa.nb_classes,
            items = cp.spa_options,
            v_model = None
        )
        
        # bind to the io
        self.output = sw.Alert() \
            .bind(options, io, 'options')
        
        super().__init__(
            io = io,
            inputs = [options],
            output = self.output,
        )
        
    def _on_click(self, widget, event, data):
        
        # silence the btn
        widget.toggle_loading()
        
        # check inputs 
        if not self.output.check_input(self.io.options, cm.spa.no_class): return widget.toggle_loading()
        if not self.output.check_input(self.io.bin_map, cm.bin.no_bin): return widget.toggle_loading()
        
        super()._on_click(widget, event, data)
        
        return