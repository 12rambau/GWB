import json
import shutil

from sepal_ui import sepalwidgets as sw 
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw
from component import scripts as cs

from .gwb_tile import GwbTile

class FadTile(GwbTile):

    def __init__(self, io):
        
        # create the widgets
        connectivity = v.Select(
            label = cm.acc.connectivity,
            items = cp.connectivity,
            v_model = cp.connectivity[0]
        )
        prescision = v.Select(
            label = cm.fad.prescision,
            items = cp.prescision,
            v_model = cp.prescision[0]['value']
        )
        options = v.Select(
            label = cm.acc.options,
            items= cp.fad_options,
            v_model = cp.fad_options[0]['value']
        )
        
        
        # bind to the io
        self.output = sw.Alert() \
            .bind(connectivity, io, 'connectivity') \
            .bind(prescision, io, 'prescision') \
            .bind(options, io, 'options')
        
        super().__init__(
            io = io,
            inputs = [
                connectivity,
                prescision,
                options
            ],
            output = self.output
        )
        
    def _on_click(self, widget, event, data):
        
        # silence the btn
        widget.toggle_loading()
        
        # check inputs 
        if not self.output.check_input(self.io.connectivity, cm.acc.no_connex): return widget.toggle_loading()
        if not self.output.check_input(self.io.prescision, cm.fad.no_prescision): return widget.toggle_loading()
        if not self.output.check_input(self.io.options, cm.acc.no_options): return widget.toggle_loading()
        if not self.output.check_input(self.io.bin_map, cm.bin.no_bin): return widget.toggle_loading()
        
        super()._on_click(widget, event, data)
        
        return