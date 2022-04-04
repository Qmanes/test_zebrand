from app_code.repository.brand.mock_repository import find_or_fail as find_or_fail_brand
from app_code.repository.item.mock import list_all as list_all_mock
from app_code.model.Item_Model import Item
from app_code.exception.basic_exception import NotFoundException

def find_or_fail(item_id):


    result = list(filter(lambda item: item.get("uid") == item_id, list_all_mock()))

    if result:

        item = Item(**result[0])

        brand = find_or_fail_brand(item.brand_id)

        item.set_brand(brand)

        return item
    
    raise NotFoundException("Item")

def all():

    return list(map(lambda item: Item(**item), list_all_mock()))

def save(item):

    list_all = all()

    list_all.append(item)

    return list_all

def update(item):

    return list(map(lambda item_iter: item_iter if item_iter.get_id() != item.get_id() else item, all()))

def delete(item_id):

    return list(filter(lambda item_iter: item_iter.get_id() != item_id, all()))
    




