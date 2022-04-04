from flask_restful import Resource
from app_code.use_case.stadistic.get_item_view import handle as get_item_view
from app_code.service.utils.response import try_catch
from flask_jwt_extended import jwt_required

class ItemViewStadistic(Resource):
    
    @jwt_required()
    def get(self):
        
        def handle():
            
            msg = "Item View Stadistic"

            return get_item_view(), msg

        return try_catch(handle)