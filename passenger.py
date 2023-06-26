import sqlite3


class Passenger:
    def __init__(self, first_name, last_name, dob, passport):
        self._id = None
        self._first_name = first_name
        self._last_name = last_name
        self._dob = dob
        self._passport = passport
        self.add_to_psngr_db()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

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
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, value):
        self._dob = value

    @property
    def passport(self):
        return self._passport

    @passport.setter
    def passport(self, value):
        self._passport = value

    def add_to_psngr_db(self):
        # Insert the user into the database
        conn = sqlite3.connect('passengers_data.db')
        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO users (first_name, last_name, date_of_birth, passport_number)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self._first_name, self._last_name, self._dob, self._passport))
        conn.commit()
        conn.close()
