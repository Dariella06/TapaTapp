import requests

# Función para registrar un nuevo usuario
def register_user(username, password, email):
    response = requests.post('http://localhost:10050/register', json={"username": username, "password": password, "email": email})
    return response

# Función para autenticar al usuario
def authenticate_user(username, password):
    response = requests.post('http://localhost:10050/login', json={"username": username, "password": password})
    return response

# Función para mostrar la información del usuario
def show_user_info(user):
    print(f"Nombre de 👤: {user['username']}")
    print(f"Correo 💌: {user['email']}")

# Función para listar niños  
def list_children_with_taps(children, taps):
    print("Lista de niños 👶 con sus registros de Tap:")
    for child in children:
        print(f"\n🆔: {child['id']}, Nombre🦝: {child['child_name']}, Promedio de sueño💤: {child['sleep_average']}, ID de tratamiento💊: {child['treatment_id']}, Tiempo⌛: {child['time']}")
        print("Registros de Tap📔:")
        child_taps = [tap for tap in taps if tap['child_id'] == child['id']]
        if child_taps:
            for tap in child_taps:
                print(f"  - Tap ID: {tap['id']}, Estado: {tap['status']}")
        else:
            print("  - No tiene registros de Tap.")

# Función principal
def main():
    token = None  # Variable para almacenar el token
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
            print("")
            username = input("Introduce tu nombre de 👤: ")
            password = input("🙊 Introduce tu password 🙊: ")
            response = authenticate_user(username, password)
            print("")
            
            if response.status_code == 200:
                data = response.json()
                token = data['token']  # Almacena el token
                print(f"💖 Bienvenido💖, {data['user_info']['username']}!")
                
                while True:
                    print("Selecciona una opción:")
                    print("1. ℹℹ User info")
                    print("2. 👶 Listar todos los niños con Taps")
                    print("3. 💨 Cerrar sesión")
                    
                    option = input("Selecciona una opción: ")
                    
                    if option == "1":
                        print("")
                        show_user_info(data['user_info'])
                        print("")
                    elif option == "2":
                        print("")
                        list_children_with_taps(data['children'], data['taps'])
                        print("")
                    elif option == "3":
                        print("")
                        print("Cerrando sesión...")
                        token = None  # Limpia el token al cerrar sesión
                        print("¿Quieres continuar con la última sesión abierta o iniciar sesión nuevamente?")
                        print("1. Continuar con la última sesión")
                        print("2. Iniciar sesión")
                        choice = input("Selecciona una opción: ")
                        
                        if choice == "1" and token:
                            # Verificar el token
                            response = requests.get('http://localhost:10050/protected', headers={"Authorization": f"Bearer {token}"})
                            if response.status_code == 200:
                                print("Sesión activa. Puedes continuar.")
                                # Aquí puedes agregar más lógica para continuar la sesión
                            else:
                                print("Token inválido o sesión expirada.")
                                token = None  # Limpia el token si es inválido
                        elif choice == "2":
                            continue  # Regresa al inicio del bucle para iniciar sesión nuevamente
                        else:
                            print("Opción no válida.")
                        print("")
                        break
                    else:
                        print("")
                        print("Opción no válida.")
            else:
                print("Usuario o contraseña incorrectos.")
                print("")
        
        elif option == "3":
            print("")
            print("Saliendo del programa...")
            print("")
            break
        else:
            print("")
            print("Opción no válida.")
            print("")

if __name__ == "__main__":
    main()