class User:
    # num_of_users = 1
    # users = []

    def __init__(self, first_name, last_name, phone_num, email, password, is_signed_in=False, logged_in=False):
        # self._id = User.num_of_users
        self._name = first_name
        self._last_name = last_name
        self._phone_num = phone_num
        self._email = email
        self._password = password
        self._is_signed_in = is_signed_in
        self._is_logged_in = logged_in
        # User.num_of_users += 1
        # User.users.append(self)
        self.add_to_file()

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

    def add_to_file(self):
        with open('users_instances.txt', 'a') as file:
            file.write(f"first name,{self._name}, last name,{self._last_name},"
                       f" phone number,{self._phone_num}, email,{self._email},"
                       f" password,{self._password}, signed?,{self._is_signed_in},"
                       f" logged?,{self._is_logged_in}  \n")
