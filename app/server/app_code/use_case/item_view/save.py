from app_code.model.ItemView_Model import ItemView
from app_code.repository.item_view.item_view_repository import save

def handle(item_id):

    item_view = ItemView(item_id=item_id)

    item_view.save()
    
    save(item_view)

