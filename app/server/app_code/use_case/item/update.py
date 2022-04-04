from app_code.repository.item.item_repository import find_or_fail, update, find_by_sku, get_brand
from app_code.use_case.notification.notificate_item_update import handle as notificate_item_update

def handle(user_id, item_id, sku, name, price, brand_id):

    item_old = find_or_fail(item_id)

    item_update = preparate_item(item_old, sku, name, price, brand_id)
    
    assert_brand_sku_not_repeat(item_update)

    notificate_item_update(user_id, item_old, item_update)
    
    return update_item(item_update)

def preparate_item(item, sku, name, price, brand_id):

    brand = get_brand(brand_id)

    item.edit(sku = sku, name = name, price = price, brand_id = brand.get_uid())

    delattr(item, "brand")

    return item

def assert_brand_sku_not_repeat(item):

    if find_by_sku(item.sku, item.get_uid()):

        item.raise_repeat_exception("Sku")

def update_item(item):

    item_updated = update(item)

    return item_updated.as_dict()