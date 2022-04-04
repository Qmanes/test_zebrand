from app_code.repository.brand.brand_repository import find_or_fail as get_brand
from app_code.repository.mariadb.Execute import Execute
from app_code.model.Item_Model import Item

TABLE = "items"

EXECUTE = Execute(TABLE, Item, "Item")

def find_or_fail(item_id):

    item = EXECUTE.find_or_fail(item_id)

    return set_with_brand(item)

def all():

    list_all = EXECUTE.all()

    return list(map(lambda item: set_with_brand(item), list_all))

def find_by_sku(item_sku, item_id = None):

    condition = "sku ='{}' {}".format(item_sku, " AND uid != '{}'".format(item_id) if item_id else "")

    return EXECUTE.find_one(condition)

def save(item):

    item = EXECUTE.save(item)

    return set_with_brand(item)

def update(item):

    data = """
        name = '{name}',
        sku = '{sku}',
        price = '{price}',
        brand_id = '{brand_id}'
    
    """.format(name = item.name, sku = item.sku, price = item.price, brand_id = item.brand_id)

    condition = "uid = '{}'".format(item.get_uid())
    
    item = EXECUTE.update(item.get_uid(), data, condition)

    return set_with_brand(item)


def delete(item_id):

    return EXECUTE.delete(item_id)


def set_with_brand(item):

    brand = get_brand(item.brand_id)

    item.set_brand(brand)

    return item