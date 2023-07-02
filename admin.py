from person import Person
import sqlite3


class Admin(Person):

    def delete_user(self, user_id):
        # Connect to the database
        conn = sqlite3.connect('big_data.db')
        cursor = conn.cursor()

        # Execute the DELETE statement
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
