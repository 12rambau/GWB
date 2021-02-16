import json
import shutil

from sepal_ui import sepalwidgets as sw 
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw
from component import scripts as cs

from .gwb_tile import GwbTile

class MspaTile(GwbTile):

    def __init__(self, io): 
        
        # create the widgets
        connectivity = v.Select(
            label = cm.acc.connectivity,
            items = cp.connectivity,
            v_model = cp.connectivity[0]
        )
        edge_width = v.Slider(
            label = cm.mspa.edge_width,
            max = 30,
            v_model = 1
        )
        transition = v.Switch(
            label = cm.mspa.transition,
            false_value = 0,
            true_value = 1,
            v_model = 1
        )
        int_ext = v.Switch(
            label = cm.mspa.int_ext,
            false_value = 0, 
            true_value = 1,
            v_model = 1
        )
        
        
        # bind to the io
        self.output = sw.Alert() \
            .bind(connectivity, io, 'connectivity') \
            .bind(edge_width, io, 'edge_width') \
            .bind(transition, io, 'transition') \
            .bind(int_ext, io, 'int_ext')
        
        super().__init__(
            io = io,
            inputs = [
                connectivity,
                edge_width,
                transition,
                int_ext
            ],
            output = self.output
        )
        
    def _on_click(self, widget, event, data):
        
        # silence the btn
        widget.toggle_loading()
        
        # check inputs 
        if not self.output.check_input(self.io.connectivity, cm.acc.no_connex): return widget.toggle_loading()
        if not self.output.check_input(self.io.edge_width, cm.mspa.no_edge_width): return widget.toggle_loading()
        if not self.output.check_input(self.io.bin_map, cm.bin.no_bin): return widget.toggle_loading()
        
        super()._on_click(widget, event, data)
        
        return