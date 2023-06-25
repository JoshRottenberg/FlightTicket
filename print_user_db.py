import sqlite3

# Connect to the database
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Execute a SELECT query to retrieve all rows from the "users" table
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Print the column headers
print("ID | First Name | Last Name | Phone Number | Email | Password | Is Signed Up")

# Iterate over the rows and print the data
for row in rows:
    print(row)

# Close the connection
conn.close()
