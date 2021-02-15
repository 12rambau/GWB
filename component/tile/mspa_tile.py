import json
import shutil

from sepal_ui import sepalwidgets as sw 
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw
from component import scripts as cs

class MspaTile(sw.Tile):

    def __init__(self, io):
        
        # gather io 
        self.io = io 
        
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
            .bind(connectivity, self.io, 'connectivity') \
            .bind(edge_width, self.io, 'edge_width') \
            .bind(transition, self.io, 'transition') \
            .bind(int_ext, self.io, 'int_ext')
        
        # create the btn 
        btn = sw.Btn(cm.process.btn.format(io.process))
        
        super().__init__(
            self.io.tile_id,
            "Run Process",
            inputs = [
                connectivity,
                edge_width,
                transition,
                int_ext
            ],
            output = self.output,
            btn = btn
        )
        
        # link js behaviours
        btn.on_event('click', self._on_click)
        
    def _on_click(self, widget, event, data):
        
        # silence the btn
        widget.toggle_loading()
        
        # check inputs 
        if not self.output.check_input(self.io.connectivity, cm.acc.no_connex): return widget.toggle_loading()
        if not self.output.check_input(self.io.edge_width, cm.mspa.no_edge_width): return widget.toggle_loading()
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