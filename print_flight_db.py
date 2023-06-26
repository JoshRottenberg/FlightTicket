import sqlite3

# Connect to the database
conn = sqlite3.connect('flights_base2.db')
cursor = conn.cursor()

# Execute the SELECT query to retrieve the TRANSACTIONID column
cursor.execute("SELECT * FROM Flights LIMIT 10")
rows = cursor.fetchall()

# Print the TRANSACTIONID for each row
for row in rows:
    print(row)

# Close the connection
conn.close()
