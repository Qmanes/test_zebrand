from flask_restful import Resource
from app_code.use_case.user.find import handle as find_user
from app_code.use_case.user.all import handle as all_user
from app_code.use_case.user.save import handle as save_user
from app_code.use_case.user.update import handle as update_user
from app_code.use_case.user.delete import handle as delete_user
from app_code.service.utils.response import try_catch
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

class FindUser(Resource):
    
    @jwt_required()
    def get(self):
        
        def handle():
            
            msg = "User Find"

            user_id = request.args.get('user_id')

            return find_user(user_id), msg

        return try_catch(handle)

class AllUser(Resource):
    
    @jwt_required()
    def get(self):
        
        def handle():
            
            msg = "User All"

            return all_user(), msg

        return try_catch(handle)

class SaveUser(Resource):
    
    @jwt_required()
    def post(self):
        
        def handle():
            
            msg = "User save"

            json = request.get_json()
            
            return save_user(**json), msg

        return try_catch(handle)


class UpdateUser(Resource):

    @jwt_required()
    def put(self):
        
        def handle():
            
            msg = "User Edit"

            json = request.get_json()

            return update_user(**json), msg

        return try_catch(handle)
    

class DeleteUser(Resource):
    
    @jwt_required()
    def delete(self):
        
        def handle():
            
            msg = "User Delete"

            user_id = get_jwt_identity()


            json = request.get_json()

            return delete_user(user_id, **json), msg

        return try_catch(handle)