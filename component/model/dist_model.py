import json

from traitlets import Any

from .gwb_model import GWBModel
from component import parameter as cp


class DistModel(GWBModel):

    # the init file
    file = Any(None).tag(sync=True)

    # all the bytes values
    background = Any([]).tag(sync=True)
    foreground = Any([]).tag(sync=True)

    # the process
    connectivity = Any(cp.connectivity[0]["value"]).tag(sync=True)
    options = Any(cp.dist_options[0]["value"]).tag(sync=True)

    def __init__(self):

        super().__init__(process="dist")

    def update_byte_list(self):
        """manually update the byte_list"""

        return super().update_byte_list([self.background, self.foreground])

    def update_params_list(self):
        """manually update the params list"""

        return super().update_params_list([self.connectivity, self.options])

    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)"""

        self.update_params_list()

        return super().get_params_list(self.params_list)
