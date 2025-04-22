import mysql.connector

class DAOUser:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="Tapatapp"
            )
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None
            self.cursor = None

    def get_all_users(self):
        if not self.cursor:
            return None
        query = "SELECT * FROM User"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall() 
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    dao = DAOUser()
    users = dao.get_all_users()
    if users:
        for user in users:
            print(user)
    dao.close_connection()