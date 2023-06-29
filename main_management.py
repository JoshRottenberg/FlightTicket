from user_management import *
from flights_management import *
from order_management import OrderManagement


class MainManagement:
    def __init__(self):
        self.user_management = UserManagement()
        self.flights_management = FlightManagement()
        self.order_management = OrderManagement()
