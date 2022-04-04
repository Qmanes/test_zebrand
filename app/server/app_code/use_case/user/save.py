from app_code.repository.user.user_repository import save, find_by_email
from app_code.model.User_model import User
from email_validator import validate_email, EmailNotValidError

def handle(email, fullname, password, is_root = False):

    user = preparate_user(email, fullname, password, is_root)

    assert_brand_email_not_repeat(user)

    return save_user(user)
    
def preparate_user(email, fullname, password, is_root):

    user = User(email = email, fullname = fullname)
    
    user.set_password(password)

    user.set_type(is_root)

    user.save()

    return user

def assert_brand_email_not_repeat(user):

    if find_by_email(user.email):

        user.raise_repeat_exception("Email")

def save_user(user):

    user = save(user)

    return user.as_dict()

