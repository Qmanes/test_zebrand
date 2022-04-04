from flask_restful import Resource
from app_code.use_case.setup.auto_setup import handle as auto_setup
from app_code.service.utils.response import try_catch

class AutoSetup(Resource):
    
    def get(self):
        
        def handle():
            
            msg = "Auto setup"

            return auto_setup(), msg

        return try_catch(handle)