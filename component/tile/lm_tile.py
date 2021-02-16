import json
import shutil

from sepal_ui import sepalwidgets as sw 
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw
from component import scripts as cs

from .gwb_tile import GwbTile

class LmTile(GwbTile):

    def __init__(self, io): 
        
        # create the widgets
        kdim = v.TextField(
            label = cm.lm.kdim,
            type= 'number',
            v_model = None
        )
        
        
        # bind to the io
        self.output = sw.Alert() \
            .bind(kdim, io, 'kdim')
        
        super().__init__(
            io = io,
            inputs = [kdim],
            output = self.output
        )
        
    def _on_click(self, widget, event, data):
        
        # silence the btn
        widget.toggle_loading()
        
        # check inputs 
        if not self.output.check_input(self.io.kdim, cm.lm.no_kdim): return widget.toggle_loading()
        
        super()._on_click(widget, event, data)
        
        return