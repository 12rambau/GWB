from traitlets import Any

from component import parameter as cp

from .gwb_model import GWBModel


class FragModel(GWBModel):
    # the init file
    file = Any(None).tag(sync=True)

    # all the bytes values
    background = Any([]).tag(sync=True)
    foreground = Any([]).tag(sync=True)
    spe_background_1 = Any([]).tag(sync=True)
    spe_background_2 = Any([]).tag(sync=True)
    statistics = Any(0).tag(sync=True)

    # the process
    connectivity = Any(cp.connectivity[0]["value"]).tag(sync=True)
    res = Any(None).tag(sync=True)
    window_size = Any("[]").tag(sync=True)
    prescision = Any(cp.prescision[0]["value"]).tag(sync=True)
    options = Any(cp.frag_options[0]["value"]).tag(sync=True)

    def __init__(self):
        super().__init__(process="frag")

    def update_byte_list(self):
        """manually update the byte_list."""
        return super().update_byte_list(
            [
                self.background,
                self.foreground,
                self.spe_background_1,
                self.spe_background_2,
            ]
        )

    def update_params_list(self):
        """manually update the params list."""
        return super().update_params_list(
            [
                self.options,
                self.connectivity,
                self.res,
                self.join_attr("window_size"),
                self.prescision,
                self.statistics,
            ]
        )

    def get_params_list(self):
        """get the params list for naming purposes (_ and no spaces)."""
        self.update_params_list()

        params = self.params_list
        params[3] = self.join_attr("window_size", "_")

        return super().get_params_list(params)
