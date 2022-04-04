from app_code.repository.brand.mock import list_all as list_all_mock
from app_code.model.Brand_Model import Brand
from app_code.exception.basic_exception import NotFoundException

def find_or_fail(brand_id):

    result = list(filter(lambda brand: brand.get("uid") == brand_id, list_all_mock()))

    if result:

        return Brand(**result[0])
    
    raise NotFoundException("Brand")

def all():

    return list(map(lambda brand: Brand(**brand), list_all_mock()))

def save(brand):

    list_all = all()

    list_all.append(brand)

    return list_all

def update(brand):

    return list(map(lambda brand_iter: brand_iter if brand_iter.get_id() != brand.get_id() else brand, all()))

def delete(brand_id):

    return list(filter(lambda brand_iter: brand_iter.get_id() != brand_id, all()))
    




