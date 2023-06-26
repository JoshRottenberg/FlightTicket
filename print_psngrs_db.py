import sqlite3

try:
    # Connect to the database
    conn = sqlite3.connect('psngrs_data.db')
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve all rows from the "users" table
    cursor.execute('SELECT * FROM passengers')
    rows = cursor.fetchall()

    # Print the column headers
    print("ID | FIRST NAME  |   LAST NAME  | DOB   |  PASSPORT ")

    # Iterate over the rows and print the data
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("Error accessing the database:", e)

finally:
    # Close the connection
    if conn:
        conn.close()

