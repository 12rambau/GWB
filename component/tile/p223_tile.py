import json
import shutil

from sepal_ui import sepalwidgets as sw 
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw
from component import scripts as cs

from .gwb_tile import GwbTile

class P223Tile(GwbTile):

    def __init__(self, io):
        
        # create the widgets
        algorithm = v.Select(
            label = cm.p223.algo,
            items = cp.algo,
            v_model = cp.algo[0]['value']
        )
        kdim = v.TextField(
            label = cm.lm.kdim,
            type= 'number',
            hint=cm.frag.invalid_window,
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
        
        # create extra js behaviour 
        kdim.on_event('focusout', self._on_focusout)
        
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
    
    def _on_focusout(self, widget, event, data):
        
        # clear the error message 
        widget.error_messages = None
        
        # check if an input exist 
        if not widget.v_model:
            return self
        
        # test the value over the limits 
        if not cs.is_valid_window(widget.v_model): 
            widget.v_model = False
            widget.error_messages = [cm.frag.invalid_window]
            
        return self