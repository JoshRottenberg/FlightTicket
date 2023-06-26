# import sqlite3
#
# # Connect to the database
# conn = sqlite3.connect('flights_base2.db')
# cursor = conn.cursor()
#
# # Execute the SELECT query to retrieve the TRANSACTIONID column
# cursor.execute("SELECT TRANSACTIONID FROM Flights LIMIT 150")
# rows = cursor.fetchall()
#
# # Print the TRANSACTIONID for each row
# for row in rows:
#     transaction_id = row[0]
#     print(transaction_id)
#
# # Close the connection
# conn.close()
import sqlite3

# Connect to the database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Execute the SELECT query to retrieve all TRANSACTIONID values
cursor.execute("SELECT TRANSACTIONID FROM Flights")
rows = cursor.fetchall()

# Create a set to store unique TRANSACTIONID values
unique_ids = set()

# Iterate over the rows and check for duplicates
for row in rows:
    transaction_id = row[0]
    if transaction_id in unique_ids:
        print(f"Duplicate TRANSACTIONID found: {transaction_id}")
    else:
        unique_ids.add(transaction_id)

# If no duplicates found, print a success message
if len(unique_ids) == len(rows):
    print("All TRANSACTIONID values are unique.")

# Close the connection
conn.close()
