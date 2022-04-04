from app_code.repository.notification.notification_repository import find_or_fail, update

def handle(user_id, notification_id):


    result = find_or_fail(notification_id, user_id)
    
    if result.is_active():

        result.set_status_view()

        result = update(user_id, result)

    return result.as_dict()