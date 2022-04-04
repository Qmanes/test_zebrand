from flask_restful import Resource
from app_code.use_case.brand.find import handle as find_brand
from app_code.use_case.brand.all import handle as all_brand
from app_code.use_case.brand.save import handle as save_brand
from app_code.use_case.brand.update import handle as update_brand
from app_code.use_case.brand.delete import handle as delete_brand
from app_code.service.utils.response import try_catch
from flask_jwt_extended import jwt_required

from flask import request

class FindBrand(Resource):
    
    @jwt_required()
    def get(self):
        
        def handle():
            msg = "brand Find"

            brand_id = request.args.get('brand_id')

            return find_brand(brand_id), msg

        return try_catch(handle)

class AllBrand(Resource):

    @jwt_required()
    def get(self):
        
        def handle():
            
            msg = "brand All"

            return all_brand(), msg

        return try_catch(handle)

class SaveBrand(Resource):

    @jwt_required()
    def post(self):

        
        def handle():
            
            msg = "brand save"

            json = request.get_json()

            return save_brand(**json), msg

        return try_catch(handle)

class UpdateBrand(Resource):
    
    @jwt_required()
    def put(self):
        
        def handle():
            
            msg = "brand Edit"

            json = request.get_json()
           
            return update_brand(**json), msg

        return try_catch(handle)
    
class DeleteBrand(Resource):

    @jwt_required()
    def delete(self):
        
        def handle():
            
            msg = "brand Delete"

            json = request.get_json()

            return delete_brand(**json), msg

        return try_catch(handle)