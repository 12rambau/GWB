import os
from functools import partial
from pathlib import Path
from traitlets import List, Dict, Int
import ipyvuetify as v
import sepal_ui.sepalwidgets as sw
from sepal_ui.scripts.utils import loading_button

from .datatable import *
from .reclassifytable import ReclassifyTable
from ...scripts.pre_processing import *
from ...widget.reclassifywgs import *


class CustomizeTile(v.Card):
    
    classes_files = List([]).tag(sync=True)
    
    def __init__(self, class_path=Path('~').expanduser()/'downloads', *args, **kwargs):
        
        """Stand-alone tile composed by a select widget containing .csv reclassify files
        found in the class_path, and a ClassTable to edit and/or create a new 
        classification table,
        
        Args:
            class_path (str) (optional): Folder path containing classification tables
        """
        
        super().__init__(*args, **kwargs)
        
        self.title = v.CardTitle(children=['Edit or create new classifications'])
        self.class_path = class_path
        
        self.w_class_file = v.Select(
            label='Select a classes file', 
            items=self.get_items(), 
            v_model='',
            dense=True
        )
        self.ct = ClassTable(
            out_path=self.class_path,
            schema = {'id':'number', 'code':'number', 'description':'string'},
        ).hide()

        use_btn = sw.Btn('Get table')
        self.children=[
            self.title,
            v.Flex(class_='ml-2 d-flex', children=[
                self.w_class_file,
                use_btn,
            ]),
            self.ct
        ]
        self.get_classes_files()
        
        # Events
        
        # Listen Class table save dialog to refresh the classes widget
        self.ct.save_dialog.observe(self._refresh_files, 'reload')
        
        # Get the corresponding table
        use_btn.on_event('click', self.get_class_table)
        
    def get_class_table(self, *args):
        """Display class table widget in view"""

        # Call class table method to build items
        self.ct.populate_table(self.w_class_file.v_model)
        self.ct.show()
                
    def _refresh_files(self, *args):
        """Trigger event when a new file is created"""
        self.get_classes_files()
        self.w_class_file.items = self.get_items()
        
    def get_classes_files(self):
        """Search for classes inside module path"""

        look_up_folder = Path(self.class_path).glob('*.csv')
        module_classes_folder = (Path(os.getcwd())/'component/parameter').glob('*.csv')
        
        self.classes_files = [str(f) for f in (list(look_up_folder) + \
                                               list(module_classes_folder))]
    
    def get_items(self):
        """Get items for widget selection"""
        self.get_classes_files()
        classes_files = [{'divider':True}, {'header':'New classification'}] + \
                        [{'text':'Create new classification...', 'value':''}] + \
                        [{'divider':True}, {'header':'Local classifications'}] + \
                        [{'text':Path(f).name, 'value':f}  for f in self.classes_files]

        return classes_files
    
    


class ReclassifyUI(v.Card, sw.SepalWidget):
    
    def __init__(self, *args, **kwargs):

        self.class_ = 'pa-4'

        super().__init__(*args, **kwargs)
        
        # Class parameters
                
        self.root_dir=None
        self.class_path=None
        self.workspace()
        
#         self.alert_dialog = Dialog(transition=False)
        self.alert_dialog = sw.Alert().hide()
        title = v.CardTitle(children=["Reclassify raster"])
        description = v.CardText(
            class_='py-0', 
            children=[sw.Markdown("Reclassify rasters")]
        )

        self.customize_class = CustomizeTile(self.class_path)
        self.w_class_file = v.Select(
            label='Select a classes file', 
            v_model='',
            dense=True
        )
        
        self.get_table_btn = sw.Btn('Get tables', class_='mb-2')
        self.save_raster_btn = sw.Btn('Reclassify', class_='my-2').hide()
        
        
        self.get_items()
    
        self.w_select_raster = sw.FileInput(['.tif'], label='Search raster')
        self.w_reclassify_table = ReclassifyTable().show()

        tabs_titles = ['Reclassify', 'Customize classification']
        tab_content = [
            v.Card(children=[
                title,
                description,
                self.w_select_raster,
                self.w_class_file,
                self.get_table_btn,
                self.w_reclassify_table,
                self.save_raster_btn,
                self.alert_dialog,
            ]),
            self.customize_class
        ]

        self.children=[
            Tabs(tabs_titles, tab_content)
        ]
        
        # Decorate functions
        self.reclassify_and_save = loading_button(self.save_raster_btn, self.alert_dialog)(self.reclassify_and_save)
        self.get_reclassify_table = loading_button(self.get_table_btn, self.alert_dialog)(self.get_reclassify_table)
        
        # Events
        self.get_table_btn.on_event('click', self.get_reclassify_table)
        self.save_raster_btn.on_event('click', self.reclassify_and_save)
        
        # Refresh tables        
        self.customize_class.observe(self.get_items, 'classes_files')
        
    def reclassify_and_save(self, *args):
        """Reclassify the input raster and save it in sepal space"""
        
        in_raster = self.w_select_raster.file
        change_matrix = self.w_reclassify_table.matrix
        
        map_values = {
            k: v['value'] if 'text' in change_matrix else v
                for k, v in change_matrix.items()
        }
            # Get reclassify path raster
        filename = Path(in_raster).stem
        dst_raster = Path('~').expanduser()/f'downloads/{filename}_reclassified.tif'
        
        reclassify_from_map(in_raster, map_values, dst_raster=dst_raster, overwrite=True)
        
        self.alert_dialog.add_msg('File {} succesfully reclassified'.format(dst_raster), type_='success')
                
    def get_reclassify_table(self, *args):
        """Display a reclassify table which will lead the user to select
        a local code 'from user' to a target code based on a classes file"""
        
        code_fields = unique(self.w_select_raster.file)
        self.w_reclassify_table._get_matrix(code_fields, self.w_class_file.v_model)
        self.save_raster_btn.show()
        
    def get_items(self, *args):
        """Get classes .csv files from the selected path"""
        
        self.w_class_file.items = [{'text':'Manual classification', 'value':''}] + \
                                  [{'divider':True}] + \
                                  [{'text':Path(f).name, 'value':f} for f in self.customize_class.classes_files]
    
    def workspace(self):
        """ Creates the workspace necessary to store the data

        return:
            returns env paths
        """

        base_dir = Path('~').expanduser()

        root_dir = base_dir/'module_results/gwb'
        class_path = root_dir/'custom_classification'

        root_dir.mkdir(parents=True, exist_ok=True)
        class_path.mkdir(parents=True, exist_ok=True)

        self.root_dir = root_dir
        self.class_path  = class_path
        
