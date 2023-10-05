import ipyvuetify as v
from sepal_ui.scripts import utils as su

from component import parameter as cp
from component.message import cm

from .gwb_tile import GwbTile


class DistTile(GwbTile):
    def __init__(self, model):

        # create the widgets
        connectivity = v.Select(
            label=cm.acc.connectivity,
            items=cp.connectivity,
            v_model=cp.connectivity[0]["value"],
        )
        options = v.Select(
            label=cm.acc.options,
            items=cp.dist_options,
            v_model=cp.dist_options[0]["value"],
        )

        # bind to the io
        (model.bind(connectivity, "connectivity").bind(options, "options"))

        super().__init__(model=model, inputs=[connectivity, options])

    @su.loading_button()
    def _on_click(self, widget, event, data):

        # check inputs
        if not all(
            [
                self.alert.check_input(self.model.connectivity, cm.acc.no_connex),
                self.alert.check_input(self.model.options, cm.acc.no_options),
                self.alert.check_input(self.model.bin_map, cm.bin.no_bin),
            ]
        ):
            return

        super()._on_click(widget, event, data)

        return
