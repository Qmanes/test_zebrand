class NotFoundException(Exception):
    
    def __init__(self, title):

        self.message = "{title} Not Found".format(title = title)
        super().__init__(self.message)

class NotChangeException(Exception):
    
    def __init__(self, title):

        self.message = "Field {title} not has change".format(title = title)
        super().__init__(self.message)

class RepeatException(Exception):
    
    def __init__(self, title):

        self.message = "{title} name exist in db".format(title = title)
        super().__init__(self.message)

class RequiredException(Exception):
    
    def __init__(self, title):

        self.message = "The field {title} is required".format(title = title)
        super().__init__(self.message)

class LoginException(Exception):
    
    def __init__(self):

        self.message = "Username or Password Incorrect"
        super().__init__(self.message)

class DeleteRootException(Exception):

    def __init__(self):

        self.message = "El usuario root no puede ser eliminado"
        super().__init__(self.message)

class DeleteYourSelfException(Exception):

    def __init__(self):

        self.message = "No puede eliminarse usted mismo"
        super().__init__(self.message)