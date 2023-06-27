import sqlite3


class Ticket:
    def __init__(self, pass_id, order_id, flight_id, price, seat=None, seat_class="economy"):
        self._pass_id = pass_id
        self._order_id = order_id
        self._flight_id = flight_id
        self._price = price
        self._seat = seat
        self._seat_class = seat_class
        self.add_to_tickets_db()

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

    def add_to_tickets_db(self):
        # Insert the user into the database
        conn = sqlite3.connect('big_data.db')
        cursor = conn.cursor()
        cursor.execute('''
                        INSERT INTO tickets (passenger_id, order_id, flight_code, seat_code, seat_class, price)
                        VALUES (?, ?, ?, ?, ?, ? )
                    ''', (self._pass_id, self._order_id, self._flight_id, self._seat, self._seat_class, self._price ))
        conn.commit()
        conn.close()
