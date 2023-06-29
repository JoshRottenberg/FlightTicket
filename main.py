from exeptions import *
from order_management import *
from main_management import *
from user_management import *
from flights_management import *
import sys


def main():
    process = MainManagement()
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

    not_status = False
    while not not_status:
        num_of_travelers = input("How many travelers?: ")
        not_status = is_int(num_of_travelers)
    num_of_travelers = int(num_of_travelers)
    cur_flight = process.flights_management.search_for_flights(num_of_travelers)

    while True:
        is_order = input("Do you want to open a new order? (y/n): ")

        if is_order.lower() == 'y' or is_order.lower() == 'yes':
            cur_order = process.order_management.create_new_order(cur_user.get_user_id())
            break

        elif is_order.lower() == 'n' or is_order.lower() == 'no':
            print("OK, see you next time")
            exit(1)

    total_price = 0
    for passenger in range(1, num_of_travelers + 1):
        print(f"Please enter the details of passenger {passenger}")
        cur_pass = process.order_management.add_passenger()
        cur_ticket = process.order_management.add_ticket(pass_id=cur_pass.get_pass_id(),
                                                         flight_id=cur_flight.flight_code, price=cur_flight.price,
                                                         order_id=cur_order.order_id)
        total_price += int(cur_ticket._price[1:])

    print()
    print(f"Congratulations {cur_user._first_name}, you are flying to {cur_flight._destination}. Your order has been confirmed")
    print(f"Your order id is: {cur_order._order_id}")
    print(f"You ordered {cur_order._num_of_tickets} tickets")
    print(f"The total price for the order is: {cur_order._total_price}")
    print(f"Have a nice flight!")

    process.order_management.payment(cur_order._total_price)
    process.order_management.update_order(order=cur_order, total_price=total_price, num_of_travelers=num_of_travelers)
    return  # Close the main function


if __name__ == "__main__":
    main()
