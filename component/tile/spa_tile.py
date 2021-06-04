import json
import shutil

from sepal_ui import sepalwidgets as sw 
from sepal_ui.scripts import utils as su
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw
from component import scripts as cs

from .gwb_tile import GwbTile

class SpaTile(GwbTile):

    def __init__(self, model): 
        
        # create the widgets
        options = v.Select(
            label = cm.spa.nb_classes,
            items = cp.spa_options,
            v_model = None
        )
        
        # bind to the io
        model.bind(options, 'options')
        
        super().__init__(
            model = model,
            inputs = [options]
        )
        
    @su.loading_button()
    def _on_click(self, widget, event, data):
        
        # check inputs 
        if not self.alert.check_input(self.model.options, cm.spa.no_class): return
        if not self.alert.check_input(self.model.bin_map, cm.bin.no_bin): return
        
        super()._on_click(widget, event, data)
        
        return