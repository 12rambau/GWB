from sepal_ui import sepalwidgets as sw


class DeprecatedTile(sw.Tile):
    def __init__(self, tile_id):
        alert = sw.Alert().show()
        markdown = sw.Markdown(
            f"The module {tile_id} has been deprecated. For details and alternatives, please view <a href='https://ies-ows.jrc.ec.europa.eu/gtb/GWB/GWB_changelog.txt' target='_blank'>the changelog</a>."
        )
        alert.add_msg(markdown, "warning")
        inputs = [alert]

        super().__init__(
            tile_id,
            title="Deprecated process",
            inputs=inputs,
        )
