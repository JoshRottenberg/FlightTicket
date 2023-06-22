class Passenger:
    def __init__(self):
        self._id = None
        self._first_name = None
        self._last_name = None
        self._dob = None
        self._passport = None

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
