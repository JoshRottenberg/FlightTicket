class Ticket:
    def __init__(self, ticket_id, pass_id, flight_id, seat, seat_class, price):
        self._ticket_id = ticket_id
        self._pass_id = pass_id
        self._flight_id = flight_id
        self._seat = seat
        self._seat_class = seat_class
        self._price = price

    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        self._ticket_id = value

    @property
    def pass_id(self):
        return self._pass_id

    @pass_id.setter
    def pass_id(self, value):
        self._pass_id = value

    @property
    def flight_id(self):
        return self._flight_id

    @flight_id.setter
    def flight_id(self, value):
        self._flight_id = value

    @property
    def seat(self):
        return self._seat

    @seat.setter
    def seat(self, value):
        self._seat = value

    @property
    def seat_class(self):
        return self._seat_class

    @seat_class.setter
    def seat_class(self, value):
        self._seat_class = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
