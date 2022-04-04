from app_code.repository.user.user_repository import find_by_login
from app_code.repository.notification.notification_repository import get_unview_count

from flask_jwt_extended import create_access_token
def handle(username, password):

    user = validate_user(username, password)

    unview_count = get_notification_unview(user.get_uid())

    access_token = create_access_token(identity=user.get_uid())


    return {
        "access_token": access_token,
        "Notification Unview": unview_count
    }

def validate_user(username, password):

    user = find_by_login(username)

    user.validate_password(password)

    return user

def get_notification_unview(user_id):

    return  get_unview_count(user_id)
