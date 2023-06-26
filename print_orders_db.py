import sqlite3

try:
    # Connect to the database
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve all rows from the "users" table
    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()

    # Print the column headers
    print("ID | USER ID  |   NUM_OF_TICKETS  | TOTAL PRICE ")

    # Iterate over the rows and print the data
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("Error accessing the database:", e)

finally:
    # Close the connection
    if conn:
        conn.close()
