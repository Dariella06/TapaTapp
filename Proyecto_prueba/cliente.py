# cliente.py (Cliente del juego de cartas)
import requests
import json
import os
from pathlib import Path

BASE_URL = "http://127.0.0.1:5000"
TOKEN_FILE = Path.home() / ".cardgame_token.json"

# ======================
# FUNCIONES AUXILIARES
# ======================

def guardar_token(token_data):
    try:
        with open(TOKEN_FILE, 'w') as f:
            json.dump({
                'token': token_data['token'],
                'user_id': token_data['user_id'],
                'username': token_data['username']
            }, f)
        os.chmod(TOKEN_FILE, 0o600)
        return True
    except Exception as e:
        print(f"[!] Error guardando token: {str(e)}")
        return False

def cargar_token():
    try:
        if not TOKEN_FILE.exists():
            return None
            
        with open(TOKEN_FILE, 'r') as f:
            data = json.load(f)
            if all(key in data for key in ['token', 'user_id', 'username']):
                return data
            return None
    except Exception as e:
        print(f"[!] Error cargando token: {str(e)}")
    return None

def eliminar_token():
    try:
        if TOKEN_FILE.exists():
            os.remove(TOKEN_FILE)
            return True
    except Exception as e:
        print(f"[!] Error eliminando token: {str(e)}")
    return False

def mostrar_partidas(partidas):
    print("\n=== PARTIDAS DISPONIBLES ===")
    for partida in partidas['waiting_matches']:
        print(f"ID: {partida['id']} - Creador: {partida['creator_name']} - Creada: {partida['created_at']}")

def mostrar_mazos(mazos):
    print("\n=== TUS MAZOS ===")
    for i, mazo in enumerate(mazos, 1):
        print(f"{i}. ID: {mazo['id']} - Nombre: {mazo['name']} - Cartas: {len(mazo.get('cards', []))}")

def mostrar_cartas(cartas):
    print("\n=== CARTAS DISPONIBLES ===")
    for carta in cartas:
        print(f"ID: {carta['id']} - Nombre: {carta['name']} - Tipo: {carta['type']} - Costo: {carta['cost']}")

def mostrar_estado_partida(partida):
    print("\n=== ESTADO DE LA PARTIDA ===")
    print(f"ID: {partida['match_info']['id']}")
    print(f"Turno: {partida['match_info']['current_turn']}")
    
    # Obtener nombre del jugador actual
    current_player_id = partida['match_info']['current_player']
    current_player_name = None
    for jugador in partida['players']:
        if jugador['player_id'] == current_player_id:
            current_player_name = jugador['username']
            break
    
    print(f"Jugador actual: {current_player_name if current_player_name else 'Desconocido'}")
    
    print("\nJugadores:")
    for jugador in partida['players']:
        print(f"- {jugador['username']} (Vida: {jugador['life_points']}, Mana: {jugador['mana_available']}/{jugador['mana_max']})")
    
    if partida.get('player_deck'):
        print("\nCartas en tu mano:")
        for carta in partida['player_deck'][:5]:  # Mostrar primeras 5 cartas como ejemplo
            print(f"- {carta['name']} (Costo: {carta['cost']})")

# ======================
# FUNCIONES PRINCIPALES
# ======================

