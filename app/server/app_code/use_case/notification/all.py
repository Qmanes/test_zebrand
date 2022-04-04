from app_code.repository.notification.notification_repository import all

def handle(user_id):

    all_notification = all(user_id)

    return list(map(lambda item: item.get_title_format(), all_notification))