import sqlite3


class User:

    def __init__(self, first_name=None, last_name=None, phone_num=None, email=None, password=None, is_signed_up=False):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_num = phone_num
        self._email = email
        self._password = password
        self._is_signed_up = is_signed_up
        self.add_to_db() if not self._is_signed_up else None

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

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

    def add_to_db(self):
        # Insert the user into the database
        conn = sqlite3.connect('big_data.db')
        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO users (first_name, last_name, phone_num, email, password)
                VALUES (?, ?, ?, ?, ?)
            ''', (self._first_name, self._last_name, self._phone_num, self._email, self._password))
        conn.commit()
        conn.close()

    def get_user_id(self):
        conn = sqlite3.connect('big_data.db')
        cursor = conn.cursor()
        query = f"SELECT id FROM users WHERE email =  ?"
        cursor.execute(query, (self._email,))

        output = cursor.fetchall()
        return output[0][0]
