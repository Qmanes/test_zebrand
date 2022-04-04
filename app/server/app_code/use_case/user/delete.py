from app_code.repository.user.user_repository import find_or_fail, delete

def handle(admin_id, user_id):

    user = find_or_fail(user_id)

    user.delete(admin_id)

    delete(user.get_uid())

