import sqlite3

# Create a connection to the database file
conn = sqlite3.connect('big_data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the "users" table with the desired columns
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passengers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        date_of_birth DATE,
        passport TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
