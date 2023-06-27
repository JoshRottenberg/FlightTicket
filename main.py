from user import User
from admin import Admin
from passenger import Passenger
from ticket import Ticket
from order import Order
from flight import Flight
from flights import *
from exeptions import *
import sqlite3
from sys_cntrl import *
import re


def search_for_flights(num_of_travelers):
    num_of_passengers = num_of_travelers
    origin_city = input("From which city are you flying from?: ")
    is_available_flight = False
    while not is_available_flight:
        destination_city = input("To which city are you flying to?: ")
        departure_date = input("Please enter your departure date (yyyy/mm/dd): ")
        list_of_flights = flight_found(origin_city=origin_city, destination_city=destination_city,
                                       departure_date=departure_date,
                                       num_of_seats=num_of_passengers)
        if list_of_flights:
            is_available_flight = True

    chosen_flight = choose_flight(list_of_flights)

    return chosen_flight


def add_passenger():
    pf_name_status = False
    while not pf_name_status:
        p_f_name = input("Please enter passenger's first name: ")
        pf_name_status = validate_name(p_f_name)

    pl_name_status = False
    while not pl_name_status:
        p_l_name = input("Please enter passenger's last name: ")
        pl_name_status = validate_name(p_l_name)

    p_dob = input("Please enter passenger's D.O.B (yyyy-mm-dd): ")  # add exeptions

    pp_num_status = False
    while not pp_num_status:
        p_pass_num = input("Please enter passenger's passport number: ")
        pp_num_status = validate_passport()

    new_passenger = Passenger(first_name=p_f_name, last_name=p_l_name, dob=p_dob, passport=p_pass_num)


def create_new_order(user_id):
    user_id = user_id
    tickets_quantity = 0
    order_price = 0
    new_order = Order(user_id=user_id, num_of_tickets=tickets_quantity, total_price=order_price)
    pass


def buy_ticket(flight_code):
    pass_id = passenger_id
    flight_id = flight_code
    seat_class = seat_class

    new_ticket = Ticket(flight_id=flight_id, seat_class=seat_class)




def main():
    # managment = Controler()
    print("Hey! Welcome to the new friendly flight tickets reservation site")
    while True:
        is_new = input("Do you have an account? (y/n): ")
        if is_new.lower() == 'n' or is_new.lower() == 'no':
            cur_user = Controler.create_new_user()
            break
        elif is_new.lower() == 'y' or is_new.lower() == 'yes':
            cur_user = Controler.check_if_user()
            if cur_user:
                break

    print("Let's find the perfect flight for you")
    num_of_travelers = int(input("How many travelers?: "))
    new_flight = search_for_flights(num_of_travelers)

    while True:
        new_order = input("Do you want to open a new order? (y/n): ")
        if new_order.lower() == 'y' or new_order.lower() == 'yes':
            create_new_order(cur_user.get_user_id())
            break
        elif new_order.lower() == 'n' or new_order.lower() == 'no':
            print("OK, see you next time")
            break

    return  # Close the main function


if __name__ == "__main__":
    main()
