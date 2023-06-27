import sqlite3
from flight import Flight


class FlightManagement:

    def search_for_flights(self, num_of_travelers):
        num_of_passengers = num_of_travelers
        origin_city = input("From which city are you flying from?: ")
        is_available_flight = False
        while not is_available_flight:
            destination_city = input("To which city are you flying to?: ")
            departure_date = input("Please enter your departure date (yyyy/mm/dd): ")
            list_of_flights = FlightManagement.flight_found(origin_city=origin_city, destination_city=destination_city,
                                           departure_date=departure_date,
                                           num_of_seats=num_of_passengers)
            if list_of_flights:
                is_available_flight = True

        chosen_flight = FlightManagement.choose_flight(list_of_flights)

        return chosen_flight

    def flight_found(self, origin_city, destination_city, departure_date, num_of_seats):
        connection = sqlite3.connect("flights_base2.db")
        cursor = connection.cursor()

        table_name = "Flights"

        # User input for search criteria
        flight_date = departure_date
        origin_city = origin_city
        dest_city = destination_city

        # Select rows that match the search criteria
        query = f"SELECT * FROM {table_name} WHERE FLIGHTDATE = ? AND ORIGINCITYNAME = ? AND DESTCITYNAME = ?"
        cursor.execute(query, (flight_date, origin_city, dest_city))
        rows = cursor.fetchall()

        for row in rows:
            seats_avel = row[16]
            if num_of_seats > seats_avel:
                print("There are not enough available seats in any of the flights")
                return False

        if rows:
            num_of_flights = len(rows)
            list_of_codes = []
            print()
            print(f"We have found {num_of_flights} flights for you")
            print()
            i = 0
            for row in rows:
                if num_of_seats < seats_avel:
                    i += 1
                    print(f"Flight number {i}")
                    print("Flight Details:")
                    print(f"Flight Date: {row[1]}")
                    print(f"Airline Name: {row[3]}")
                    print(f"Origin Airport: {row[6]}")
                    print(f"Destination Airport: {row[10]}")
                    print(f"Departure Time: {row[13][:-2] + ':' + row[13][-2:]}")
                    print(f"Arrival Time: {row[14][:-2] + ':' + row[14][-2:]}")
                    print(f"The price for this flight is: {row[17]}")
                    print()
                    print(
                        "---------------------------------------------------------------------------------------------------")
                    trans_code_id = (i, row[0])
                    list_of_codes.append(trans_code_id)

        connection.close()

        if rows:
            return list_of_codes
        else:
            print("We couldn't find a flight that matches your preferences. Let's try again")
            return False

    def choose_flight(self, list_of_flights):
        chosen_i = int(input("Choose your preferred flight: "))  # add exeption
        chosen_code = list[chosen_i - 1][1]

        conn = sqlite3.connect('flights_base2.db')
        cursor = conn.cursor()
        transaction_id = f'{chosen_code}'
        cursor.execute("SELECT * FROM Flights WHERE TRANSACTIONID = ?", (transaction_id,))
        row = cursor.fetchone()

        if row:
            chosen_flight = row
            new_flight = Flight(flight_code=row[0], date=row[1], company=row[3], distance=row[15])
            return new_flight
        else:
            print("there is a problem")
