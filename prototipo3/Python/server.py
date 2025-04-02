import jwt  # Esta es la librería JWT, que se usa para crear y validar tokens.
import datetime  # Esta librería se utiliza para manejar fechas y tiempos.
from flask import Flask, jsonify, request  # Se importan Flask y funciones auxiliares para crear la aplicación y gestionar peticiones HTTP.
from ServerDatos import User, Child, Tap, Role, Status, Treatment  # Se importa la clase User para representar los datos de un usuario.
from ServerDao import UserDAO  # Se importa la clase UserDAO, la cual gestiona la interacción con los datos de los usuarios.

# Se crea la aplicación Flask.
app = Flask(__name__)

# Se configura una clave secreta para crear y validar los tokens JWT.
app.config['SECRET_KEY'] = 'DariellaCamille'

# Ruta para registrar un nuevo usuario.
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # Se obtienen los datos enviados en formato JSON.
    username = data.get("username")  # Se extrae el nombre de usuario.
    password = data.get("password")  # Se extrae la contraseña.
    email = data.get("email")  # Se extrae el correo electrónico.
    
    # Se verifica que se hayan enviado todos los datos necesarios.
    if not username or not password or not email:
        return jsonify({"error": "Faltan datos"}), 400

    user_dao = UserDAO()  # Se crea una instancia de UserDAO para interactuar con la base de datos de usuarios.

    # Se comprueba si el usuario ya existe.
    if user_dao.get_user(username, password):
        return jsonify({"error": "El usuario ya existe"}), 400

    # Se crea un nuevo usuario y se obtienen sus "hijos" asociados.
    new_user = user_dao.add_user(username, password, email)
    children = user_dao.get_children(new_user.id)

    # Se devuelve una respuesta exitosa con la información del nuevo usuario.
    return jsonify({
        "message": "Usuario registrado exitosamente",
        "user_info": new_user.__dict__,  # Se convierte el objeto usuario a un diccionario.
        "children": [child.__dict__ for child in children],  # Se convierten los objetos hijos a diccionarios.
    }), 201

# Ruta para validar el token enviado en el encabezado de la solicitud.
@app.route('/validate_token', methods=['POST'])
def validate_token():
    token = request.headers.get('Authorization')  # Se obtiene el token del encabezado de la petición.

    # Se verifica que el token haya sido proporcionado.
    if not token:
        return jsonify({"error": "Token no proporcionado"}), 400

    try:
        # Se decodifica el token usando la clave secreta y el algoritmo HS256.
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        user_id = decoded['user_id']  # Se extrae el ID del usuario del token.

        user_dao = UserDAO()  # Se crea una instancia de UserDAO.
        # Se busca el usuario en la lista de usuarios usando el ID extraído.
        user = next((user for user in user_dao.users if user.id == user_id), None)

        if user:
            # Se obtienen los hijos y TAPS asociados al usuario.
            children = user_dao.get_children(user.id)
            taps = user_dao.get_taps(user.id)
            # Se devuelve una respuesta indicando que la sesión es válida.
            return jsonify({
                "message": "Sesión válida",
                "user_info": user.__dict__,
                "children": [child.__dict__ for child in children],
                "taps": [tap.__dict__ for tap in taps]
            }), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 401

    except jwt.ExpiredSignatureError:
        # Se maneja el error si el token ha expirado.
        return jsonify({"error": "El token ha expirado"}), 401
    except jwt.InvalidTokenError:
        # Se maneja el error si el token es inválido.
        return jsonify({"error": "Token inválido"}), 401

# Ruta para que el usuario inicie sesión y se genere un token.
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Se obtienen los datos enviados en formato JSON.
    username = data.get("username")  # Se extrae el nombre de usuario.
    password = data.get("password")  # Se extrae la contraseña.

    # Se verifica que se hayan enviado el nombre de usuario y la contraseña.
    if not username or not password:
        return jsonify({"error": "Nombre de usuario o contraseña faltantes"}), 400

    user_dao = UserDAO()  # Se crea una instancia de UserDAO.
    user = user_dao.get_user(username, password)  # Se busca al usuario con las credenciales proporcionadas.

    if user:
        # Se crea un token JWT que contiene el ID del usuario y una fecha de expiración de 1 hora.
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        # Se obtienen los hijos y TAPS asociados al usuario.
        children = user_dao.get_children(user.id)
        taps = user_dao.get_taps(user.id)

        # Se devuelve una respuesta exitosa con el token y la información del usuario.
        return jsonify({
            "message": "Login exitoso",
            "user_info": user.__dict__,
            "token": token,
            "children": [child.__dict__ for child in children],
            "taps": [tap.__dict__ for tap in taps]
        }), 200
    else:
        # Se devuelve un error si las credenciales son incorrectas.
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

# Se inicia la aplicación en modo desarrollo.
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
