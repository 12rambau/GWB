from sepal_ui.scripts import utils as su

from component import widget as cw
from component.message import cm

from .gwb_tile import GwbTile


class RecTile(GwbTile):
    def __init__(self, model, convert_tile):

        # create the widgets
        self.rec_table = cw.RecTable()

        # bind to the io
        model.bind(self.rec_table.save, "recode_json")

        super().__init__(model=model, inputs=[self.rec_table])

        # link js behaviours
        convert_tile.alert.observe(self._on_class_change, "class")

    def _on_class_change(self, change):
        """update the table when a new file is loaded."""
        if any(class_ in change["new"] for class_ in ["success", "warning"]):
            self.rec_table.reload_body(self.io.bin_map)

        return self

    @su.loading_button()
    def _on_click(self, widget, event, data):

        # check inputs
        if not self.alert.check_input(self.model.bin_map, cm.bin.no_bin):
            return

        super()._on_click(widget, event, data)

        return
