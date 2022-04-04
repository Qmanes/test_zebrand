from app_code.repository.user.user_repository import find_or_fail, all
def handle():

    all_user = all()

    return list(map(lambda user: user.as_dict(), all_user))
