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


class FragTile(GwbTile):
    def __init__(self, model):

        # create the widgets
        connectivity = v.Select(
            label=cm.acc.connectivity,
            items=cp.connectivity,
            v_model=cp.connectivity[0]["value"],
        )
        res = v.TextField(
            label=cm.acc.res, type="number", v_model=None, hint=cm.acc.res_hint
        )
        windows = cw.Windows(label=cm.frag.windows)
        options = v.Select(
            label=cm.acc.options,
            items=cp.frag_options,
            v_model=cp.frag_options[0]["value"],
        )

        prescision = v.Select(
            label=cm.fad.prescision,
            items=cp.prescision,
            v_model=cp.prescision[0]["value"],
        )

        # bind to the io
        (
            model.bind(connectivity, "connectivity")
            .bind(res, "res")
            .bind(windows.save, "window_size")
            .bind(options, "options")
            .bind(prescision, "prescision")
        )

        # extra js behaviour
        res.on_event("focusout", self._on_focus_out)

        super().__init__(
            model=model, inputs=[connectivity, res, windows, options, prescision]
        )

    @su.loading_button()
    def _on_click(self, widget, event, data):

        # check inputs
        if not all(
            [
                self.alert.check_input(self.model.connectivity, cm.acc.no_connex),
                self.alert.check_input(self.model.res, cm.acc.no_res),
                self.alert.check_input(
                    json.loads(self.model.window_size), cm.frag.no_windows
                ),
                self.alert.check_input(self.model.options, cm.acc.no_options),
                self.alert.check_input(self.model.prescision, cm.fad.no_prescision),
                self.alert.check_input(self.model.bin_map, cm.bin.no_bin),
            ]
        ):
            return

        super()._on_click(widget, event, data)

        return

    def _on_focus_out(self, widget, event, data):

        # clear error
        widget.error_messages = None

        # get out if v_model is none
        if not widget.v_model:
            return self

        valid = True
        try:

            value = int(widget.v_model)

            if value < 0:
                valid = False

        except ValueError:
            valid = False

        if not valid:
            widget.v_model = None
            widget.error_messages = [cm.acc.res_hint]

        return self
