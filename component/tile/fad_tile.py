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


class FadTile(GwbTile):
    def __init__(self, model):

        # create the widgets
        connectivity = v.Select(
            label=cm.acc.connectivity,
            items=cp.connectivity,
            v_model=cp.connectivity[0]["value"],
        )
        prescision = v.Select(
            label=cm.fad.prescision,
            items=cp.prescision,
            v_model=cp.prescision[0]["value"],
        )
        options = v.Select(
            label=cm.acc.options,
            items=cp.fad_options,
            v_model=cp.fad_options[0]["value"],
        )

        # bind to the io
        (
            model.bind(connectivity, "connectivity")
            .bind(prescision, "prescision")
            .bind(options, "options")
        )

        super().__init__(
            model=model,
            inputs=[connectivity, prescision, options],
        )

    @su.loading_button()
    def _on_click(self, widget, event, data):

        # check inputs
        if not all(
            [
                self.alert.check_input(self.model.connectivity, cm.acc.no_connex),
                self.alert.check_input(self.model.prescision, cm.fad.no_prescision),
                self.alert.check_input(self.model.options, cm.acc.no_options),
                self.alert.check_input(self.model.bin_map, cm.bin.no_bin),
            ]
        ):
            return

        super()._on_click(widget, event, data)

        return
