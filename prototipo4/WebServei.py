from ServerDAOS import DAOUser


if __name__ == "__main__":
    dao = DAOUser()
    
    # Simulación de login
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    # Validar el usuario con el DAO
    user = dao.validate_user(username, password)
    if user:
        print("Login exitoso. Bienvenido:")
        print(user)
    else:
        print("Credenciales incorrectas. Inténtelo de nuevo.")
    
    dao.close_connection()