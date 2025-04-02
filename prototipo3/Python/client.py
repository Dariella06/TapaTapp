import requests  # Esta es la librería requests, que se utiliza para hacer peticiones HTTP a otros servidores.

# Esta función envía una petición POST a la ruta /register para registrar un usuario.
def register_user(username, password, email):
    # Se envía una solicitud POST al servidor local con los datos del usuario en formato JSON.
    response = requests.post(
        'http://localhost:5000/register',
        json={"username": username, "password": password, "email": email}
    )
    return response

# Esta función envía una petición POST a la ruta /login para autenticar al usuario.
def authenticate_user(username, password):
    # Se envía una solicitud POST con el nombre de usuario y la contraseña.
    response = requests.post(
        'http://localhost:5000/login',
        json={"username": username, "password": password}
    )
    return response

# Esta función envía una petición POST a la ruta /validate_token para validar un token JWT.
def validate_token(token):
    # Se prepara un encabezado HTTP que incluye el token de autorización.
    headers = {'Authorization': token}
    # Se envía la solicitud POST con el encabezado configurado.
    response = requests.post(
        'http://localhost:5000/validate_token',
        headers=headers
    )
    return response

# Esta función muestra en consola la información básica del usuario.
def show_user_info(user):
    print("\nNombre de 👤:", user['username'])  # Muestra el nombre del usuario.
    print("Correo 💌:", user['email'])  # Muestra el correo del usuario.
    print("")

# Esta función lista los niños asociados al usuario y sus registros de Tap.
def list_children_with_taps(children, taps):
    if not children:
        print("Aún no tienes niños asociados. Puedes añadir niños más tarde.")
        return

    print("Lista de niños 👶 con sus registros de Tap:")
    for child in children:
        # Muestra los detalles básicos de cada niño.
        print(f"\n🆔: {child['id']}, Nombre🦝: {child['child_name']}, Promedio de sueño💤: {child['sleep_average']}, ID de tratamiento💊: {child['treatment_id']}, Tiempo⌛: {child['time']}")
        
        # Se filtran los registros de Tap que correspondan al niño actual.
        child_taps = [tap for tap in taps if tap['child_id'] == child['id']]
        if child_taps:
            print("Registros de Tap📔:")
            for tap in child_taps:
                # Se muestran los detalles de cada registro de Tap.
                print(f"  - Tap ID: {tap['id']}, Inicio⌛: {tap['init']}, Fin⏳: {tap['end']}")
        else:
            print("  - No tiene registros de Tap.")

# Función principal que muestra un menú interactivo para el usuario.
def main():
    token = None  
    saved_username = None
    saved_password = None

    while True:
        # Se muestra el menú de opciones.
        print("\nSelecciona una opción:")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        option = input("Selecciona una opción: ")
        print("")
        
        if option == "1":
            # Se solicitan los datos del usuario para registrarse.
            username = input("Introduce tu nombre de 👤: ")
            password = input("🙊 Introduce tu password 🙊: ")
            email = input("Introduce tu correo 💌: ")
            response = register_user(username, password, email)
            
            if response.status_code == 201:
                print("Usuario registrado exitosamente!")
            else:
                # Se muestra el error obtenido del servidor.
                print(response.json().get("error", "Error al registrar el usuario."))
        
        elif option == "2":
            # Se solicitan los datos del usuario para iniciar sesión.
            username = input("Introduce tu nombre de 👤: ")
            password = input("🙊 Introduce tu password 🙊: ")
            response = authenticate_user(username, password)

            if response.status_code == 200:
                data = response.json()
                token = data.get('token')
                saved_username = username  
                saved_password = password
                
                print(f"💖 Bienvenido💖, {data['user_info']['username']}!")
                
                while True:
                    # Se muestra un submenú para opciones post-login.
                    print("\nSelecciona una opción:")
                    print("1. ℹℹ User info")
                    print("2. 👶 List Child with Taps")
                    print("3. 💨 Cerrar Sesión")
                    
                    option = input("Selecciona una opción: ")
                    
                    if option == "1":
                        show_user_info(data['user_info'])
                    elif option == "2":
                        list_children_with_taps(data['children'], data['taps'])
                    elif option == "3":
                        print("\nCerrando Sesión...\n")
                        print("Elige una opción:")
                        print("1. Continuar sesión")
                        print("2. Volver al menú principal")
                        
                        option = input("Selecciona una opción: ")
                        if option == "1":
                            print("\nVerificando sesión...")
                            response = validate_token(token)

                            if response.status_code == 200:
                                data = response.json()
                                print(f"Sesión reanudada para {data['user_info']['username']}.")
                            else:
                                print("El token ha expirado o es inválido. Reautenticando...")
                                response = authenticate_user(saved_username, saved_password)
                                if response.status_code == 200:
                                    data = response.json()
                                    token = data.get('token')  # Se actualiza el token.
                                    print(f"\nSesión iniciada nuevamente para {data['user_info']['username']}.")
                                else:
                                    print("Error al reautenticar. Debes iniciar sesión manualmente.")
                                    token = None
                                    break
                        elif option == "2":
                            print("\nVolviendo al menú principal...\n")
                            break 
                        else:
                            print("Opción no válida.")
                    else:
                        print("Opción no válida.")
            else:
                print("Usuario o contraseña incorrectos.")
        
        elif option == "3":
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción no válida.")

# Se ejecuta la función principal si este archivo es el programa principal.
if __name__ == "__main__":
    main()