def menu_inicio():
    while True:
        print("\n=== MENÚ DE INICIO ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        
        opcion = input("\nOpción: ").strip()
        
        if opcion == "1":
            if iniciar_sesion():
                return True  # Usuario autenticado
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("\n[+] ¡Hasta pronto!")
            exit()
        else:
            print("\n[!] Opción no válida")

def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    email = input("Email: ").strip()

    try:
        response = requests.post(
            f"{BASE_URL}/register",
            json={"username": username, "password": password, "email": email},
            timeout=5
        )
        
        if response.status_code == 201:
            print("\n[+] ¡Usuario registrado exitosamente!")
        else:
            error_msg = response.json().get('error', 'Error desconocido')
            print(f"\n[!] Error en el registro: {error_msg}")
    except requests.exceptions.RequestException as e:
        print(f"\n[!] Error de conexión: {str(e)}")

def iniciar_sesion():
    print("\n=== INICIO DE SESIÓN ===")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    
    try:
        response = requests.post(
            f"{BASE_URL}/login",
            json={"username": username, "password": password},
            timeout=5
        )
        
        if response.status_code == 200:
            if guardar_token(response.json()):
                print("\n[+] Sesión iniciada correctamente")
                return True
            else:
                print("\n[!] No se pudo guardar el token")
        else:
            error_msg = response.json().get('error', 'Credenciales incorrectas')
            print(f"\n[!] {error_msg}")
    except requests.exceptions.RequestException as e:
        print(f"\n[!] Error de conexión: {str(e)}")
    
    return False

def menu_mazos(token_data):
    headers = {'Authorization': f'Bearer {token_data["token"]}'}
    
    while True:
        print("\n=== MENÚ DE MAZOS ===")
        print("1. Ver mis mazos")
        print("2. Crear nuevo mazo")
        print("3. Añadir carta a mazo")
        print("4. Ver cartas disponibles")
        print("5. Eliminar un mazo")
        print("6. Volver al menú principal")
        
        opcion = input("\nOpción: ").strip()
        
        try:
            if opcion == "1":
                response = requests.get(
                    f"{BASE_URL}/decks",
                    headers=headers,
                    timeout=5
                )
                
                if response.status_code == 200:
                    mostrar_mazos(response.json())
                else:
                    error_msg = response.json().get('error', 'Error al obtener mazos')
                    print(f"\n[!] {error_msg}")
            
            elif opcion == "2":
                nombre = input("Nombre del nuevo mazo: ").strip()
                response = requests.post(
                    f"{BASE_URL}/decks",
                    headers=headers,
                    json={"name": nombre},
                    timeout=5
                )
                
                if response.status_code == 201:
                    print("\n[+] Mazo creado exitosamente!")
                    print(f"ID del mazo: {response.json()['deck_id']}")
                else:
                    error_msg = response.json().get('error', 'Error al crear mazo')
                    print(f"\n[!] {error_msg}")
            
            elif opcion == "3":
                deck_id = input("ID del mazo: ").strip()
                card_id = input("ID de la carta a añadir: ").strip()
                quantity = input("Cantidad (opcional, default 1): ").strip() or "1"
                
                response = requests.post(
                    f"{BASE_URL}/decks/{deck_id}/cards",
                    headers=headers,
                    json={"card_id": card_id, "quantity": int(quantity)},
                    timeout=5
                )
                
                if response.status_code == 200:
                    print("\n[+] Carta añadida al mazo exitosamente!")
                else:
                    error_msg = response.json().get('error', 'Error al añadir carta')
                    print(f"\n[!] {error_msg}")
            
            elif opcion == "4":
                response = requests.get(
                    f"{BASE_URL}/cards",
                    headers=headers,
                    timeout=5
                )
                
                if response.status_code == 200:
                    mostrar_cartas(response.json())
                else:
                    error_msg = response.json().get('error', 'Error al obtener cartas')
                    print(f"\n[!] {error_msg}")
            
            elif opcion == "5":
                deck_id = input("ID del mazo a eliminar: ").strip()
                confirm = input("¿Estás seguro de que quieres eliminar este mazo? (s/n): ").strip().lower()
                
                if confirm == 's':
                    response = requests.delete(
                        f"{BASE_URL}/decks/{deck_id}",
                        headers=headers,
                        timeout=5
                    )
                    
                    if response.status_code == 200:
                        print("\n[+] Mazo eliminado exitosamente!")
                    else:
                        error_msg = response.json().get('error', 'Error al eliminar mazo')
                        print(f"\n[!] {error_msg}")
            
            elif opcion == "6":
                break
            
            else:
                print("\n[!] Opción no válida")
        
        except requests.exceptions.RequestException as e:
            print(f"\n[!] Error de conexión: {str(e)}")

def menu_principal_partidas(token_data):
    """Nuevo menú principal de partidas"""
    headers = {'Authorization': f'Bearer {token_data["token"]}'}
    
    while True:
        print("\n=== MENÚ PRINCIPAL DE PARTIDAS ===")
        print("1. Crear nueva partida")
        print("2. Ver partidas disponibles")
        print("3. Unirse a partida")
        print("4. Volver al menú principal")
        
        opcion = input("\nOpción: ").strip()
        
        try:
            if opcion == "1":
                # Crear nueva partida y entrar directamente al juego
                response = requests.get(
                    f"{BASE_URL}/decks",
                    headers=headers,
                    timeout=5
                )
                
                if response.status_code != 200:
                    error_msg = response.json().get('error', 'Error al obtener mazos')
                    print(f"\n[!] {error_msg}")
                    continue
                
                mazos = response.json()
                if not mazos:
                    print("\n[!] No tienes mazos creados. Crea un mazo primero.")
                    continue
                
                mostrar_mazos(mazos)
                deck_id = input("\nID del mazo con el que jugar: ").strip()
                
                response = requests.post(
                    f"{BASE_URL}/matches",
                    headers=headers,
                    json={"deck_id": deck_id},
                    timeout=5
                )
                
                if response.status_code == 201:
                    print("\n[+] Partida creada exitosamente!")
                    print(f"ID de partida: {response.json()['match_id']}")
                    # Entrar directamente al menú de juego
                    menu_juego_partida(token_data, response.json()['match_id'])
                else:
                    error_msg = response.json().get('error', 'Error al crear partida')
                    print(f"\n[!] {error_msg}")
            
            elif opcion == "2":
                # Ver partidas disponibles
                response = requests.get(
                    f"{BASE_URL}/matches",
                    headers=headers,
                    timeout=5
                )
                
                if response.status_code == 200:
                    mostrar_partidas(response.json())
                else:
                    error_msg = response.json().get('error', 'Error al obtener partidas')
                    print(f"\n[!] {error_msg}")
            
            elif opcion == "3":
                # Unirse a partida existente
                match_id = input("ID de partida a unirse: ").strip()
                
                response = requests.get(
                    f"{BASE_URL}/decks",
                    headers=headers,
                    timeout=5
                )
                
                if response.status_code != 200:
                    error_msg = response.json().get('error', 'Error al obtener mazos')
                    print(f"\n[!] {error_msg}")
                    continue
                
                mazos = response.json()
                if not mazos:
                    print("\n[!] No tienes mazos creados. Crea un mazo primero.")
                    continue
                
                mostrar_mazos(mazos)
                deck_id = input("\nID del mazo con el que jugar: ").strip()
                
                response = requests.post(
                    f"{BASE_URL}/matches/{match_id}/join",
                    headers=headers,
                    json={"deck_id": deck_id},
                    timeout=5
                )
                
                if response.status_code == 200:
                    print("\n[+] Te has unido a la partida!")
                    # Entrar directamente al menú de juego
                    menu_juego_partida(token_data, match_id)
                else:
                    error_msg = response.json().get('error', 'Error al unirse a partida')
                    print(f"\n[!] {error_msg}")
            
            elif opcion == "4":
                break
            
            else:
                print("\n[!] Opción no válida")
        
        except requests.exceptions.RequestException as e:
            print(f"\n[!] Error de conexión: {str(e)}")

def menu_juego_partida(token_data, match_id):
    """Menú cuando ya estás dentro de una partida"""
    headers = {'Authorization': f'Bearer {token_data["token"]}'}
    
    while True:
        print("\n=== MENÚ DE JUEGO ===")
        print("1. Ver estado de la partida")
        print("2. Realizar acción (si es tu turno)")
        print("3. Rendirse/Abandonar partida")
        
        opcion = input("\nOpción: ").strip()
        
        try:
            if opcion == "1":
                # Ver estado actual
                response = requests.get(
                    f"{BASE_URL}/matches/current",
                    headers=headers,
                    timeout=5
                )
                
                if response.status_code == 200:
                    mostrar_estado_partida(response.json())
                else:
                    error_msg = response.json().get('error', 'Error al obtener partida')
                    print(f"\n[!] {error_msg}")
            
            elif opcion == "2":
                # Realizar acción
                response = requests.get(
                    f"{BASE_URL}/matches/current",
                    headers=headers,
                    timeout=5
                )
                
                if response.status_code != 200:
                    error_msg = response.json().get('error', 'Error al verificar turno')
                    print(f"\n[!] {error_msg}")
                    continue
                
                partida = response.json()
                if partida['match_info']['current_player'] != token_data['user_id']:
                    print("\n[!] No es tu turno ahora mismo")
                    continue
                
                print("\nAcciones disponibles:")
                print("1. Pasar turno")
                print("2. Jugar carta")
                action = input("Elige acción: ").strip()
                
                if action == "1":
                    response = requests.post(
                        f"{BASE_URL}/matches/action",
                        json={"action": "end_turn"},
                        headers=headers,
                        timeout=5
                    )
                    
                    if response.status_code == 200:
                        print("\n[+] Turno pasado exitosamente!")
                    else:
                        error_msg = response.json().get('error', 'Error al pasar turno')
                        print(f"\n[!] {error_msg}")
                
                elif action == "2":
                    # Mostrar cartas disponibles
                    if partida.get('player_deck'):
                        print("\nTus cartas disponibles:")
                        for carta in partida['player_deck']:
                            print(f"ID: {carta['id']} - {carta['name']} (Costo: {carta['cost']})")
                    
                    card_id = input("\nID de la carta a jugar: ").strip()
                    response = requests.post(
                        f"{BASE_URL}/matches/action",
                        json={"action": "play_card", "card_id": card_id},
                        headers=headers,
                        timeout=5
                    )
                    
                    if response.status_code == 200:
                        print("\n[+] Carta jugada exitosamente!")
                    else:
                        error_msg = response.json().get('error', 'Error al jugar carta')
                        print(f"\n[!] {error_msg}")
                else:
                    print("\n[!] Acción no válida")
                    continue
            
            elif opcion == "3":
                # Abandonar partida con confirmación
                confirm = input("\n¿Estás seguro que quieres abandonar la partida? (s/n): ").strip().lower()
                if confirm == "s":
                    response = requests.post(
                        f"{BASE_URL}/matches/{match_id}/surrender",
                        headers=headers,
                        json={},  # Asegurarse de enviar un JSON vacío si el endpoint lo espera
                        timeout=5
                    )
                    
                    if response.status_code == 200:
                        print("\n[+] Has abandonado la partida")
                        print("El otro jugador recibirá una notificación de victoria")
                        return  # Salir del menú de juego
                    else:
                        try:
                            error_msg = response.json().get('error', 'Error al abandonar partida')
                            print(f"\n[!] {error_msg}")
                        except:
                            print("\n[!] Error desconocido al abandonar partida")
                else:
                    print("\n[+] Continúas en la partida")
            
            else:
                print("\n[!] Opción no válida")
        
        except requests.exceptions.RequestException as e:
            print(f"\n[!] Error de conexión: {str(e)}")
        except json.JSONDecodeError:
            print("\n[!] Error procesando la respuesta del servidor")
            
def menu_principal(token_data):
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestionar mazos")
        print("2. Jugar partida")
        print("3. Cerrar sesión")
        
        opcion = input("\nOpción: ").strip()
        
        if opcion == "1":
            menu_mazos(token_data)
        elif opcion == "2":
            menu_principal_partidas(token_data)
        elif opcion == "3":
            if eliminar_token():
                print("\n[+] Sesión cerrada correctamente")
            break
        else:
            print("\n[!] Opción no válida")

if __name__ == "__main__":
    # Mostrar menú de inicio primero
    if menu_inicio():
        # Si el usuario inició sesión, cargar token y mostrar menú principal
        token_data = cargar_token()
        if token_data:
            menu_principal(token_data)