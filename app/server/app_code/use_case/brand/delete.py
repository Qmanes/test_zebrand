from app_code.repository.brand.brand_repository import find_or_fail, delete

def handle(brand_id):

    brand = find_or_fail(brand_id)

    delete(brand.get_uid())