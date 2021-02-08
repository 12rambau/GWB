from sepal_ui import sepalwidgets as sw 
import ipyvuetify as v

from component.message import cm
from component import parameter as cp
from component import widget as cw

class accc_process(sw.Tile):

    def __init__(self, io):
        
        # gather io 
        self.io = io 
        
        # create the widgets
        connectivity = v.Select(
            label = cm.acc.connectivity,
            items = cp.connectivity,
            v_model = cp.connectivity[0]
        )
        res = v.TextField(
            label = cm.acc.res,
            type= 'number',
            v_model = None
        )
        thresholds = cw.Thresholds(label = cm.acc.thresholds)
        options = v.Select(
            label = cm.acc.options,
            items= cp.options,
            v_model = cp.options[0]['value']
        )
        
        
        # bind to the io
        self.output = sw.Alert() \
            .bind(connectivity, self.io, 'connectivity') \
            .bind(res, self.io, 'res') \
            .bind(thresholds.save, self.io, 'thresholds') \
            .bind(options, self.io, 'options')
        
        # create the btn 
        btn = sw.Btn('Start acc process')
        
        super().__init__(
            self.io.tile_id,
            "Run Process",
            inputs = [
                connectivity,
                res,
                thresholds,
                options
            ],
            output = self.output,
            btn = btn
        )