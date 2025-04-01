from flask import Flask, jsonify, request

app = Flask(__name__)


TOKEN_VALID = "secret123"

# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return f"{self.username}:{self.password}:{self.email}"

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

# Clase para manejar usuarios
class UserDAO:
    def __init__(self):
        self.users = users

    def get_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def add_user(self, username, password, email):
        new_id = len(self.users) + 1
        new_user = User(new_id, username, password, email)
        self.users.append(new_user)
        return new_user

# Ruta para registrar un nuevo usuario
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not username or not password or not email:
        return jsonify({"error": "Faltan datos para el registro"}), 400

    user_dao = UserDAO()
    if user_dao.get_user(username, password):
        return jsonify({"error": "El usuario ya existe"}), 400

    new_user = user_dao.add_user(username, password, email)
    return jsonify({"message": "Usuario registrado exitosamente", "user_info": new_user.__dict__}), 201

# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Nombre de usuario o contraseña faltantes"}), 400

    user_dao = UserDAO()
    user = user_dao.get_user(username, password)

    if user:
        return jsonify({
            "message": "Login exitoso",
            "user_info": user.__dict__,
            "children": [child.__dict__ for child in children],  # Todos los niños
            "taps": [tap.__dict__ for tap in taps]  # Todos los Taps
        }), 200
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)