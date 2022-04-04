from app_code.repository.user.mock import list_all as list_all_mock
from app_code.model.User_model import User
from app_code.exception.basic_exception import NotFoundException

def find_or_fail(user_id):

    result = list(filter(lambda user: user.get("uid") == user_id, list_all_mock()))

    if result:

        return User(**result[0])
    
    raise NotFoundException("User")

def all():

    return list(map(lambda user: User(**user), list_all_mock()))

def save(user):

    list_all = all()

    list_all.append(user)

    return list_all

def update(user):

    return list(map(lambda user_iter: user_iter if user_iter.get_id() != user.get_id() else user, all()))

def delete(user_id):

    return list(filter(lambda user_iter: user_iter.get_id() != user_id, all()))
    




