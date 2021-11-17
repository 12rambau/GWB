import json

import ipyvuetify as v

from component.message import cm
from component import scripts as cs


class Windows(v.Layout):
    def __init__(self, label="Thresholds"):

        # hidden textfield to save the v_model
        # the v_model will be stored as json
        self.save = v.TextField(v_model=None)

        # create the inputs
        self.text_fields = [
            v.TextField(
                placeholder=cm.frag.window_lbl.format(i + 1),
                v_model=None,
                type="number",
                class_="ml-1 mr-1",
                hint=cm.frag.invalid_window,
            )
            for i in range(10)
        ]

        # title
        title = v.Html(tag="h4", children=[label])

        # add js behaviour
        for w in self.text_fields:
            w.observe(self._on_change, "v_model")
            w.on_event("focusout", self._on_focusout)

        super().__init__(
            class_="ma-5",
            row=True,
            children=[title, v.Layout(row=True, children=self.text_fields)],
        )

    def _on_change(self, change):

        # get the values of al widgets
        values = [w.v_model for w in self.text_fields]

        # remove none values
        values = [int(v) for v in values if v]

        # sort them
        values.sort()

        # add them as json in the save field
        self.save.v_model = json.dumps(values)

        return self

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
