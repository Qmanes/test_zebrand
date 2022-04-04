from app_code.repository.item.item_repository import save, get_brand, find_by_sku
from app_code.use_case.notification.notificate_item_save import handle as notificate_item_save
from app_code.model.Item_Model import Item

def handle(user_id, sku, name, price, brand_id):

    item = preparate_item(sku, name, price, brand_id)
    
    assert_brand_sku_not_repeat(item)

    notificate_item_save(user_id, item)

    return save_item(item)
    
def preparate_item(sku, name, price, brand_id):

    brand = get_brand(brand_id)

    item = Item(sku = sku, name = name, price = price, brand_id = brand.get_uid())

    item.save()

    return item

def assert_brand_sku_not_repeat(item):

    if find_by_sku(item.sku):

        item.raise_repeat_exception("Sku")

def save_item(item):

    item_save = save(item)

    return item_save.as_dict()