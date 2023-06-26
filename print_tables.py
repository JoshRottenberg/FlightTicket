import sqlite3

# Connect to the database
connection = sqlite3.connect("big_data.db")
cursor = connection.cursor()

# Fetch the table names from the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

# Print the table names
for table in tables:
    print(table[0])

# Close the database connection
connection.close()