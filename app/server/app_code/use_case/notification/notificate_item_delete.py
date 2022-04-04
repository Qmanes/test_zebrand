from app_code.repository.user.user_repository import all as all_user
from app_code.repository.notification.notification_repository import save_list
from app_code.model.Notification_Model import Notification
import json

def handle(user_from, item ):

    list_user  = all_user()

    user = list(filter(lambda user: user.get_uid() == user_from, list_user))

    title = "{} ha eliminado un item".format(user[0].fullname)

    msg =json.dumps({
        "deleted_item": item.as_dict()
    })

    list_user_id = list(map(lambda user: preparate_notification(user_from, user.get_uid(), title, msg) ,list_user))
    
    save_list(list_user_id)

def preparate_notification(user_from, user_to, title, msg):

    notification = Notification(user_from=user_from, user_to = user_to, title=title, msg=msg)

    notification.save()

    return notification
