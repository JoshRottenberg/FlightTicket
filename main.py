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
                        password=new_password)
    # User.users.append(current_user)
    print(User.users)


def check_if_user():
    user_name = input("Please enter your username (Email): ")
    password = input("Please enter your password: ")
    for user in User.users:
        if user_name == user.email and password == user.password:
            current_user = user
            print(f"welcome back {user.first_name}!")
            return False
        if not any(user_name == user.email) or (user_name == user.email and password != user.password):
            print("error!")
            return True


def main():
    print("Hey! Welcome to the new friendly flight tickets reservation site")
    while True:
        is_new = input("do you have an account? (y/n):")
        if is_new.lower() == 'n':
            create_new_user()
            break
        elif is_new.lower() == 'y':
            check_if_user()

    return  # Close the main function


if __name__ == "__main__":
    main()
