import requests

# Función para registrar un nuevo usuario
def register_user(username, password, email):
    response = requests.post('http://localhost:5000/register', json={"username": username, "password": password, "email": email})
    return response

# Función para autenticar al usuario
def authenticate_user(username, password):
    response = requests.post('http://localhost:5000/login', json={"username": username, "password": password})
    return response

# Función para validar el token y continuar la sesión
def validate_token(token):
    headers = {'Authorization': token}
    response = requests.post('http://localhost:5000/validate_token', headers=headers)
    return response

# Función para mostrar la información del usuario
def show_user_info(user):
    print("")
    print(f"Nombre de 👤: {user['username']}")
    print(f"Correo 💌: {user['email']}")

# Función para listar niños y sus Taps  
def list_children_with_taps(children, taps):
    print("Lista de niños 👶 con sus registros de Tap:")
    for child in children:
        print(f"\n🆔: {child['id']}, Nombre🦝: {child['child_name']}, Promedio de sueño💤: {child['sleep_average']}, ID de tratamiento💊: {child['treatment_id']}, Tiempo⌛: {child['time']}")
        print("Registros de Tap📔:")
        
        child_taps = [tap for tap in taps if tap['child_id'] == child['id']]
        
        if child_taps:
            for tap in child_taps:
                print(f"  - Tap ID: {tap['id']}, Estado: {tap['status_id']}, Inicio: {tap['init']}, Fin: {tap['end']}")
        else:
            print("  - No tiene registros de Tap.")

# Función principal
def main():
    token = None  
    while True:
        print("Selecciona una opción:")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        option = input("Selecciona una opción: ")
        print("")
        
        if option == "1":
            print("")
            username = input("Introduce tu nombre de 👤: ")
            password = input("🙊 Introduce tu password 🙊: ")
            email = input("Introduce tu correo 💌: ")
            print("")

            response = register_user(username, password, email)
            if response.status_code == 201:
                print("Usuario registrado exitosamente!")
                print("")
            else:
                print(response.json().get("error", "Error al registrar el usuario."))
        
        elif option == "2":
            username = input("Introduce tu nombre de 👤: ")
            password = input("🙊 Introduce tu password 🙊: ")
            response = authenticate_user(username, password)
            print("")

            if response.status_code == 200:
                data = response.json()
                token = data.get('token')
                print(f"💖 Bienvenido💖, {data['user_info']['username']}!")
                print("Elige una de las opciones que tenemos para que puedas ver la funcionalidad del TapaTapp💖")
                print(" ")

                while True:
                    print("")
                    print("Selecciona una opción:")
                    print("1. ℹℹ User info")
                    print("2. 👶 List Child with Taps")
                    print("3. 💨 Cerrar Sesión")
                    
                    option = input("Selecciona una opción: ")
                    
                    if option == "1":
                        show_user_info(data['user_info'])
                    elif option == "2":
                        list_children_with_taps(data.get('children', []), data.get('taps', []))
                    elif option == "3":
                        print("")
                        print("Cerrando Sesión...")
                        print("")
                        print("Elige una opción:")
                        print("1. Continuar la sesión")
                        print("2. Volver al menú principal")
                        
                        option = input("Selecciona una opción: ")
                        if option == "1":
                            print("")
                            print("Verificando sesión...")
                            response = validate_token(token)
                            if response.status_code == 200:
                                data = response.json()
                                print(f"Sesión reanudada para {data['user_info']['username']}.")
                                break 
                            else:
                                print("El token ha expirado o es inválido. Por favor, inicia sesión nuevamente.")
                                token = None
                                break
                        elif option == "2":
                            print("")
                            print("Volviendo al menú principal...")
                            print("")
                            break 
                        else:
                            print("")
                            print("Opción no válida.")
                    else:
                        print("")
                        print("Opción no válida.")
            else:
                print("Usuario o contraseña incorrectos.")
                print("")
        
        elif option == "3":
            print("Saliendo del programa...")
            print("")
            break
        else:
            print("Opción no válida.")
            print("")

if __name__ == "__main__":
    main()