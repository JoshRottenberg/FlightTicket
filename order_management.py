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
import random


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
        seat_class = "economy"
        seat = self.take_seat(grade="economy")
        while True:
            is_upgrade = input("Do you wish to upgrade your seat? (y/n): ")
            if is_upgrade.lower() == 'n' or is_upgrade.lower() == 'no':
                print(f"The price for economy class is {price}, passenger seat: {seat}")
                break
            elif is_upgrade.lower() == 'y' or is_upgrade.lower() == 'yes':
                while True:
                    seat_class = input("What is your preferred class? (business/first): ")
                    if seat_class.lower() == "business":
                        price = '$' + str(int(price[1:]) * 2)
                        seat = self.take_seat(grade="business")
                        print(f"The price for business class is {price}, passenger seat: {seat}")
                        break
                    elif seat_class.lower() == "first":
                        price = '$' + str(int(price[1:]) * 3)
                        seat = self.take_seat(grade="first")
                        print(f"The price for first class is {price}, passenger seat: {seat}")
                        break
            break

        new_ticket = Ticket(pass_id=pass_id, flight_id=flight_id, seat_class=seat_class,price=price, order_id=order_id, seat=seat)
        return new_ticket

    def delete_ticket(self):
        pass

    def update_order(self, order, price):
        order._num_of_tickets += 1
        order._total_price += price

    def take_seat(self, grade):
        if grade == "economy":
            seat_letter = random.choice([chr(i) for i in range(65, 75)])
            seat_number = random.randint(16, 50)
        elif grade == "business":
            seat_letter = random.choice([chr(i) for i in range(65, 71)])
            seat_number = random.randint(6, 16)
        elif grade == "first":
            seat_letter = random.choice([chr(i) for i in range(65, 68)])
            seat_number = random.randint(1, 6)
        seat = str(seat_number) + seat_letter
        return seat

    def payment(self, total_price):
        print("To complete the reservation, commit payment")
        cc_status = False
        while not cc_status:
            cc = input("Please type your Credit Card number (digits only)")
            cc_status = validate_cc(cc)
        # Check the length of the card number and validate the card issuer
        if len(cc) == 15 and cc[:2] in ['34', '37']:
            card_issuer = 'American Express'
        elif len(cc) == 16 and cc[:2] in ['51', '52', '53', '54', '55']:
            card_issuer = 'MasterCard'
        elif len(cc) in [13, 16] and cc[0] == '4':
            card_issuer = 'Visa'
        print(f"Your card issuer is {card_issuer}")
        cc_date_status = False
        while not cc_date_status:
            cc_date = input("Please type your Credit Card expiration date (format mm/yy)")
            cc_date_status = validate_cc_date(cc_date)
        cvv_status = False
        while not cvv_status:
            cvv = input("Please type your cvv")
            cvv_status = validate_cvv(cvv, card_issuer)
        print("Reservation completed!!, Thank you for using our services")

