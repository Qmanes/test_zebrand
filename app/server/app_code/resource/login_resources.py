from flask_restful import Resource
from app_code.use_case.login.login_admin import handle as login_admin
from app_code.service.utils.response import try_catch
from flask import request

class LoginAdmin(Resource):
    
    def post(self):
        
        def handle():
            
            msg = "Login User"

            json = request.get_json()

            return login_admin(**json), msg

        return try_catch(handle)