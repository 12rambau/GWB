import json

from traitlets import Any

from .gwb_model import GWBModel
from component import parameter as cp


class LmModel(GWBModel):

    # the init file
    file = Any(None).tag(sync=True)

    # all the bytes values
    lc_1 = Any([]).tag(sync=True)
    lc_2 = Any([]).tag(sync=True)
    lc_3 = Any([]).tag(sync=True)

    # the process
    kdim = Any(None).tag(sync=True)

    def __init__(self):

        super().__init__(process="lm")

    def update_byte_list(self):
        """manually update the byte_list"""

        return super().update_byte_list([self.lc_1, self.lc_2, self.lc_3])

    def update_params_list(self):
        """manually update the params list"""

        return super().update_params_list([self.kdim])

    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)"""

        self.update_params_list()

        return super().get_params_list(self.params_list)
