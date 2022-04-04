from app_code.repository.item.item_repository import find_or_fail, delete
from app_code.use_case.notification.notificate_item_delete import handle as notificate_item_delete


def handle(user_id, item_id):

    item = find_or_fail(item_id)

    notificate_item_delete(user_id, item)

    delete(item.get_uid())

