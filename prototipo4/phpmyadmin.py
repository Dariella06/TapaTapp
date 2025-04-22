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

    def validate_user(self, username, password):
        if not self.cursor:
            return None
        query = "SELECT * FROM User WHERE username = %s AND password = %s"
        try:
            self.cursor.execute(query, (username, password))
            user = self.cursor.fetchone()
            if user:
                return user  # Devuelve el usuario si las credenciales son correctas
            else:
                return None  # Devuelve None si las credenciales no coinciden
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            
#NO BORRAR(SOY IMBECIL Y SE ME OLVIDA LO QUE HICE)
if __name__ == "__main__":
    dao = DAOUser()
    
    # Simulación de login
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    user = dao.validate_user(username, password)
    if user:
        print("Login exitoso. Bienvenido:")
        print(user)
    else:
        print("Credenciales incorrectas. Inténtelo de nuevo.")
    
    dao.close_connection()