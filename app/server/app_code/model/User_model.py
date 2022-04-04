import json
import bcrypt

from app_code.model.Basic_Model import Basic
from app_code.exception.basic_exception import LoginException, DeleteYourSelfException, DeleteRootException

class User(Basic):

    def __init__(self, uid = None, fullname = None, email = None, type = None, status = None, *args, **Kwargs):

        self.uid = uid
        self.fullname = self.set_fullname(fullname)
        self.email = self.set_email(email)
        self.type = type

        super().__init__(status)

    def set_password(self, password):
        
        self.assert_field_required(password, "Password")

        self.password =  self.crypt_password(password)

    def set_password_crypt(self, password):

        self.password = password.encode("utf-8")

    def set_type(self, is_root):

        self.type = "admin" if not is_root else "root"

    def edit(self, fullname):

        fullname = self.set_fullname(fullname)

        self.assert_than_has_change(self.fullname, fullname, "Fullname")

        self.fullname = fullname

        self.update()
    
    def set_email(self, email):

        self.assert_field_required(email, "Email")

        self.assert_email_valid(email, "Email")

        return self.format_str_lowercase(email)

    def set_fullname(self, fullname):
       
        self.assert_field_required(fullname, "fullname")

        return self.format_str_capitalcase(fullname)

    def crypt_password(self, password):

        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def validate_password(self, password):
        
        if not bcrypt.checkpw(password.encode("utf-8"), self.password):

            raise LoginException()

    def delete(self, user_id):

        self.assert_that_not_delete_yourself(user_id)

        self.assert_that_not_delete_type_root()

        super().delete()

    def assert_that_not_delete_yourself(self, user_id):

        if self.get_uid() == user_id:

            raise DeleteYourSelfException()
    
    def assert_that_not_delete_type_root(self):

        if self.type == "root":

            raise DeleteRootException()