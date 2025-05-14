import mysql.connector
import hashlib  # Para manejar contraseñas encriptadas con SHA256

class DAOBase:
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

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


class DAOUser(DAOBase):
    def validate_user(self, username, password):
        if not self.cursor:
            return None
        # Encriptar la contraseña ingresada
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        query = "SELECT * FROM User WHERE username = %s AND password = %s"
        try:
            self.cursor.execute(query, (username, hashed_password))
            user = self.cursor.fetchone()
            return user  # Devuelve el usuario si las credenciales son correctas
        except mysql.connector.Error as err:
            print(f"Error en la consulta SQL: {err}")
            return None

    def add_user(self, username, password, email):
        if not self.cursor:
            return None
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        query = "INSERT INTO User (username, password, email) VALUES (%s, %s, %s)"
        try:
            self.cursor.execute(query, (username, hashed_password, email))
            self.connection.commit()
            return {"id": self.cursor.lastrowid, "username": username, "email": email}
        except mysql.connector.Error as err:
            print(f"Error al agregar el usuario: {err}")
            return None


class DAOChild(DAOBase):
    def get_all_children(self):
        if not self.cursor:
            return None
        query = "SELECT * FROM Child"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error al obtener los niños: {err}")
            return None

    def add_child(self, name, age, user_id):
        if not self.cursor:
            return None
        query = "INSERT INTO Child (name, age, user_id) VALUES (%s, %s, %s)"
        try:
            self.cursor.execute(query, (name, age, user_id))
            self.connection.commit()
            return {"id": self.cursor.lastrowid, "name": name, "age": age, "user_id": user_id}
        except mysql.connector.Error as err:
            print(f"Error al agregar el niño: {err}")
            return None


class DAOTap(DAOBase):
    def get_all_taps(self):
        if not self.cursor:
            return None
        query = "SELECT * FROM Tap"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error al obtener los Taps: {err}")
            return None

    def add_tap(self, description, child_id):
        if not self.cursor:
            return None
        query = "INSERT INTO Tap (description, child_id) VALUES (%s, %s)"
        try:
            self.cursor.execute(query, (description, child_id))
            self.connection.commit()
            return {"id": self.cursor.lastrowid, "description": description, "child_id": child_id}
        except mysql.connector.Error as err:
            print(f"Error al agregar el Tap: {err}")
            return None


class DAORole(DAOBase):
    def get_all_roles(self):
        if not self.cursor:
            return None
        query = "SELECT * FROM Role"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error al obtener los roles: {err}")
            return None

    def add_role(self, name):
        if not self.cursor:
            return None
        query = "INSERT INTO Role (name) VALUES (%s)"
        try:
            self.cursor.execute(query, (name,))
            self.connection.commit()
            return {"id": self.cursor.lastrowid, "name": name}
        except mysql.connector.Error as err:
            print(f"Error al agregar el rol: {err}")
            return None


class DAOStatus(DAOBase):
    def get_all_statuses(self):
        if not self.cursor:
            return None
        query = "SELECT * FROM Status"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error al obtener los estados: {err}")
            return None

    def add_status(self, name):
        if not self.cursor:
            return None
        query = "INSERT INTO Status (name) VALUES (%s)"
        try:
            self.cursor.execute(query, (name,))
            self.connection.commit()
            return {"id": self.cursor.lastrowid, "name": name}
        except mysql.connector.Error as err:
            print(f"Error al agregar el estado: {err}")
            return None


class DAOTreatment(DAOBase):
    def get_all_treatments(self):
        if not self.cursor:
            return None
        query = "SELECT * FROM Treatment"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error al obtener los tratamientos: {err}")
            return None

    def add_treatment(self, name, description):
        if not self.cursor:
            return None
        query = "INSERT INTO Treatment (name, description) VALUES (%s, %s)"
        try:
            self.cursor.execute(query, (name, description))
            self.connection.commit()
            return {"id": self.cursor.lastrowid, "name": name, "description": description}
        except mysql.connector.Error as err:
            print(f"Error al agregar el tratamiento: {err}")
            return None
        
    def get_treatment_by_id(self, treatment_id):
        if not self.cursor:
            return None
        query = "SELECT * FROM Treatment WHERE id = %s"
        try:
            self.cursor.execute(query, (treatment_id,))
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error al obtener el tratamiento: {err}")
            return None