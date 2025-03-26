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
                print(f"  - Tap ID: {tap['id']}, Inicio⌛: {tap['init']}, Fin⏳: {tap['end']}")
        else:
            print("  - No tiene registros de Tap.")

# Función principal
def main():
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