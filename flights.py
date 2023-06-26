import sqlite3


def flight_found(origin_city, destination_city, departure_date, num_of_seats):
    connection = sqlite3.connect(r"C:\Users\User\PycharmProjects\pythonProject12\flights_base2.db")
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
        seats_avel = row[-1]
        if num_of_seats > seats_avel:
            print("There are not enough available seats in any of the flights")
            return False


    if rows:
        num_of_flights = len(rows)
        print(f" We have found {num_of_flights} flights for you")
        i = 0
        for row in rows:
            if num_of_seats < seats_avel:
                i += 1
                print(f"Flight number {i}")
                print("Flight Details:")
                #print(f"Transaction ID: {row[0]}")
                print(f"Flight Date: {row[1]}")
                print(f"Airline Name: {row[3]}")
                print(f"Origin Airport: {row[6]}")
                print(f"Destination Airport: {row[10]}")
                print(f"Departure Time: {row[13][:-2] + ':' + row[13][-2:]}")
                print(f"Arrival Time: {row[14][:-2] + ':' + row[14][-2:]}")
                #print(f"Seats Available: {row[-1]}")
                print()

    connection.close()

    if rows:
        return True
    else:
        print("We couldn't find a flight that matches your preferences. Let's try again")
        return False
