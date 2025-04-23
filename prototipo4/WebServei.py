from ServerDAOS import DAOUser, DAOChild  # Importar DAOUser y DAOChild

def show_user_info(user):
    print("\nInformación del usuario:")
    print(f"ID: {user['id']}")
    print(f"Nombre de usuario: {user['username']}")
    print(f"Correo electrónico: {user['email']}")

def show_children_info(user_id):
    child_dao = DAOChild()  # Crear una instancia de DAOChild
    children = child_dao.get_all_children()  # Obtener todos los niños
    child_dao.close_connection()

    # Filtrar los niños asociados al usuario
    user_children = [child for child in children if child['user_id'] == user_id]

    if user_children:
        print("\nInformación de los niños asociados:")
        for child in user_children:
            print(f"ID: {child['id']}, Nombre: {child['name']}, Edad: {child['age']}")
    else:
        print("\nNo hay niños asociados a este usuario.")

if __name__ == "__main__":
    dao = DAOUser()
    
    # Simulación de login
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    # Validar el usuario con el DAO
    user = dao.validate_user(username, password)
    if user:
        print("Login exitoso. Bienvenido:")
        print(f"Usuario: {user['username']}")

        while True:
            print("\nOpciones:")
            print("1. Ver información del usuario")
            print("2. Ver información de los niños asociados")
            print("3. Salir")
            option = input("Seleccione una opción: ")

            if option == "1":
                show_user_info(user)
            elif option == "2":
                show_children_info(user['id'])
            elif option == "3":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
    else:
        print("Credenciales incorrectas. Inténtelo de nuevo.")
    
    dao.close_connection()