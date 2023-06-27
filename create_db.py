import sqlite3
#
# # Create a connection to the database file
# conn = sqlite3.connect('big_data.db')
#
# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()
#
# # Create the "users" table with the desired columns
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT,
#         last_name TEXT,
#         phone_num TEXT,
#         email TEXT,
#         password TEXT,
#         is_signed_up BOOL
#     )
# ''')
#
# # Commit the changes and close the connection
# conn.commit()
# conn.close()
#
#
#
#
# Create a connection to the database file
conn = sqlite3.connect('big_data.db')
#
# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the "orders" table with the desired columns
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id UNSIGNED,
        num_of_tickets UNSIGNED,
        total_price UNSIGNED
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

#
#
#
# # Create a connection to the database file
# conn = sqlite3.connect('big_data.db')
#
# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()
#
# # Create the "passengers" table with the desired columns
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS passengers (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT,
#         last_name TEXT,
#         date_of_birth DATE,
#         passport TEXT
#     )
# ''')
#
# # Commit the changes and close the connection
# conn.commit()
# conn.close()
#
#
# # Create a connection to the database file
# conn = sqlite3.connect('big_data.db')
#
# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()
#
# # Create the "tickets" table with the desired columns
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS tickets (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         passenger_id UNSIGNED,
#         flight_id TEXT,
#         seat TEXT,
#         seat_class TEXT,
#         price TEXT
#     )
# ''')
#
# # Commit the changes and close the connection
# conn.commit()
# conn.close()