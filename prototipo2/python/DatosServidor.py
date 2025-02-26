# User Class
class User:
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def __str__(self):
        return self.first_name + " " + self.last_name + "(" + self.email + ")"

# Child Class
class Child:
    def __init__(self, id, first_name, last_name, treatment_id, average_sleep):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.treatment_id = treatment_id
        self.average_sleep = average_sleep
    
    def __str__(self):
        return self.first_name + " " + self.last_name + " (Treatment: " + str(self.treatment_id) + ", Sleep: " + str(self.average_sleep) + " hrs)"

# Treatment Class
class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return "Treatment " + str(self.id) + ": " + self.name

# Tap Class
class Tap:
    def __init__(self, id, child_id, status_id, user_id, start, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.start = start
        self.end = end
    
    def __str__(self):
        return "Tap " + str(self.id) + " (Child " + str(self.child_id) + " - Status " + str(self.status_id) + ")"

# Status Class
class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return "Status " + str(self.id) + ": " + self.name

# Role Class
class Role:
    def __init__(self, id, role_type):
        self.id = id
        self.role_type = role_type
    
    def __str__(self):
        return "Role " + str(self.id) + ": " + self.role_type


# Verification Code Class
class VerificationCode:
    def __init__(self, user_id, code):
        self.user_id = user_id
        self.code = code
    
    def __str__(self):
        return "Verification Code for User " + str(self.user_id) + ": " + self.code


# Sample Data
users = [
    User(1, "Mother", "Perez", "mother@gmail.com", "1234"),
    User(2, "Father", "Lopez", "father@gmail.com", "3564")
]

# Children
children = [
    Child(1, "Dariella", "Child", 1, 9),
    Child(2, "Camille", "Child", 2, 5)
]

# Treatments
treatments = [
    Treatment(1, "Hour"),
    Treatment(2, "Percentage")
]

# Roles
roles = [
    Role(1, "Admin"),
    Role(2, "Tutor Mother Father"),
    Role(3, "Caregiver"),
    Role(4, "Follow-up")
]

# Statuses
statuses = [
    Status(1, "Sleeping"),
    Status(2, "Awake"),
    Status(3, "No Patch"),
    Status(4, "No Patch")
]

# User-Child Relationship
user_child_relationship = [
    {"user_id": 1, "child_id": 1, "role_id": 1},
    {"user_id": 1, "child_id": 1, "role_id": 2},
    {"user_id": 2, "child_id": 2, "role_id": 1},
    {"user_id": 2, "child_id": 2, "role_id": 2}
]

# Verification
verification_codes = [
    VerificationCode(1, "ABC123"),
    VerificationCode(2, "XYZ789")
]
