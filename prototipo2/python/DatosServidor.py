import requests

# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email

# Clase Child
class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

# Clase Tap
class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end

# Clase Status
class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Clase Role
class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

# Clase Treatment
class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Datos de ejemplo
users = [
    User(id=1, username="mare", password="12345", email="prova@gmail.com"),
    User(id=2, username="pare", password="123", email="prova2@gmail.com")
]

children = [
    Child(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6)
]

taps = [
    Tap(id=1, child_id=1, status_id=1, user_id=1, init="2024-12-18T19:42:43", end="2024-12-18T20:42:43"),
    Tap(id=2, child_id=2, status_id=2, user_id=2, init="2024-12-18T21:42:43", end="2024-12-18T22:42:43")
]

relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 1},
    {"user_id": 1, "child_id": 2, "rol_id": 1},
    {"user_id": 1, "child_id": 1, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 1},
    {"user_id": 2, "child_id": 2, "rol_id": 2}
]

roles = [
    Role(id=1, type_rol='Admin'),
    Role(id=2, type_rol='Tutor Mare Pare'),
    Role(id=3, type_rol='Cuidador'),
    Role(id=4, type_rol='Seguiment')
]

statuses = [
    Status(id=1, name="sleep"),
    Status(id=2, name="awake"),
    Status(id=3, name="yes_eyepatch"),
    Status(id=4, name="no_eyepatch")
]

treatments = [
    Treatment(id=1, name='Hour'),
    Treatment(id=2, name='percentage')
]

# Función para autenticar al usuario a través del servidor Flask
def authenticate_user(username, password):
    response = requests.post('http://localhost:10050/prototipo2', json={"username": username, "password": password})
    return response

# Función para mostrar la información del usuario
def show_user_info(user):
    print(f"Nombre de 👤: {user['username']}")
    print(f"Correo 💌: {user['email']}")
    print(f"Contraseña 🔑: {user['password']}")

# Función para listar los niños
def list_children(children):
    print("Lista de niños 👶:")
    for child in children:
        print(f"ID: {child['id']}, Nombre: {child['child_name']}, Promedio de sueño: {child['sleep_average']}, ID de tratamiento: {child['treatment_id']}, Tiempo: {child['time']}")
        

# Función principal
def main():
    print(" ")
    username = input("Introduce tu nombre de 👤: ")
    password = input("🙊 Introduce tu password 🙊: ")
    
    response = authenticate_user(username, password)
    
    if response.status_code == 200:
        data = response.json()
        print(" ")
        print(f"💖 Bienvenido💖, {data['user_info']['username']}!")
        print("Elige una de las opciones que tenemos para que puedas ver la funcionalidad del TapaTapp💖")
        print(" ")

        while True:
            print("Selecciona una opción:")
            print("1. ℹℹ User info")
            print("2. 👶 List Child")
            print("3. 💨 Salir")
            
            option = input("Selecciona una opción: ")
            
            if option == "1":
                print(" ")
                show_user_info(data['user_info'])
                print(" ")
            elif option == "2":
                print(" ")
                list_children(data['children'])
                print(" ")
            elif option == "3":
                print(" ")
                print("Espero que vuelvas pronto 😘💖")
                print("Saliendo del programa...")
                break
            else:
                print(" ")
                print("Opción no válida.")
                print(" ")
    else:
        print("Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    main()