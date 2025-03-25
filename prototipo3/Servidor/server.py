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
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end

class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

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

# Clases DAO
class UserDAO:
    def __init__(self):
        self.users = users

    def get_user_by_username_password(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

class ChildDAO:
    def __init__(self):
        self.children = children

    def get_children_by_user_id(self, user_id):
        child_ids = [rel["child_id"] for rel in relation_user_child if rel["user_id"] == user_id]
        return [child for child in self.children if child.id in child_ids]

@app.route('/prototipo2', methods=['POST'])
def prototipo2():
    data = request.get_json()

    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Nombre de usuario o contraseña faltantes"}), 400

    username = data["username"]
    password = data["password"]

    user_dao = UserDAO()
    user = user_dao.get_user_by_username_password(username, password)

    if user:
        child_dao = ChildDAO()
        children = child_dao.get_children_by_user_id(user.id)

       
        child_ids = [child.id for child in children]
        child_taps = [tap.__dict__ for tap in taps if tap.child_id in child_ids]

        return jsonify({
            "message": "Login exitoso",
            "user_info": user.__dict__,
            "children": [child.__dict__ for child in children],
            "taps": child_taps  
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