class User:
    def __init__(self, id, name, last_name, phone_num, email, password, loged_in=bool):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._phone_num = phone_num
        self._email = email
        self._password = password
        self._is_loged_in = loged_in

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def phone_num(self):
        return self._phone_num

    @phone_num.setter
    def phone_num(self, value):
        self._phone_num = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def logged_in(self):
        return self._is_logged_in

    @logged_in.setter
    def logged_in(self, value):
        self._is_logged_in = value
