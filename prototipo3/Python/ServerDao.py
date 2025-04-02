from ServerDatos import users, children, taps, relation_user_child, User

class UserDAO:
    def __init__(self):
        self.users = users
        self.children = children
        self.taps = taps
        self.relations = relation_user_child

    def get_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def add_user(self, username, password, email):
        new_id = len(self.users) + 1
        new_user = User(new_id, username, password, email)
        self.users.append(new_user)
        
        default_child_ids = [1, 2]
        for child_id in default_child_ids:
            self.relations.append({"user_id": new_user.id, "child_id": child_id, "rol_id": 1})
        
        return new_user
    
    def get_children(self, user_id):
        child_ids = [rel["child_id"] for rel in self.relations if rel["user_id"] == user_id]
        return [child for child in self.children if child.id in child_ids]

    def get_taps(self, user_id):
        child_ids = [rel["child_id"] for rel in self.relations if rel["user_id"] == user_id]
        return [tap for tap in self.taps if tap.child_id in child_ids]
