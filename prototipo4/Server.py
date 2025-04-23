from flask import Flask, request, jsonify
from ServerDAOS import DAOUser 
import hashlib  # Para manejar contraseñas encriptadas con SHA256

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  
    username = data.get("username")  
    password = data.get("password")  

    if not username or not password:
        return jsonify({"error": "Nombre de usuario o contraseña faltantes"}), 400

    user_dao = DAOUser()  
    user = user_dao.validate_user(username, password)


    if user:
        return jsonify({
            "message": "Login exitoso",
            "user_info": user
        }), 200
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

if __name__ == "__main__":
    app.run(debug=True)