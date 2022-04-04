from app_code.repository.item.item_repository import find_or_fail
from app_code.use_case.item_view.save import handle as save_view
def handle(item_id):


    result = find_or_fail(item_id)

    save_view(result.get_uid())

    return result.as_dict()
