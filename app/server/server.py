from flask import Flask
from flask_restful import Api
from app_code.resource.setup_resources import AutoSetup 

from app_code.resource.user_resources import FindUser, AllUser, SaveUser, UpdateUser, DeleteUser
from app_code.resource.item_resources import FindItem, AllItem, SaveItem, UpdateItem, DeleteItem
from app_code.resource.brand_resources import FindBrand, AllBrand, SaveBrand, UpdateBrand, DeleteBrand
from app_code.resource.stadistic_resources import ItemViewStadistic
from app_code.resource.login_resources import LoginAdmin
from flask_jwt_extended import JWTManager

from app_code.resource.notification_resource import AllNotification, FindNotification
#from flask_cors import CORS, cross_origin


server = Flask(__name__)

server.config['JWT_SECRET_KEY'] = 'abcdefghijklemnopq'

server.config['PROPAGATE_EXCEPTIONS'] = True

jwt = JWTManager(server)


api = Api(server)

#CORS(server)

#----------------Login--------------------

api.add_resource(LoginAdmin, '/admin/login')


#----------------Users--------------------

api.add_resource(FindUser, '/user/find')
api.add_resource(AllUser, '/user/all')
api.add_resource(SaveUser, '/user/save')
api.add_resource(UpdateUser, '/user/update')
api.add_resource(DeleteUser, '/user/delete')

#----------------Items--------------------

api.add_resource(FindItem, '/item/find')
api.add_resource(AllItem, '/item/all')
api.add_resource(SaveItem, '/item/save')
api.add_resource(UpdateItem, '/item/update')
api.add_resource(DeleteItem, '/item/delete')

#----------------Brand--------------------

api.add_resource(FindBrand, '/brand/find')
api.add_resource(AllBrand, '/brand/all')
api.add_resource(SaveBrand, '/brand/save')
api.add_resource(UpdateBrand, '/brand/update')
api.add_resource(DeleteBrand, '/brand/delete')


#----------------Brand--------------------

api.add_resource(FindNotification, '/notification/find')
api.add_resource(AllNotification, '/notification/all')

#----------------Stadistic--------------------

api.add_resource(ItemViewStadistic, '/stadistic/item-view')

#----------------Setup--------------------

api.add_resource(AutoSetup, '/setup/auto-setup')


if __name__ == "__main__":
   server.run(host='0.0.0.0', debug= True) 
