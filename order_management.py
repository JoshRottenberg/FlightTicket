from user import User
from admin import Admin
from passenger import Passenger
from ticket import Ticket
from order import Order
from flight import Flight
from flights_management import *
from exeptions import *
import sqlite3
from user_management import *
import re


class OrderManagement:

    def create_new_order(self, user_id):
        user_id = user_id
        tickets_quantity = 0
        order_price = 0
        new_order = Order(user_id=user_id, num_of_tickets=tickets_quantity, total_price=order_price)
        pass

    def add_passenger(self):
        pf_name_status = False
        while not pf_name_status:
            p_f_name = input("Please enter passenger's first name: ")
            pf_name_status = validate_name(p_f_name)

        pl_name_status = False
        while not pl_name_status:
            p_l_name = input("Please enter passenger's last name: ")
            pl_name_status = validate_name(p_l_name)

        p_dob = input("Please enter passenger's D.O.B (yyyy/mm/dd): ")  # add exeptions

        pp_num_status = False
        while not pp_num_status:
            p_pass_num = input("Please enter passenger's passport number: ")
            pp_num_status = validate_passport(p_pass_num)

        new_passenger = Passenger(first_name=p_f_name, last_name=p_l_name, dob=p_dob, passport=p_pass_num)
        return new_passenger

    def delete_passenger(self):
        pass

    def add_ticket(self, pass_id, flight_id, price):
        seat = " "
        seat_class = ""
        price = ""

        new_ticket = Ticket(pass_id=pass_id, flight_id=flight_id, seat_class=seat_class,price=price)
# OrderManagement()
