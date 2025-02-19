from flask import Flask, request, jsonify

class User:
    def __init__(self, id, username, password, email=""):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

#    def __str__(self):
#        return "Id:" + str(self.id) + " Username:" + self.username

listUsers= [
    User(1,"usuari1", "12345", "prova@gmail.com"),
    User(2,"user2", "123", "user2@proven.cat"),
    User(3,"admin","12","admin@proven.cat"),
    User(4,"admin2","12"),
    User(5,"Dariella","2006","dariella@gmail.com")
]

class DAOUsers:
    def __init__(self):
        self.users=listUsers
    
    def getUserByUsername(self,username):
        for u in self.users:
            if u.username == username:
                return u.__dict__
        return None

daoUser = DAOUsers()

u=daoUser.getUserByUsername("usuari1")
if(u):
    print(u)
else:
    print("No trobat")

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

@app.route('/prototip1/getuser', methods=['GET'])
def get_user():
    username = request.args.get('username', default="", type=str)
    print("Username received: " + username)
    
    if not username:
        return jsonify({"ERROR": "Mal Request: 'username' parametro es requerido"}), 400

    user = daoUser.getUserByUsername(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"ERROR": "usuario con el usernam '" + username + "' no encontrado"}), 404


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
    
    return jsonify(daoUser.getUserByUsername("usuari1","prova@gmail.com"))



if __name__ == '__main__':
     app.run(debug=True,host="0.0.0.0",port="10050")

