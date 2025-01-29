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

'''u=daoUser.getUserByUsername("usuari1ewrwe")
if(u):
    print(u)
else:
    print("No trobat")'''

print(daoUser.getUserByUsername("usuari1"))

app = Flask(__name__)

@app.route('/hello',methods=['GET'])
def hello():
    user = str(request.args.get('username'))
    return jsonify(daoUser.getUserByUsername("usuari1"))

if __name__ == '__main__':
     app.run(debug=True,host="0.0.0.0",port="10050")