from app_code.repository.user.user_repository import find_or_fail, update

def handle(user_id, fullname):
    
    user = preparate_user(user_id, fullname)

    return update_user(user)

def preparate_user(user_id, fullname):

    user =find_or_fail(user_id)

    user.edit(fullname)

    return user

def update_user(user):

    user = update(user)

    return user.as_dict()
