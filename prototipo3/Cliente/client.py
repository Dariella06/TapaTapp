import requests

# Función para autenticar al usuario a través del servidor Flask
def authenticate_user(username, password):
    response = requests.post('http://localhost:10050/prototipo2', json={"username": username, "password": password})
    return response

# Función para mostrar la información del usuario
def show_user_info(user):
    print(f"Nombre de 👤: {user['username']}")
    print(f"Correo 💌: {user['email']}")
    print(f"Contraseña 🔑: {user['password']}")

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
# Función principal
def main():
    print(" ")
    username = input("Introduce tu nombre de 👤: ")
    password = input("🙊 Introduce tu password 🙊: ")
    
    response = authenticate_user(username, password)
    
    if response.status_code == 200:
        data = response.json()
        print(" ")
        print(f"💖 Bienvenido💖, {data['user_info']['username']}!")
        print("Elige una de las opciones que tenemos para que puedas ver la funcionalidad del TapaTapp💖")
        print(" ")

        while True:
            print("Selecciona una opción:")
            print("1. ℹℹ User info")
            print("2. 👶 List Child with Taps")
            print("3. 💨 Salir")
            
            option = input("Selecciona una opción: ")
            
            if option == "1":
                print(" ")
                show_user_info(data['user_info'])
                print(" ")
            elif option == "2":
                print(" ")
                list_children_with_taps(data['children'], data['taps'])  # Cambia esto para usar los datos de taps
                print(" ")
            elif option == "3":
                print(" ")
                print("Espero que vuelvas pronto 😘💖")
                print("Saliendo del programa...")
                break
            else:
                print(" ")
                print("Opción no válida.")
                print(" ")
    else:
        print("Usuario o contraseña incorrectos.")
if __name__ == "__main__":
    main()