from user import User
from admin import Admin
from passenger import Passenger
from ticket import Ticket
from order import Order
from flight import Flight
from flights import Flights


def create_new_user():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    phone_num = input("Please enter your phone number: ")
    email = input("Please enter your Email address: ")
    new_password = input("What is your password: ")
    current_user = User(first_name=first_name, last_name=last_name, phone_num=phone_num, email=email,
                        password=new_password, is_signed_in=True)


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
        if is_new.lower() == 'n':
            create_new_user()
            break
        elif is_new.lower() == 'y':
            if check_if_user():
                break


    return  # Close the main function


if __name__ == "__main__":
    main()