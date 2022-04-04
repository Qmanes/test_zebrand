import json
from app_code.model.Basic_Model import Basic

class Brand(Basic):

    def __init__(self, uid = None, name = None, status = None):
        
        super().__init__(status)

        self.uid = uid

        self.name = self.set_name(name) 

    def edit(self, name):

        name = self.format_str_capitalcase(name) 

        self.assert_than_has_change(self.name, name, "Name")

        self.name = name

        self.update()

    def set_name(self, name):
        
        self.assert_field_required(name, "Name")

        return self.format_str_capitalcase(name)
