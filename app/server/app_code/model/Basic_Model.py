from  uuid import uuid1
from email_validator import validate_email, EmailNotValidError
from app_code.exception.basic_exception import NotChangeException, RequiredException, RepeatException

class Basic():

    def __init__(self, status=None):

        self.status = status

    def as_dict(self):

        return self.__dict__
        
    def save(self):

        self.uid = str(uuid1())
        self.status = "Active"
    
    def update(self):

        pass

    def delete(self):

        self.status = "Deleted"


    def get_uid(self):

        return self.uid
    
    def get_tuple_fields(self):

        obj_dict = self.as_dict()

        return tuple(obj_dict.keys())

    def get_tuple_values(self):

        obj_dict = self.as_dict()

        return tuple(obj_dict.values())

    def format_str_lowercase(self, string):

        string_clear = self.clear_string(string)
        
        return string_clear.lower()
    
    def format_str_capitalcase(self, string):

        string_clear = self.clear_string(string)
        
        return string_clear.capitalize()

    def format_str_uppercase(self, string):

        string_clear = self.clear_string(string)
        
        return string_clear.upper()

    def clear_string(self, string):

        return " ".join(string.split())

    def assert_than_has_change(self, self_field, field, field_name):

        if self_field == field:

            raise NotChangeException(field_name)

    def assert_field_required(self, field, field_name):

        if not field:

            self.raise_field_required(field_name)

    def assert_email_valid(self, field, field_name = None):

        validate_email(field)
    
    def format_float(self, value):

        return float(value)
    
    def raise_repeat_exception(self, title):

        raise RepeatException(title)

    def raise_field_required(self, field_name):

        raise RequiredException(field_name)
    