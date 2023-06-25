from user import User
from admin import Admin
from passenger import Passenger
from ticket import Ticket
from order import Order
from flight import Flight
from flights import Flights
from exeptions import *


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
    with open('users_instances.txt', 'r') as file:
        for line in file:
            words = line.strip().split(',')
            if words[7] == user_name and words[9] == password:
                print(f"welcome back {words[1]}!")
                return True
        print("one of the details isn't correct, please retry")
        return False


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

    return  # Close the main function


if __name__ == "__main__":
    main()
