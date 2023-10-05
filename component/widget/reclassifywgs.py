import ipyvuetify as v
from IPython.display import display
from ipywidgets import Output
from traitlets import Int, link


class Dialog(v.Dialog):
    def __init__(self, output=None, *args, **kwargs):

        self.output = output if output else Output()

        self.v_model = False
        self.max_width = 436
        self.overlay_color = "black"
        self.overlay_opcity = 0.7
        self.children = [v.Card(children=[self.output])]

        super().__init__(*args, **kwargs)

    def alert(self, alert):
        self.v_model = True
        with self.output:
            self.output.clear_output()
            display(alert)


class Tabs(v.Card):

    current = Int(0).tag(sync=True)

    def __init__(self, titles, content, **kwargs):

        self.background_color = "primary"
        self.dark = True

        self.tabs = [
            v.Tabs(
                v_model=self.current,
                children=[
                    v.Tab(children=[title], key=key) for key, title in enumerate(titles)
                ],
            )
        ]

        self.content = [
            v.TabsItems(
                v_model=self.current,
                children=[
                    v.TabItem(children=[content], key=key)
                    for key, content in enumerate(content)
                ],
            )
        ]

        self.children = self.tabs + self.content

        link((self.tabs[0], "v_model"), (self.content[0], "v_model"))

        super().__init__(**kwargs)
