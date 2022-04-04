import json
from app_code.model.Basic_Model import Basic

class ItemView(Basic):

    def __init__(self, uid = None, item_id = None, datetime = None, status = None):

        super().__init__(status)

        self.uid = uid
        self.item_id = item_id
        self.datetime = datetime

    def save(self):

        delattr(self, "datetime")

        super().save()

    def set_item(self, item_name):

        self.item_name = item_name

    def set_brand(self, brand_name):

        self.brand_name = brand_name