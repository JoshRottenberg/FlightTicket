import sqlite3
class Flight:
    def __init__(self, flight_code, date, company, distance):
        self._flight_code = flight_code
        self._date = date
        self._company = company
        self._distance = distance
        self._price = self.get_price()
        self._origin = self.get_origin()
        self._destination = self.get_dest()


    def __iter__(self):
        yield self._flight_code
        yield self._date
        yield self._company
        yield self._distance


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