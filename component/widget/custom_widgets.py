from typing import Literal

import sepal_ui.sepalwidgets as sw
from component.scripts.gwb_version import get_gwb_version


class CustomAppBar(sw.AppBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        version = get_gwb_version()

        version_holder = sw.Flex(
            class_="d-inline-flex justify-end",
            children=[
                sw.Html(
                    tag="span",
                    class_="text--secondary mr-1",
                    children=[f"Running GWB: v.{version}"],
                ),
            ],
        )

        self.children = self.children[:3] + [version_holder] + self.children[3:]
