from app_code.repository.item.item_repository import all
def handle():

    all_item = all()

    return list(map(lambda item: item.as_dict(), all_item))
