from app_code.repository.brand.brand_repository import all
def handle():


    all_brand = all()

    return list(map(lambda brand: brand.as_dict(), all_brand))
