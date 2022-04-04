from app_code.repository.brand.brand_repository import find_or_fail, update, find_by_name

def handle(brand_id, name):

    brand = preparate_brand(brand_id, name)

    assert_brand_name_not_repeat(brand)

    return update_brand(brand)

def preparate_brand(brand_id, name):

    brand = find_or_fail(brand_id)

    brand.edit(name = name)

    return brand

def assert_brand_name_not_repeat(brand):

    if find_by_name(brand.name):

        brand.raise_repeat_exception("Name")

def update_brand(brand):

    brand_updated = update(brand)

    return brand_updated.as_dict()