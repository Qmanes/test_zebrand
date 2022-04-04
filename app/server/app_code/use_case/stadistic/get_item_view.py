from app_code.repository.item_view.item_view_repository import all
def handle():

    list_view = all()

    total_item_view = get_item_view(list_view)

    total_brand_view = get_brand_view(list_view)

    return {

        "item_view": total_item_view,
        "brand_view": total_brand_view
    }

def get_item_view(list_view):

    list_count = list(map(lambda x: x.item_name, list_view))

    return get_count(list_count)

def get_brand_view(list_view):

    list_count = list(map(lambda x: x.brand_name, list_view))

    return get_count(list_count)

def get_count(list_count):

    count_json = {}

    list(map(lambda x: set_count(list_count.count(x),count_json, x), list_count))

    return count_json
    
def set_count(count, count_json, item):

    if not item in count_json:

        count_json.setdefault(item, count)

