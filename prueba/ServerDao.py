from ServerDatos import users, User

class UserDAO:
    def __init__(self):
        self.users = users

    def get_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def add_user(self, username, password, email):
        new_id = len(self.users) + 1
        new_user = User(new_id, username, password, email)
        self.users.append(new_user)
        return new_user