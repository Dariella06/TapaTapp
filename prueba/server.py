# server.py
import jwt
import datetime
from flask import Flask, jsonify, request
from ServerDatos import User, Child, Tap, Role, Status, Treatment 
from ServerDao import UserDAO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DariellaCamille'

# Ruta para registrar un nuevo usuario
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not username or not password or not email:
        return jsonify({"error": "Faltan datos"}), 400

    user_dao = UserDAO()
    existing_user = user_dao.get_user(username, password)

    if existing_user:
        return jsonify({"error": "El usuario ya existe"}), 400

    new_user = user_dao.add_user(username, password, email)
    return jsonify({"message": "Usuario registrado exitosamente", "user_info": new_user.__dict__}), 201

# Ruta para validar token y obtener información del usuario autenticado
@app.route('/validate_token', methods=['POST'])
def validate_token():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"error": "Token no proporcionado"}), 400

    try:
        # Decodificar el token usando la clave secreta
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        user_id = decoded_token['user_id']

        # Buscar el usuario por ID
        user_dao = UserDAO()
        user = next((user for user in user_dao.users if user.id == user_id), None)

        if user:
            return jsonify({
                "message": "Sesión válida",
                "user_info": user.__dict__
            }), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 401

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "El token ha expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token inválido"}), 401

# Ruta de login donde generamos un token JWT
# Ruta de login donde generamos un token JWT
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
        # Crear un token JWT
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        # Obtener la lista de niños y TAPS asociados al usuario
        children = []  # Aquí deberías obtener los niños asociados al usuario
        taps = []      # Aquí deberías obtener los TAPS asociados al usuario

        return jsonify({
            "message": "Login exitoso",
            "user_info": user.__dict__,
            "token": token,
            "children": children,  # Asegúrate de que esta lista esté poblada
            "taps": taps           # Asegúrate de que esta lista esté poblada
        }), 200
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401
    
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)