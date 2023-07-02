from exeptions import *
from order_management import *
from main_management import *
from user_management import *
from flights_management import *
import sys


def get_cur_user(process):
    while True:
        is_new = input("Do you have an account? (y/n): ")
        if is_new.lower() == 'n' or is_new.lower() == 'no':
            cur_user = process.user_management.create_new_user()
            break
        elif is_new.lower() == 'y' or is_new.lower() == 'yes':
            cur_user = process.user_management.check_if_user()
            if cur_user:
                break
    return cur_user


def get_num_of_travelers():
    while True:
        num_of_travelers = input("How many travelers?: ")
        if is_int(num_of_travelers):
            break
    return int(num_of_travelers)


def get_cur_order(process, cur_user):
    while True:
        is_order = input("Do you want to open a new order? (y/n): ")
        if is_order.lower() == 'y' or is_order.lower() == 'yes':
            cur_order = process.order_management.create_new_order(cur_user.get_person_id())
            break

        elif is_order.lower() == 'n' or is_order.lower() == 'no':
            print("OK, see you next time")
            exit(1)
    return cur_order


def main():
    process = MainManagement()
    print("Hey! Welcome to the new friendly flight tickets reservation site")
    cur_user = get_cur_user(process)

    print("Let's find the perfect flight for you")
    num_of_travelers = get_num_of_travelers()

    cur_flight = process.flights_management.search_for_flights(num_of_travelers)

    cur_order = get_cur_order(process, cur_user)

    total_price = 0
    for passenger in range(1, num_of_travelers + 1):
        print(f"Please enter the details of passenger {passenger}")
        cur_pass = process.order_management.add_passenger()
        cur_ticket = process.order_management.add_ticket(pass_id=cur_pass.get_pass_id(),
                                                         flight_id=cur_flight.flight_code, price=cur_flight.price,
                                                         order_id=cur_order.order_id)
        total_price += int(cur_ticket._price[1:])

    process.order_management.payment(cur_order._total_price)
    process.order_management.update_order(order=cur_order, total_price=total_price, num_of_travelers=num_of_travelers)
    print(f"\nCongratulations {cur_user._first_name}")
    process.order_management.show_order(cur_flight._origin, cur_flight._destination, cur_order._order_id,
                                        cur_order._num_of_tickets, cur_order._total_price)
    print(f"\nHave a nice flight!")
    return  # Close the main function


if __name__ == "__main__":
    main()
