from flask_restful import Resource
from app_code.use_case.item.find import handle as find_item
from app_code.use_case.item.all import handle as all_item
from app_code.use_case.item.save import handle as save_item
from app_code.use_case.item.update import handle as update_item
from app_code.use_case.item.delete import handle as delete_item
from app_code.service.utils.response import try_catch
from flask import request

from flask_jwt_extended import (jwt_required,get_jwt_identity)

class FindItem(Resource):
    
    def get(self):
        
        def handle():
            
            msg = "Item Find"
            
            item_id = request.args.get('item_id')

            return find_item(item_id), msg

        return try_catch(handle)

class AllItem(Resource):

    def get(self):
        
        def handle():
            
            msg = "Item All"

            return all_item(), msg

        return try_catch(handle)

class SaveItem(Resource):
    
    @jwt_required()
    def post(self):
        
        def handle():
            
            user_id = get_jwt_identity()


            msg = "Item save"

            json = request.get_json()

            return save_item(user_id, **json), msg

        return try_catch(handle)

class UpdateItem(Resource):

    @jwt_required()
    def put(self):
        
        def handle():
            
            msg = "Item Edit"

            user_id = get_jwt_identity()

            json = request.get_json()

            return update_item(user_id, **json), msg

        return try_catch(handle)
    
class DeleteItem(Resource):

    @jwt_required()
    def delete(self):
        
        def handle():
            
            msg = "Item Delete"

            user_id = get_jwt_identity()

            json = request.get_json()

            return delete_item(user_id, **json), msg

        return try_catch(handle)