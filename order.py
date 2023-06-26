import sqlite3


class Order:
    def __init__(self, user_id=0, num_of_tickets=0, total_price=0):
        self._user_id = user_id
        self._num_of_tickets = num_of_tickets
        self._total_price = total_price
        self.add_order_db()

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def num_of_tickets(self):
        return self._num_of_tickets

    @num_of_tickets.setter
    def num_of_tickets(self, value):
        self._num_of_tickets = value

    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        self._total_price = value

    def add_order_db(self):
        # Insert the user into the database
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO orders (user_id, num_of_tickets, total_price)
                VALUES (?, ?, ? )
            ''', (self._user_id, self._num_of_tickets, self._total_price))
        conn.commit()
        conn.close()
