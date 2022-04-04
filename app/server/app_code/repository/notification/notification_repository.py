from app_code.repository.mariadb.Execute import Execute
from app_code.model.Notification_Model import Notification
from app_code.exception.basic_exception import NotFoundException

TABLE = "notifications"

EXECUTE = Execute(TABLE, Notification, "Notification")


def find_or_fail(notification_id, user_id):

    condition = "uid = '{}' and user_to = '{}' and status != 'Delete'".format(notification_id, user_id)
    
    result =  EXECUTE.find_one(condition)

    if not result:

        raise NotFoundException("User Admin")

    return result
    
def update(user_id, notification):

    data = "status = '{}'".format(notification.status)

    condition = "uid = '{}' AND user_to = '{}'".format(notification.get_uid(), user_id)
    
    return EXECUTE.update(notification.get_uid(), data, condition)

def all(user_id):

    condition = "AND user_to = '{}'".format(user_id)

    return EXECUTE.all(condition)
    
def save_list(notification_list):

    return list(map(lambda notification: EXECUTE.save(notification), notification_list))

def get_unview_count(user_id):

    condition = "user_to = '{}' and status = 'Active'".format(user_id)

    count = EXECUTE.find_count(condition)

    return count[0]