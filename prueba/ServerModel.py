class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end

class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name