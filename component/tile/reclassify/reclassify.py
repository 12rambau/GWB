import os
from pathlib import Path
from traitlets import List, Dict, Int
import ipyvuetify as v
import sepal_ui.sepalwidgets as sw

from ...widget.reclassifywgs import *


class CustomizeClass(v.Card):
    
    classes_files = List([]).tag(sync=True)
    
    def __init__(self, class_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title = v.CardTitle(children=['Edit or create new classifications'])
        self.class_path = class_path
        self.structure = {'id':'number', 'code':'number', 'description':'string'}
        self.w_class_file = v.Select(
            label='Select a classes file', 
            items=self.get_items(), 
            v_model='',
            dense=True
        )
        self.ct = ClassTable(
            out_path=self.class_path,
            _metadata = {'name':'class_table'}
        ).hide()

        use_btn = sw.Btn('Get table')
        self.children=[
            self.title,
            v.Flex(class_='d-flex', children=[
                self.w_class_file,
                use_btn,
            ]),
            self.ct
        ]
        self.get_classes_files()
        
        # Events
        self.ct.save_dialog.observe(self._refresh_files, 'reload')
        use_btn.on_event('click', self.get_class_table)
        
    def get_class_table(self, *args):
        """Display class table widget in view"""

        # Call class table method to build items
        self.ct.populate_table(self.structure, self.w_class_file.v_model)
        self.ct.show()
                
    def _refresh_files(self, *args):
        """Trigger event when a new file is created"""
        self.get_classes_files()
        self.w_class_file.items = self.get_items()
        
    def get_classes_files(self):
        """Search for classes inside module path"""

        look_up_folder = Path(self.class_path).glob('*.csv')
        module_classes_folder = (Path(os.getcwd())/'component/parameter').glob('*.csv')
        
        self.classes_files = [str(f) for f in (list(look_up_folder) + list(module_classes_folder))]
    
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
        
        self.alert_dialog = Dialog(transition=False)
        
        title = v.CardTitle(children=["Reclassify raster"])
        description = v.CardText(
            class_='py-0', 
            children=[sw.Markdown("Reclassify rasters")]
        )

        self.customize_class = CustomizeClass(self.class_path)
        self.w_class_file = v.Select(
            label='Select a classes file', 
            v_model='',
            dense=True
        )
        self.get_items()
        
        
#         self.w_reclassify = GeeSelector(self.alert_dialog, self.w_class_file)

        tabs_titles = ['Reclassify', 'Customize classification']
        tab_content = [
            v.Card(children=[
                title,
                description,
                self.w_class_file,
#                 self.w_reclassify
            ]),
            self.customize_class
        ]

        self.children=[
            self.alert_dialog,
            Tabs(tabs_titles, tab_content)
        ]
        
        # Events
        
        # Refresh tables
        
        self.customize_class.observe(self.get_items, 'classes_files')
        
    def get_items(self, *args):
        self.w_class_file.items =  [
            {'text':Path(f).name, 'value':f}  for f in self.customize_class.classes_files
        ]
        
    
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
        
class ClassTable(v.DataTable, sw.SepalWidget):
    
        
    def __init__(self, out_path, *args, **kwargs):
        """
        
        Args: 
            out_path (str): output path where table will be saved
        """
        self.out_path = out_path
        self.dialog = Output()

        self.edit_icon = v.Icon(children=['mdi-pencil'])
        edit_icon = sw.Tooltip(self.edit_icon, 'Edit selelcted row')
        
        self.delete_icon = v.Icon(children=['mdi-delete'])
        delete_icon = sw.Tooltip(self.delete_icon, 'Permanently delete the selected row')
        
        self.add_icon = v.Icon(children=['mdi-plus'])
        add_icon = sw.Tooltip(self.add_icon, 'Create a new element')
        
        self.save_icon = v.Icon(children=['mdi-content-save'])
        save_icon = sw.Tooltip(self.save_icon, 'Write current table on SEPAL space')
        self.save_dialog = SaveDialog(table=self, out_path=self.out_path, transition=False)
        
        slot = v.Toolbar(
            class_='d-flex mb-6',
            flat=True, 
            children=[
                self.dialog,
                v.ToolbarTitle(children=['Customization tools']),
                v.Divider(class_='mx-4', inset=True, vertical=True),
                v.Flex(class_='ml-auto', children=[edit_icon, delete_icon, add_icon]),
                v.Divider(class_='mx-4', inset=True, vertical=True),
                save_icon
            ]
        )
        
        self.v_slots = [{
            'name': 'top',
            'variable': 'top',
            'children': [slot]
        }]
        
        self.v_model = []
        self.item_key = 'id'
        self.show_select = True
        self.single_select = True
        self.hide_default_footer = True
        
        super().__init__(*args, **kwargs)
        
        
        self.edit_icon.on_event('click', self._edit_event)
        self.delete_icon.on_event('click', self._remove_event)
        self.add_icon.on_event('click', self._add_event)
        self.save_icon.on_event('click', self._save_event)
        
    def populate_table(self, structure, items_file):
        """ Populate table, it will fill the table with the items_file

        Args:
            structure (dict {'title':'type'}): Dictionary 
                with column names (key) and type of data (value)
            items (.txt): file containing classes and description

        """
        self.structure = structure
        
        self.headers =  [
            {'text': k.capitalize(), 'value': k} for k in structure.keys() if k!='id'
        ]

        self.items = [] if items_file == '' else self.get_items_from_txt(items_file)
    
    def get_items_from_txt(self, items_path):
        """Read txt file with classification"""
        
        items = []
        keys = self.structure.keys()
        with open(items_path) as f:
            for i, line in enumerate(f.readlines()):
                item = [it.replace('\n','') if isinstance(it, str) else it for it in [i]+line.split(',')]
                items+=[(dict(zip(keys, item)))]
                
        return items
    
    def _save_event(self, widget, event, data):
        
        with self.dialog:
            self.dialog.clear_output()
            self.save_dialog.v_model=True
            display(self.save_dialog)
            
        
    def _edit_event(self, widget, event, data):

        dial = EditDialog(
            schema = self.structure, 
            default= self.v_model[0],
            table = self,
            transition=False
        )
        with self.dialog:
            display(dial)
                    
    def _add_event(self, widget, event, data):
        
        dial = EditDialog(
            schema = self.structure, 
            table = self
        )
        with self.dialog:
            display(dial)
        
    def _remove_event(self, widget, event, data):
        """Remove current selected (self.v_model) element from table"""
        
        current_items = self.items.copy()
        current_items.remove(self.v_model[0])
        
        self.items = current_items
        
class EditDialog(v.Dialog):
    
    model = Dict().tag(sync=True)
    
    def __init__(self, table, schema,  *args, default = None, **kwargs):
        """
        
        Dialog to modify/create new elements on a table
        
        Args: 
            table (v.DataTable): Table linked with dialog
            schema (dict {'title':'type'}): Schema for table
            title (str): Title for the dialog
            default (dict): Dictionary with default valules
        """
        
        self.table = table
        self.default = default
        self.title = "New element" if not self.default else "Modify element"
        self.schema = schema
        self.v_model=True
        self.max_width=500
        self.overlay_opcity=0.7
        
        # Action buttons
        self.save = v.Btn(children=['Save'])
        save_tool = sw.Tooltip(self.save, 'Create new element')
        
        self.cancel = v.Btn(children=['Cancel'])
        cancel_tool = sw.Tooltip(self.cancel, 'Ignore changes')
        
        self.modify = v.Btn(children=['Modify'])
        modify_tool = sw.Tooltip(self.modify, 'Update row')
        
        save = [save_tool, cancel_tool]
        modify = [modify_tool, cancel_tool]
        
        actions = v.CardActions(children=save if not default else modify)
        
        super().__init__(*args, **kwargs)
        
        self.children=[
            v.Card(
                class_='pa-4',
                children=[
                    v.CardTitle(children=[self.title])] + \
                    self._get_widgets() + \
                    [actions]
            )
        ] 
        
        # Create events
        
        self.save.on_event('click', self._save)
        self.modify.on_event('click', self._modify)
        self.cancel.on_event('click', self._cancel)
        
    def _modify(self, widget, event, data):
        """Modify elements to the table"""
        
        current_items = self.table.items.copy()
        
        for i, item in enumerate(current_items):
            if item['id'] == self.model['id']:
                current_items[i] = self.model
        
        self.table.items = current_items
        self.v_model=False
    
    def _save(self, widget, event, data):
        """Add elements to the table"""
        
        current_items = self.table.items.copy()
        item_to_add = self.model
        new_items = [item_to_add] + current_items
        
        self.table.items = new_items
        self.v_model=False
                
    def _get_index(self):
        """Get an unique index for a new element"""
        
        index = 1 if not self.table.items else max([i['id'] for i in self.table.items])+1
        return index
        
    def _cancel(self, widget, event, data):
        """Close dialog"""
        
        self.v_model=False
    
    def _populate_dict(self, change, title):
        """Populate model with new values"""
        self.model[title] = change['new']
    
    def _get_widgets(self):
        
        widgets = []
        for title, type_ in self.schema.items():
            
            widget = v.TextField(label=title.capitalize(), type=type_, v_model='')
            widget.observe(partial(self._populate_dict, title=title), 'v_model')
                        
            if title == 'id': widget.disabled=True
                
            if self.default: 
                widget.v_model = self.default[title]
            else:
                if title=='id': widget.v_model = self._get_index()
                
            widgets.append(widget)
            
        return widgets
        
        
class SaveDialog(v.Dialog):
    
    reload = Int().tag(sync=True)
        
    def __init__(self, table, out_path, *args, **kwargs):
        
        self.max_width=500
        self.v_model = False
        self.out_path = Path(out_path)
        
        super().__init__(*args, **kwargs)
        
        self.table = table
        
        self.w_file_name = v.TextField(
            label='Insert output file name', 
            type='string', 
            v_model='new_table.txt'
        )
        
        # Action buttons
        self.save = v.Btn(children=['Save'])
        save = sw.Tooltip(self.save, 'Save table')
        
        self.cancel = v.Btn(children=['Cancel'])
        cancel = sw.Tooltip(self.cancel, 'Cancel')
                
        self.children=[
            v.Card(
                class_='pa-4',
                children=[
                    v.CardTitle(children=['Save table']),
                    self.w_file_name,
                    save,
                    cancel
                ]
            )
        ]
        
        # Create events
        
        self.save.on_event('click', self._save)
        self.cancel.on_event('click', self._cancel)
    
    def _save(self, *args):
        """Write current table on a text file"""
        
        file_name = self.w_file_name.v_model
        file_name = file_name.strip()
        if not '.csv'in file_name:
            file_name = f'{file_name}.csv'
        
        out_file = self.out_path/file_name
        with open(out_file, 'w') as f:
            for line in self._get_lines():
                f.write(",".join(line)+'\n')
        
        # Every time a file is saved, we update the current widget state
        # so it can be observed by other objects.
        self.reload+=1
        
        self.v_model=False
        
    def _cancel(self, *args):
        self.v_model=False
            
    def _get_lines(self):
        """Get list of lines from table"""
        # Skip the first element: 'id' on table
        return [list(item.values())[1:] for item in self.table.items]