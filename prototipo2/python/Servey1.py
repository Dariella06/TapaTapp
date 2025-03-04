import DatosServidor as dades
from DatosServidor import User, Child, Tap, Status, Role, Treatment
from flask import Flask, jsonify, request

app = Flask(__name__)

class UserDAO:
    def __init__(self):
        self.users = dades.users

    def get_all_users(self):
        return [user.__dict__ for user in self.users]

    def get_user_by_username_password(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user.__dict__
        return None

class ChildDAO:
    def __init__(self):
        self.children = dades.children

    def get_all_children(self):
        children_dicts = []
        for child in self.children:
            children_dicts.append(child.__dict__)
        return children_dicts

    def get_children_by_user_id(self, user_id):
        child_ids = []
        for rel in dades.relation_user_child:
            if rel["user_id"] == user_id:
                child_ids.append(rel["child_id"])
        children_dicts = []
        for child in self.children:
            if child.id in child_ids:
                children_dicts.append(child.__dict__)
        return children_dicts

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
        children = child_dao.get_children_by_user_id(user['id'])

        return jsonify({"message": "Login exitoso", "user_info": user, "children": children}), 200
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10050)
