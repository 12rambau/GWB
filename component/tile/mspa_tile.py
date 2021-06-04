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

class MspaTile(GwbTile):

    def __init__(self, model): 
        
        # create the widgets
        connectivity = v.Select(
            label = cm.acc.connectivity,
            items = cp.connectivity,
            v_model = cp.connectivity[0]['value']
        )
        edge_width = v.Slider(
            label = cm.mspa.edge_width,
            min = 1,
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
        model \
            .bind(connectivity, 'connectivity') \
            .bind(edge_width, 'edge_width') \
            .bind(transition, 'transition') \
            .bind(int_ext, 'int_ext')
        
        super().__init__(
            model = model,
            inputs = [
                connectivity,
                edge_width,
                transition,
                int_ext
            ]
        )
        
    @su.loading_button()
    def _on_click(self, widget, event, data):
        
        # check inputs 
        if not self.alert.check_input(self.model.connectivity, cm.acc.no_connex): return
        if not self.alert.check_input(self.model.edge_width, cm.mspa.no_edge_width): return
        if not self.alert.check_input(self.model.bin_map, cm.bin.no_bin): return
        
        super()._on_click(widget, event, data)
        
        return