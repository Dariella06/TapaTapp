import requests

# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Password: {self.password}, Email: {self.email}"

class UserDAO:
    @staticmethod
    def get_user_by_username(username, email, password):
        response = requests.get(f'http://localhost:10050/prototip1/getser?username={username}&email={email}&password={password}')
        if response.status_code == 200:
            user_data = response.json()
            user = User(user_data['id'], user_data['username'], user_data['password'], user_data['email'])
            return user
        else:
            return None
        
class ViewConsole:
    @staticmethod
    def get_input_username():
        return input("Enter username: ")
    
    @staticmethod
    def get_input_email():
        return input("Enter email: ")
    
    @staticmethod
    def get_input_password():
        return input("Enter password: ")
    
    @staticmethod
    def show_user_info(username, email, password):
        user = UserDAO.get_user_by_username(username, email, password)
        if user:
            print(f"User Info: {user}")
        else:
            print(f"User with username {username} not found")

if __name__ == "__main__":
    username = ViewConsole.get_input_username()
    email = ViewConsole.get_input_email()
    password = ViewConsole.get_input_password()
    ViewConsole.show_user_info(username, email, password)
