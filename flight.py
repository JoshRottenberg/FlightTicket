import sqlite3


class Flight:
    def __init__(self, flight_code, date, company):
        self._flight_code = flight_code
        self._date = date
        self._company = company
        self._price = self.get_price()
        self._origin = self.get_origin()
        self._destination = self.get_dest()

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
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value

    def get_price(self):
        conn = sqlite3.connect("flights_base2.db")
        cursor = conn.cursor()
        query = f"SELECT PRICE FROM Flights WHERE TRANSACTIONID =  ?"
        cursor.execute(query, (self._flight_code,))

        output = cursor.fetchall()
        return output[0][0]

    def get_origin(self):
        conn = sqlite3.connect("flights_base2.db")
        cursor = conn.cursor()
        query = f"SELECT ORIGINCITYNAME FROM Flights WHERE TRANSACTIONID =  ?"
        cursor.execute(query, (self._flight_code,))

        output = cursor.fetchall()
        return output[0][0]

    def get_dest(self):
        conn = sqlite3.connect("flights_base2.db")
        cursor = conn.cursor()
        query = f"SELECT DESTCITYNAME FROM Flights WHERE TRANSACTIONID =  ?"
        cursor.execute(query, (self._flight_code,))

        output = cursor.fetchall()
        return output[0][0]
