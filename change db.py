import sqlite3
import random

# Connect to the SQLite database
connection = sqlite3.connect("flights_base2.db")
cursor = connection.cursor()

# Add a new column "price" to the "Flights" table
cursor.execute("ALTER TABLE Flights ADD COLUMN price TEXT")

# Update each row with a random price between $150 and $800
query = "UPDATE Flights SET price = ? WHERE TRANSACTIONID = ?"
cursor.execute("SELECT TRANSACTIONID FROM Flights")
transaction_ids = cursor.fetchall()
for transaction_id in transaction_ids:
    price = "$" + str(random.randint(150, 800))
    cursor.execute(query, (price, transaction_id[0]))

# Commit the changes and close the connection
connection.commit()
connection.close()
