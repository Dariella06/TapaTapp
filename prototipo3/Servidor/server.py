from flask import Flask, jsonify, request

app = Flask(__name__)

# Clases de datos
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

class Child:
    def __init__(self, id, name, sleep_average, treatment_id, time):
        self.id = id
        self.name = name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

# Datos de ejemplo
users = [
    User(id=1, username="mare", password="12345", email="prova@gmail.com"),
    User(id=2, username="pare", password="123", email="prova2@gmail.com")
]

children = [
    Child(id=1, name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, name="Jaco Child", sleep_average=10, treatment_id=2, time=6)
]

# Clases DAO
class UserDAO:
    def __init__(self):
        self.users = users

    def get_user_by_username_password(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def add_user(self, username, password, email):
        new_id = len(self.users) + 1
        new_user = User(id=new_id, username=username, password=password, email=email)
        self.users.append(new_user)
        return new_user

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not username or not password or not email:
        return jsonify({"error": "Faltan datos para el registro"}), 400

    user_dao = UserDAO()
    existing_user = user_dao.get_user_by_username_password(username, password)

    if existing_user:
        return jsonify({"error": "El usuario ya existe"}), 400

    new_user = user_dao.add_user(username, password, email)
    return jsonify({"message": "Usuario registrado exitosamente", "user_info": new_user.__dict__}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Nombre de usuario o contraseña faltantes"}), 400

    user_dao = UserDAO()
    user = user_dao.get_user_by_username_password(username, password)

    if user:
        return jsonify({
            "message": "Login exitoso",
            "user_info": user.__dict__,
            "children": [{"id": child.id, "child_name": child.name, "sleep_average": child.sleep_average, "treatment_id": child.treatment_id, "time": child.time} for child in children],  # Información completa de los niños
            "taps": [{"id": 1, "child_id": 1, "init": "2024-12-18T19:42:43", "end": "2024-12-18T20:42:43"},
                      {"id": 2, "child_id": 2, "init": "2024-12-18T21:42:43", "end": "2024-12-18T22:42:43"}]  # Ejemplo de taps
        }), 200
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10050)


# TIENE QUE DEVOLVER UN TOKEN Y METODO POST
# Podemos poner un usuario y un codigo y tal
# BUSCAR:
# 256 chars
# Respuesta json
# Hay que autenticar tipo user y password
# enviar el token a un header
# 