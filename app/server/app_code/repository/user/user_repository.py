from app_code.repository.mariadb.Execute import Execute
from app_code.model.User_model import User
from app_code.exception.basic_exception import NotFoundException

TABLE = "users"

EXECUTE = Execute(TABLE, User, "User")

def find_or_fail(user_id):
    
   return EXECUTE.find_or_fail(user_id)

def all():

    return EXECUTE.all()


def find_by_email(user_email):

    condition = "email ='{}'".format(user_email)

    return EXECUTE.find_one(condition)

def find_by_login(username):

    condition = "email ='{}'".format(username)

    result = EXECUTE.find_one_result(condition)

    if result:
        
        user = User(*result)

        user.set_password_crypt(result[5])

        return user
    
    raise NotFoundException("User")

def save(user):

    return EXECUTE.save(user)

def update(user):

    data = "fullname = '{}'".format(user.fullname)

    condition = "uid = '{}'".format(user.get_uid())
    
    return EXECUTE.update(user.get_uid(), data, condition)

def delete(user_id):

    return EXECUTE.delete(user_id)