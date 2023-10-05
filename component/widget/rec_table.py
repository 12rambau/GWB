import json

import ipyvuetify as v

from component import scripts as cs


class RecTable(v.SimpleTable):
    def __init__(self, byte_map=None):

        header = v.Html(
            tag="thead",
            children=[
                v.Html(
                    tag="tr",
                    children=[
                        v.Html(tag="th", children=["old value"]),
                        v.Html(tag="th", children=["new value"]),
                    ],
                )
            ],
        )

        self.tbody = v.Html(tag="tbody", children=[])

        # add a  hidden textfield to save the json
        self.save = v.TextField(v_model=json.dumps({i: i for i in range(256)}))

        # load the body
        self.reload_body(byte_map)

        # create the actual table
        super().__init__(children=[header, self.tbody], class_="mb-5")

    def reload_body(self, raster):
        """dynamically change the body of the widget according to the raster file."""
        # empty the tbody children
        self.tbody.children = []

        # get the file features :
        features = cs.unique(raster)

        # create 1 line for each feature
        tmp_children = []
        for i in features:

            # create a textField
            field = v.TextField(
                placeholder="any value in [0, 256[",
                type="number",
                v_model=None,
                value=i,
            )

            # js link to the global widget
            field.observe(self._on_change, "v_model")

            # wrap it in a row
            row = v.Html(
                tag="tr",
                children=[
                    v.Html(tag="td", children=[str(i)]),
                    v.Html(tag="td", children=[field]),
                ],
            )

            # add the row to the tbody
            tmp_children += [row]

        self.tbody.children += tmp_children

        return self

    def _on_change(self, change):

        # if value > 255 empty the textField
        if change["new"] > 255:
            change["owner"].v_model = None
            return

        # else we change the value of the dictionnary
        tmp_decode = json.loads(self.save.v_model)
        tmp_decode[change["owner"].value] = change["new"]
        self.save.v_model = json.dumps(tmp_decode)

        return self
