from flask import Flask, request, jsonify
import DatosServidor as data
from DatosServidor import User, Child, Treatment, Status, VerificationCode

class UserDAO:
    def __init__(self, users):
        self.users = users

    def get_all_users(self):
        return [user.__dict__ for user in self.users]

    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user.__dict__
        return None
    
    def get_user_by_username_email_password(self, users, email, password):
        for user in self.users:
            if user.users == users and user.email == email and user.password == password:
                return user.__dict__
        return None

class ChildDAO:
    def __init__(self, children, relationships):
        self.children = children
        self.relationships = relationships

    def get_all_children(self):
        return [child.__dict__ for child in self.children]

    def get_children_by_user(self, user_id):
        ids = [rel["child_id"] for rel in self.relationships if rel["user_id"] == user_id]
        return [child.__dict__ for child in self.children if child.id in ids]

class TreatmentDAO:
    def __init__(self, treatments):
        self.treatments = treatments

    def get_all_treatments(self):
        return [treatment.__dict__ for treatment in self.treatments]

class StatusDAO:
    def __init__(self, statuses):
        self.statuses = statuses

    def get_all_statuses(self):
        return [status.__dict__ for status in self.statuses]

class VerificationCodeDAO:
    def __init__(self, codes):
        self.codes = codes

    def get_code_by_user(self, user_id):
        for code in self.codes:
            if code.user_id == user_id:
                return code.__dict__
        return None

user_dao = UserDAO()

app = Flask(__name__)

@app.route('/prototype2/users', methods=['GET'])
def get_users():
    return jsonify(user_dao.get_all_users())

@app.route('/prototype2/getuser', methods=['GET'])
def get_user_by_username_email_password():
    username = request.args.get('username', default="", type=str)
    email = request.args.get('email', default="", type=str)
    password = request.args.get('password', default="", type=str)

    if not username or not email or not password:
        return jsonify({"error": "The parameters 'username', 'email', or 'password' are required"}), 400

    user = user_dao.get_user_by_username_email_password(username, email, password)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User with the provided username, email, and password not found"}), 404

if __name__ == '__main__':
     app.run(debug=True,host="0.0.0.0",port=10050)
