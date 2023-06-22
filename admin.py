from user import User


class Admin(User):
    def __init__(self, id, name, last_name, phone_num, email, password, logged_in=False):
        super().__init__(id, name, last_name, phone_num, email, password, logged_in)
