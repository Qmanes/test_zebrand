import json
from app_code.model.Basic_Model import Basic

class Item(Basic):

    def __init__(self, uid = None, sku = None, name = None, price = None, brand_id = None, status = None):
        
        super().__init__(status)

        self.uid = uid
        self.set_sku(sku)
        self.set_name(name)
        self.set_price(price)
        self.set_brand_id(brand_id)

    def set_presenter(self, uid, name):

        self.uid = uid
        self.name = name
        
    def edit(self , sku = None, name = None, price = None, brand_id = None):

        self.set_sku(sku) if sku else self.sku
        self.set_name(name) if name else self.name
        self.set_price(price) if price else self.price
        self.set_brand_id(brand_id) if brand_id else self.brand_id
        self.update()

    def set_brand(self, brand):

        self.brand = brand

    def as_dict(self):

        if hasattr(self, "brand"):
            
            self.brand = self.brand.as_dict()
        
        return super().as_dict()

    def set_sku(self, sku):

        sku = self.format_str_uppercase(sku)

        self.assert_field_required(sku, "Sku")

        self.sku = sku
    
    def set_name(self, name):

        name = self.format_str_capitalcase(name)

        self.assert_field_required(name, "Name")

        self.name = name
    
    def set_price(self, price):

        price = self.format_float(price)

        self.assert_field_required(price, "Price")

        self.price = price
    
    def set_brand_id(self, brand_id):

        self.assert_field_required(brand_id, "Brand_id")

        self.brand_id = brand_id