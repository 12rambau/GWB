from sepal_ui import sepalwidgets as sw
import ipyvuetify as v

from component.message import cm
class FourBytes(sw.Tile):
    
    def __init__(self, io):
        
        #gather the io 
        self.io = io
        
        # create the widgets
        self.file = sw.FileInput(['.tif', '.tiff'])
        self.background = v.Select(label = 'background', items = None, v_model = None, chips = True, multiple = True)
        self.foreground = v.Select(label = 'foreground', items = None, v_model = None, chips = True, multiple = True)
        self.spe_background_1 = v.Select(label = 'spetial background 1', items = None, v_model = None, chips = True, multiple = True)
        self.spe_background_2 = v.Select(label = 'spetial background 2', items = None, v_model = None, chips = True, multiple = True)
        
        requirements = sw.Markdown(cm.requirement._4)

        # bind it to the io
        self.output = sw.Alert() \
            .bind(self.background, self.io, 'byte_1') \
            .bind(self.foreground, self.io, 'byte_2') \
            .bind(self.spe_background_1, self.io, 'byte_3') \
            .bind(self.spe_background_2, self.io, 'byte_4')
        
        # create the btn 
        btn = sw.Btn("Convert the imag classes")
        
        super().__init__(
            self.io.tile_id,
            "Select map classes",
            inputs = [
                requirements,
                self.file,
                self.background,
                self.foreground,
                self.spe_background_1, 
                self.spe_background_2, 
            ],
            output = self.output,
            btn = btn
        
        )