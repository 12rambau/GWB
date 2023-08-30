import ipyvuetify as v
import sepal_ui.sepalwidgets as sw
from sepal_ui.sepalwidgets.sepalwidget import Markdown
from sepal_ui.message import ms

disclaimer = """FAO declines all responsibility for errors or deficiencies in the database or software or in the documentation accompanying it for program maintenance and upgrading as well as for any damage that may arise from them.  
FAO also declines any responsibility for updating the data and assumes no responsibility for errors and omissions in the data provided.  
Users are, however, kindly asked to report any errors or deficiencies in this product to FAO.  

<center style="inline-block">
    <a href="http://www.openforis.org">
        <img 
            src="https://raw.githubusercontent.com/12rambau/sepal_ui/master/sepal_ui/frontend/images/dark/open-foris.png" 
            alt="Open-Foris_logo" 
            height="100" 
            class="ma-3"
        />
    </a>
    <a href="https://sepal.io">
        <img 
            src="https://raw.githubusercontent.com/12rambau/sepal_ui/master/sepal_ui/frontend/images/dark/sepal.png" 
            alt="SEPAL_logo" 
            height="100" 
            class="ma-3"
        />
    </a>
</center>"""


class TileDisclaimer(sw.Tile):
    """
    Create a about tile using a the generic disclaimer .md file.
    This tile will have the "about_widget" id and "Disclaimer" title.
    """

    def __init__(self, **kwargs):
        content = Markdown(disclaimer)

        super().__init__("about_tile", "Disclaimer", inputs=[content], **kwargs)
