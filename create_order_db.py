import sqlite3

# Create a connection to the database file
conn = sqlite3.connect('big_data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the "users" table with the desired columns
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