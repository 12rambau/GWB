import json

from traitlets import Any

from .gwb_model import GWBModel
from component import parameter as cp


class P223Model(GWBModel):

    # the init file
    file = Any(None).tag(sync=True)

    # all the bytes values
    background = Any([]).tag(sync=True)
    foreground = Any([]).tag(sync=True)
    spe_background = Any([]).tag(sync=True)

    # the process
    algorithm = Any(cp.algo[0]["value"]).tag(sync=True)
    kdim = Any(None).tag(sync=True)
    prescision = Any(cp.prescision[0]["value"]).tag(sync=True)

    def __init__(self):

        super().__init__(process="p223")

    def update_byte_list(self):
        """manually update the byte_list"""

        return super().update_byte_list([self.background, self.foreground])

    def update_params_list(self):
        """manually update the params list"""

        return super().update_params_list(
            [
                self.algorithm,
                self.kdim,
                self.prescision,
            ]
        )

    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)"""

        self.update_params_list()

        return super().get_params_list(self.params_list)
