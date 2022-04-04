import json
from app_code.model.Basic_Model import Basic

class Notification(Basic):

    def __init__(self, uid = None, user_from = None, user_to = None, title = None, msg = None, datetime = None, status = None):

        super().__init__(status)

        self.uid = uid
        self.user_from = user_from
        self.user_to = user_to
        self.title = title
        self.msg = json.loads(msg)
        self.datetime = str(datetime)

    def save(self):

        delattr(self, "datetime")
        self.msg = json.dumps(self.msg)

        super().save()

    def is_active(self):

        return self.status == "Active"
    
    def set_status_view(self):

        self.status = "View"

    def get_title_format(self):

        return {
            "uid": self.get_uid(),
            "title": self.title,
            "date time": self.datetime
        }
