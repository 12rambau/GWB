import json

import ipyvuetify as v 

class Windows(v.Layout):
    
    def __init__(self, label="Thresholds"):
        
        # hidden textfield to save the v_model 
        # the v_model will be stored as json
        self.save = v.TextField(v_model = None)
        
        # create the inputs 
        self.text_fields = [v.TextField(placeholder = f'window {i+1}', v_model = None, type="number", class_='ml-1 mr-1') for i in range(10)]
        
        # title
        title = v.Html(tag='h4', children = [label])
        
        for w in self.text_fields:
            w.observe(self._on_change, 'v_model')
            
        super().__init__(
            class_ = "ma-5",
            row = True,
            children = [title, v.Layout(row=True, children = self.text_fields)]
        )
        
    def _on_change(self, change):
        
        # get the values of al widgets 
        values = [w.v_model for w in self.text_fields]
        
        # remove none values 
        values = [int(v) for v in values if v]
        
        # sort them  
        values.sort()
        
        # add them as json in the save field 
        self.save.v_model = json.dumps(values)
        
        return self
        