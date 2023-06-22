class Flight:
    def __init__(self):
        self._id = None
        self._flight_code = None
        self._date = None
        self._origin_code = None
        self._dest_code = None
        self._company = None
        self._duration = None
        self._distance = None
        self._seats = None
        self._available_seats = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def flight_code(self):
        return self._flight_code

    @flight_code.setter
    def flight_code(self, value):
        self._flight_code = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def origin_code(self):
        return self._origin_code

    @origin_code.setter
    def origin_code(self, value):
        self._origin_code = value

    @property
    def dest_code(self):
        return self._dest_code

    @dest_code.setter
    def dest_code(self, value):
        self._dest_code = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        self._seats = value

    @property
    def available_seats(self):
        return self._available_seats

    @available_seats.setter
    def available_seats(self, value):
        self._available_seats = value
