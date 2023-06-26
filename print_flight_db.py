import sqlite3

# Connect to the database
conn = sqlite3.connect('flights_base2.db')
cursor = conn.cursor()

# Execute the SELECT query to retrieve the TRANSACTIONID column
cursor.execute("SELECT price FROM Flights LIMIT 150")
rows = cursor.fetchall()

# Print the TRANSACTIONID for each row
for row in rows:
    transaction_id = row[0]
    print(transaction_id)

# Close the connection
conn.close()
