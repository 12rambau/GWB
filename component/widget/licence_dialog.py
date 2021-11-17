import shutil

import ipyvuetify as v
from sepal_ui import sepalwidgets as sw

from component import parameter as cp
from component.message import cm


class LicenceDialog(sw.SepalWidget, v.Dialog):
    def __init__(self):

        with cp.eula_md.open() as f:
            licence = f.read()
        mkd = sw.Markdown(licence)
        text = v.CardText(children=[mkd])

        btn = v.CardActions(children=[sw.Btn(cm.app.licence.btn)])

        self.card = v.Card(children=[btn, v.Divider(), text, v.Divider(), btn])

        super().__init__(
            value=not self._is_gwb(),
            max_width="1000px",
            children=[self.card],
            persistent=True,
        )

        # link the btn behaviour
        btn.on_event("click", self._set_gwb)

    def _is_gwb(self):
        """return if the gwb EULA.TXT exist or not"""

        return cp.get_licence_dir().joinpath("EULA.txt").is_file()

    def _set_gwb(self, widget, event, data):
        """Write the EULA.txt file into the gwb hidden folder"""

        shutil.copy(cp.eula_txt, cp.get_licence_dir())
        self.value = False

        return self
