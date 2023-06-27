from user import User
from admin import Admin
from passenger import Passenger
from ticket import Ticket
from order import Order
from flight import Flight
from flights_management import *
from exeptions import *
import sqlite3
from order_management import *
from main_management import *
from user_management import *
from flights_management import *
import re
import sys

def main():
    process = MainManagement('process')
    print("Hey! Welcome to the new friendly flight tickets reservation site")
    while True:
        is_new = input("Do you have an account? (y/n): ")
        if is_new.lower() == 'n' or is_new.lower() == 'no':
            cur_user = process.user_management.create_new_user()
            break
        elif is_new.lower() == 'y' or is_new.lower() == 'yes':
            cur_user = process.user_management.check_if_user()
            if cur_user:
                break

    print("Let's find the perfect flight for you")
    num_of_travelers = int(input("How many travelers?: "))
    new_flight = process.flights_management.search_for_flights(num_of_travelers)

    while True:
        is_order = input("Do you want to open a new order? (y/n): ")
        if is_order.lower() == 'y' or is_order.lower() == 'yes':
            cur_order = process.order_management.create_new_order(cur_user.get_user_id())
            break
        elif is_order.lower() == 'n' or is_order.lower() == 'no':
            print("OK, see you next time")
            exit(1)

    for passenger in range(num_of_travelers):
        cur_pass = process.order_management.add_passenger()
        cur_ticket = process.order_management.add_ticket(pass_id=cur_pass.get_pass_id(), order_id=cur_order._order_id , flight_id=new_flight._flight_code,price=new_flight._price)
        process.order_management.update_order(order=cur_order, price=cur_ticket._total_price)
    print("All successful!")



    return  # Close the main function


if __name__ == "__main__":
    main()
