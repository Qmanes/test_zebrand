from flask_restful import Resource
from app_code.use_case.notification.find import handle as find_notification
from app_code.use_case.notification.all import handle as all_notification
from app_code.service.utils.response import try_catch
from flask_jwt_extended import jwt_required, get_jwt_identity

from flask import request

class FindNotification(Resource):
    
    @jwt_required()
    def get(self):
        
        def handle():
            msg = "brand Find"

            notification_id = request.args.get('notification_id')

            user_id = get_jwt_identity()

            return find_notification(user_id, notification_id), msg

        return try_catch(handle)

class AllNotification(Resource):

    @jwt_required()
    def get(self):
        
        def handle():
            
            msg = "brand All"
            user_id = get_jwt_identity()

            return all_notification(user_id), msg

        return try_catch(handle)