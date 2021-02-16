import json
import shutil

from sepal_ui import sepalwidgets as sw 
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw
from component import scripts as cs

from .gwb_tile import GwbTile

class P222Tile(GwbTile):

    def __init__(self, io):
        
        # create the widgets
        algorithm = v.Select(
            label = cm.p222.algo,
            items = cp.algo,
            v_model = cp.algo[0]['value']
        )
        kdim = v.TextField(
            label = cm.lm.kdim,
            type= 'number',
            v_model = None
        )
        prescision = v.Select(
            label = cm.fad.prescision,
            items = cp.prescision,
            v_model = cp.prescision[0]['value']
        )
        
        # bind to the io
        self.output = sw.Alert() \
            .bind(algorithm, io, 'algorithm') \
            .bind(kdim, io, 'kdim') \
            .bind(prescision, io, 'prescision')
        
        super().__init__(
            io = io,
            inputs = [
                algorithm,
                kdim,
                prescision,
            ],
            output = self.output
        )
        
    def _on_click(self, widget, event, data):
        
        # silence the btn
        widget.toggle_loading()
        
        # check inputs 
        if not self.output.check_input(self.io.kdim, cm.lm.no_kdim): return widget.toggle_loading()
        if not self.output.check_input(self.io.bin_map, cm.bin.no_bin): return widget.toggle_loading()
        
        super()._on_click(widget, event, data)
        
        return