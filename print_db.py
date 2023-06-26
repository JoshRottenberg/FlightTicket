import sqlite3
print("users table")
print()
try:
    # Connect to the database
    conn = sqlite3.connect('big_data.db')
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve all rows from the "users" table
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    # Print the column headers
    print("ID | First Name | Last Name | Phone Number    | Email |        Password ")

    # Iterate over the rows and print the data
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("Error accessing the database:", e)

finally:
    # Close the connection
    if conn:
        conn.close()
print()
print("----------------------------------------------")
# print()
# print("flights table")
#
# # Connect to the database
# conn = sqlite3.connect('flights_base2.db')
# cursor = conn.cursor()
#
# # Execute the SELECT query to retrieve the TRANSACTIONID column
# cursor.execute("SELECT * FROM Flights LIMIT 10")
# rows = cursor.fetchall()
#
# # Print the TRANSACTIONID for each row
# for row in rows:
#     print(row)
#
# # Close the connection
# conn.close()
#print()
# print("----------------------------------------------")

print()
print("orders table")
print()
try:
    # Connect to the database
    conn = sqlite3.connect('big_data.db')
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
print()
print("----------------------------------------------")

print()
print("passengers table")
print()
try:
    # Connect to the database
    conn = sqlite3.connect('big_data.db')
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

