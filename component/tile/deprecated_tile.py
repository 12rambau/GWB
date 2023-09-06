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


class DeprecatedTile(sw.Tile):
    def __init__(self, tile_id):
        alert = sw.Alert().show()
        markdown = sw.Markdown(
            f"The module {tile_id} has been deprecated. For details and alternatives, please view <a href='https://ies-ows.jrc.ec.europa.eu/gtb/GWB/GWB_changelog.txt' target='_blank'>the changelog</a>."
        )
        alert.add_msg(markdown, "info")
        inputs = [alert]

        super().__init__(
            tile_id,
            title="Deprecated process",
            inputs=inputs,
        )
