from app_code.repository.brand.brand_repository import save, find_by_name
from app_code.model.Brand_Model import Brand

def handle(name):

    brand = preparate_brand(name)

    assert_brand_name_not_repeat(brand)

    return save_brand(brand)
    
def preparate_brand(name):

    brand = Brand(name = name)

    brand.save()

    return brand

def assert_brand_name_not_repeat(brand):


    if find_by_name(brand.name):

        brand.raise_repeat_exception("Name")

def save_brand(brand):

    brand_save = save(brand)

    return brand_save.as_dict()