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


class LmTile(GwbTile):
    def __init__(self, model):

        # create the widgets
        kdim = v.TextField(
            class_="mb-2",
            label=cm.lm.kdim,
            type="number",
            v_model=None,
            hint=cm.frag.invalid_window,
        )

        # bind to the io
        model.bind(kdim, "kdim")

        # extra js behaviour
        kdim.on_event("focusout", self._on_focusout)

        super().__init__(model=model, inputs=[kdim])

    @su.loading_button()
    def _on_click(self, widget, event, data):

        # check inputs
        if not self.alert.check_input(self.model.kdim, cm.lm.no_kdim):
            return

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
