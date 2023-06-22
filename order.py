class Order:
    def __init__(self, user_id, ticket_arr, num_of_tickets, price):
        self._user_id = user_id
        self._ticket_arr = ticket_arr
        self._num_of_tickets = num_of_tickets
        self._price = price

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def ticket_arr(self):
        return self._ticket_arr

    @ticket_arr.setter
    def ticket_arr(self, value):
        self._ticket_arr = value

    @property
    def ticket_num(self):
        return self._ticket_num

    @ticket_num.setter
    def ticket_num(self, value):
        self._ticket_num = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
