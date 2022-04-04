from app_code.repository.setup import setup_repository
from app_code.use_case.user.save import handle as save_user

def handle():

    if setup_repository.create_users():

        save_user("admin@root.com", "Admin Root", "123456", is_root =True)

    setup_repository.create_items()
    setup_repository.create_brands()
    setup_repository.create_items_view()
    setup_repository.create_notifications()

    return "complete"
