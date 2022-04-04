from app_code.repository.user.user_repository import find_or_fail
def handle(user_id):


    result = find_or_fail(user_id)

    return result.as_dict()
