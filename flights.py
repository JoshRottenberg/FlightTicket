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
    connection.close()

    if rows:
        for row in rows:
            print(row)
        return True
    else:
        return False


