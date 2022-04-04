from app_code.repository.brand.brand_repository import find_or_fail
def handle(brand_id):


    result = find_or_fail(brand_id)

    return result.as_dict()
