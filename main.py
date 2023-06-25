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
        phone_num = input("Please enter your phone number: ")
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
                        password=new_password, is_signed_up=True)


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
        return True
    else:
        # User not found in the database or invalid credentials
        print("One of the details is incorrect. Please retry.")
        return False


def search_for_flights():
    origin_state = input("From which country are you flying from?: ")
    origin_city = input("From which city are you flying from?: ")
    is_available_flight = False
    while not is_available_flight:
        destination_state = input("To which country are you flying to?: ")
        destination_city = input("To which city are you flying to?: ")
        departure_date = input("please enter your departure date:  (yyyy/mm/dd)")
        num_of_passengers = int(input("how many travelers?: "))
        if flight_found(origin_city=origin_city,destination_city=destination_city,departure_date=departure_date,num_of_seats=num_of_passengers):
            is_available_flight = True
    return num_of_passengers


def main():
    print("Hey! Welcome to the new friendly flight tickets reservation site")
    while True:
        is_new = input("do you have an account? (y/n):")
        if is_new.lower() == 'n' or is_new.lower() == 'no':
            create_new_user()
            break
        elif is_new.lower() == 'y' or is_new.lower() == 'yes':
            if check_if_user():
                break

    # print("Let's find the perfect flight for you")
    # search_for_flights()
    # num_of_travelers = search_for_flights()
    # print("Congratulations!! you have find the perfect flight for you!!")
    # while True:
    #     new_order = input("do you want to open  a new order? (y/n):")
    #     if new_order.lower() == 'y' or new_order.lower() == 'yes':
    #         create_new_order()
    #         break
    #     elif is_new.lower() == 'y' or is_new.lower() == 'yes':
    #         if check_if_user():
    #             break





    return  # Close the main function


if __name__ == "__main__":
    main()
