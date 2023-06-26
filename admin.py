from user import User
import sqlite3


class Admin(User):
    def __init__(self, id, name, last_name, phone_num, email, password):
        super().__init__(id, name, last_name, phone_num, email, password)

    def delete_user(user_id):
        # Connect to the database
        conn = sqlite3.connect('big_data.db')
        cursor = conn.cursor()

        # Execute the DELETE statement
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
