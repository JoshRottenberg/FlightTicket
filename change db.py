import sqlite3

# Assuming you have a SQLite connection established
conn = sqlite3.connect("big_data.db")
cur = conn.cursor()

email = "1"
password = "1"

# Execute the INSERT statement
cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))

# Commit the transaction to save the changes
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()
