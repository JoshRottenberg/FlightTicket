# from user import User
# from admin import Admin
# from passenger import Passenger
# from ticket import Ticket
# from order import Order
# from flight import Flight
# from flights_management import *
# from exeptions import *
# import sqlite3
from user_management import *
from flights_management import *
from order_management import OrderManagement
import re


class MainManagement:
    def __init__(self, name):
        self._name = name
        self.user_management = UserManagement()
        self.flights_management = FlightManagement()
        self.order_management = OrderManagement()
MainManagement("gg")