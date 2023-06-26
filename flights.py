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
        if num_of_seats < seats_avel:
            print("Flight Details:")
            #print(f"Transaction ID: {row[0]}")
            print(f"Flight Date: {row[1]}")
            print(f"Airline Name: {row[3]}")
            print(f"Origin Airport: {row[6]}")
            print(f"Destination Airport: {row[11]}")
            print(f"Departure Time: {row[14][:2] + ':' + row[14][2:]}")
            print(f"Arrival Time: {row[15][:2] + ':' + row[15][2:]}")
            #print(f"Seats Available: {row[-1]}")
            print()

    connection.close()

    if rows:
        return True
    else:
        return False
