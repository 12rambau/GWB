import shutil

from sepal_ui import sepalwidgets as sw

from component.message import cm
from component import scripts as cs
from component import parameter as cp

class GwbTile(sw.Tile):

    def __init__(self, model, inputs):
        
        # gather model 
        self.model = model         
        
        super().__init__(
            self.model.tile_id,
            "Run Process",
            inputs = inputs,
            alert = sw.Alert(),
            btn = sw.Btn(cm.process.btn.format(model.process))
        )
        
        # link js behaviours
        self.btn.on_event('click', self._on_click)
        
    def _on_click(self, widget, event, data):
        
        # update the params list 
        self.model.update_params_list()

        # compute acc process 
        files = cs.run_gwb_process(
            process = self.model.process, 
            raster = self.model.bin_map, 
            params_list = self.model.params_list, 
            title = self.model.get_params_list(), 
            output = self.alert,
            offset = self.model.offset
        )
        
        # remove the tmp directory 
        # whatever the result
        shutil.rmtree(cp.get_tmp_dir())
        
        return