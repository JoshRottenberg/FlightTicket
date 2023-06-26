from user import User
from admin import Admin
from passenger import Passenger
from ticket import Ticket
from order import Order
from flight import Flight
from flights import *
from exeptions import * 
import sqlite3


def create_new_user():
    f_name_status = False
    while not f_name_status:
        first_name = input("What is your first name?: ")
        f_name_status = validate_name(first_name)

    l_name_status = False
    while not l_name_status:
        last_name = input("What is your last name?: ")
        l_name_status = validate_name(last_name)

    p_num_status = False
    while not p_num_status:
        phone_num = input("Please enter your phone num: ")
        p_num_status = validate_phone_num(phone_num)

    email_status = False
    while not email_status:
        email = input("Please enter your Email address: ")
        email_status = validate_email(email)

    pass_status = False
    while not pass_status:
        new_password = input("What is your password: ")
        pass_status = validate_password(new_password)

    current_user = User(first_name=first_name, last_name=last_name, phone_num=phone_num, email=email,
                        password=new_password)
    return current_user


def check_if_user():
    user_name = input("Please enter your username (Email): ")
    password = input("Please enter your password: ")
    # Connect to the database
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    # Execute a SELECT query to retrieve the user with the given username and password
    cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (user_name, password))
    row = cursor.fetchone()
    # Close the connection
    conn.close()
    if row is not None:
        # User found in the database
        print(f"Welcome back, {row[1]}!")
        current_user = User(email=user_name, password=password, is_signed_up=True)
        return current_user
        # return True
    else:
        # User not found in the database or invalid credentials
        print("One of the details is incorrect. Please retry.")
        return False


def search_for_flights(num_of_travelers):
    num_of_passengers = num_of_travelers
    origin_city = input("From which city are you flying from?: ")
    is_available_flight = False
    while not is_available_flight:
        destination_city = input("To which city are you flying to?: ")
        departure_date = input("Please enter your departure date (yyyy/mm/dd): ")

        list_of_flights = flight_found(origin_city=origin_city, destination_city=destination_city, departure_date=departure_date,
                        num_of_seats=num_of_passengers)
        if list_of_flights:
            is_available_flight = True

    chosen_flight = choose_flight(list_of_flights)

    return chosen_flight


def add_passenger():
    p_f_name = input("Please enter passenger's first name: ")
#     p_l_name = input("Please enter passenger's last name: ")
#     p_dob = input("Please enter passenger's D.O.B (dd/nn/yyyy): ")
#     p_pass_num = input("Please enter passenger's passport number: ")
#
#     new_passenger = Passenger(first_name=first_name, last_name=last_name, )

def crate_new_order():
    pass


def main():
    print("Hey! Welcome to the new friendly flight tickets reservation site")
    while True:
        is_new = input("Do you have an account? (y/n): ")
        if is_new.lower() == 'n' or is_new.lower() == 'no':
            cur_user = create_new_user()
            break
        elif is_new.lower() == 'y' or is_new.lower() == 'yes':
            cur_user = check_if_user()
            if cur_user:
                break

    print("Let's find the perfect flight for you")
    num_of_travelers = int(input("How many travelers?: "))
    new_flight = search_for_flights(num_of_travelers)

    while True:
        new_order = input("Do you want to open a new order? (y/n): ")
        if new_order.lower() == 'y' or new_order.lower() == 'yes':
            # create_new_order()
            break
        elif is_new.lower() == 'n' or is_new.lower() == 'no':
            print("OK, see you next time")
            break

    return  # Close the main function


if __name__ == "__main__":
    main()
