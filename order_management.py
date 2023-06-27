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
        new_order = Order(user_id=user_id)
        return new_order

    def add_passenger(self):
        pf_name_status = False
        while not pf_name_status:
            p_f_name = input("Please enter passenger's first name: ")
            pf_name_status = validate_name(p_f_name)

        pl_name_status = False
        while not pl_name_status:
            p_l_name = input("Please enter passenger's last name: ")
            pl_name_status = validate_name(p_l_name)

        p_dob_status = False
        while not p_dob_status:
            p_dob = input("Please enter passenger's D.O.B (yyyy/mm/dd): ")
            p_dob_status = validate_dob_date(p_dob)

        pp_num_status = False
        while not pp_num_status:
            p_pass_num = input("Please enter passenger's passport number: ")
            pp_num_status = validate_passport(p_pass_num)

        new_passenger = Passenger(first_name=p_f_name, last_name=p_l_name, dob=p_dob, passport=p_pass_num)
        return new_passenger

    def delete_passenger(self):
        pass

    def add_ticket(self, pass_id, order_id, flight_id, price):
        while True:
            is_upgrade = input("Do you wish to upgrade your seat? (y/n): ")
            if is_upgrade.lower() == 'n' or is_upgrade.lower() == 'no':
                break
            elif is_upgrade.lower() == 'y' or is_upgrade.lower() == 'yes':
                while True:
                    seat_class = input("What is your preferred class? (business/first): ")
                    if seat_class.lower() == "business":
                        price = '$' + str(int(price[1:]) * 2)
                        print("The price for business class is {price}")
                        break
                    elif seat_class.lower() == "first":
                        price = '$' + str(int(price[1:]) * 3)
                        print("The price for first class is {price}")
                        break
            break

        new_ticket = Ticket(pass_id=pass_id, flight_id=flight_id, seat_class=seat_class,price=price, order_id=order_id)
        return new_ticket

    def delete_ticket(self):
        pass

    def update_order(self, order, price):
        order._num_of_tickets += 1
        order._total_price += price

