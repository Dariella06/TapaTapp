from flask import Flask, request, jsonify

class User:
    def __init__(self, id, username, password, email=""):
        self.id=id
        self.username=username
        self.password=password
        self.email=email


#    def __str__(self):
#        return "Id:" + str(self.id) + " Username:" + self.username

users= [
    User(1,"usuari1", "12345", "prova@gmail.com"),
    User(2,"user2", "123", "user2@proven.cat"),
    User(3,"admin","12","admin@proven.cat"),
    User(4,"admin2","12"),
    User(5,"Dariella","2006","dariella@gmail.com")
]

class UserDAO:
    def __init__(self):
        self.users = users

    def get_all_users(self):
        result = []
        for user in self.users:
            result.append(user.__dict__)
        return result

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None
    
    def get_user_by_username_email_password(self, username, email, password):
        for user in self.users:
            if user.username == username and user.email == email and user.password == password:
                return user.__dict__
        return None

# Inicialitzar DAOs
user_dao = UserDAO()

#u=daoUser.getUserByUsername("usuari1")
#if(u):
#    print(u)
#else:
#    print("No trobat")

app = Flask(__name__)

#ESTO LO COMENTE PORQUE POR AHORA NO NOS SIRVE'''
#@app.route('/proto1/getdata/<string:param1>', methods=['GET'])
#def getData(param1):
#    return "Aquest és el servei /proto1/getdata/ amb parametre=" + param1

#@app.route('/hello', methods=['GET'])
#def hello():
#    prova=request.args.get('prova')
#    if(prova):
#        return "Hello World Param=" + prova
#    return "Hello World" ESTO ES UN COMENTARIO PARA QUE NO INTERFIERA

@app.route('/tapatapp/getuser', methods=['GET'])
def getUser():
    n = str(request.args.get('name'))
    email = str(request.args.get('mail'))
    return "Hello Word!!" + " Nom:" + n + " Email:" + email

#@app.route('/prototip/getuser/<string:username>', methods=['GET'])
#def prototipGetuser(username):
#    return "Prototip 1 - User:" + username 

@app.route('/prototip1/users', methods=['GET'])
def get_users():
    return jsonify(user_dao.get_all_users())

@app.route('/prototip1/getuser', methods=['GET'])
def get_user_by_username_email_password():
    username = request.args.get('username', default="", type=str)
    email = request.args.get('email', default="", type=str)
    password = request.args.get('password', default="", type=str)

    if not username or not email or not password:
        return jsonify({"error": "No encontrado los parametetros: 'username', 'email', or 'password' Son requeridos"}), 400

    user = user_dao.get_user_by_username_email_password(username, email, password)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Usuario con nombre de usuario, correo electrónico y contraseña proporcionados no encontrados"}), 404


#@app.route('/hello',methods=['GET'])
#def hello():
#    user = str(request.args.get('username'))
#    if not user:
#        return jsonify(daoUser.getUserByUsername("Error, l'usuari no es correcte"), 404) 
#    if not user:
#        return jsonify(daoUser.getUserByUsername("Error, Falta una data"), 404) 
#    return jsonify(daoUser.getUserByUsername("usuari1"))

@app.route('/hello', methods=['GET'])
def hello():
    user = str(request.args.get('username'))
    
    if not user:
        return jsonify({"error": "Error, l'usuari no es correcte"}), 404
    
    if not request.args.get('email'):
        return jsonify({"error": "Error, Falta una data"}), 400
    
    return jsonify(user_dao.get_user_by_username("usuari1","prova@gmail.com"))


if __name__ == '__main__':
     app.run(debug=True,host="0.0.0.0",port=10050)

