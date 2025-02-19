# Classe de Usuarios
class Usuario:
    def __init__(self, id, nombre, apellido, email, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
    
    def __str__(self):
        return self.nombre + " " + self.apellido + "(" + self.email + ")"

# Classe de Niños
class Niño:
    def __init__(self, id, nombre, apellido, tratamiento_id, promedio_sueño):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.tratamiento_id = tratamiento_id
        self.promedio_sueño = promedio_sueño
    
    def __str__(self):
        return self.nombre + " " + self.apellido + " (Tratamiento: " + str(self.tratamiento_id) + ", Sueño: " + str(self.promedio_sueño) + " hrs)"

# Classe de Tratamiento
class Tratamiento:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    def __str__(self):
        return "Tratamiento " + str(self.id) + ": " + self.nombre

# Classe de Tap
class Tap:
    def __init__(self, id, niño_id, estado_id, usuario_id, inicio, fin):
        self.id = id
        self.niño_id = niño_id
        self.estado_id = estado_id
        self.usuario_id = usuario_id
        self.inicio = inicio
        self.fin = fin
    
    def __str__(self):
        return "Tap " + str(self.id) + " (Niño " + str(self.niño_id) + " - Estado " + str(self.estado_id) + ")"

# Classe de Estado
class Estado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    def __str__(self):
        return "Estado " + str(self.id) + ": " + self.nombre

# Classe de Rol
class Rol:
    def __init__(self, id, tipo_rol):
        self.id = id
        self.tipo_rol = tipo_rol
    
    def __str__(self):
        return "Rol " + str(self.id) + ": " + self.tipo_rol


# Classe de codigo de verificación
class CodigoVerificacion:
    def __init__(self, usuario_id, codigo):
        self.usuario_id = usuario_id
        self.codigo = codigo
    
    def __str__(self):
        return "Código de Verificación para Usuario " + str(self.usuario_id) + ": " + self.codigo


# Datos de ejemplo
usuarios = [
    Usuario(1, "Madre", "Perez", "madre@gmail.com", "1234"),
    Usuario(2, "Padre", "Lopez", "padre@gmail.com", "3564")
]

# Niños
niños = [
    Niño(1, "Dariella", "Child", 1, 9),
    Niño(2, "Jaco", "Child", 2, 5)
]


# Tratamientos
tratamientos = [
    Tratamiento(1, "Hora"),
    Tratamiento(2, "Porcentaje")
]


# Roles
roles = [
    Rol(1, "Admin"),
    Rol(2, "Tutor Madre Padre"),
    Rol(3, "Cuidador"),
    Rol(4, "Seguimiento")
]


# Estados
estados = [
    Estado(1, "Dormir"),
    Estado(2, "Despierto"),
    Estado(3, "Sin Parche"),
    Estado(4, "No Parche")
]

# Relación del usuario de niñoc
relacion_usuario_niño = [
    {"usuario_id": 1, "niño_id": 1, "rol_id": 1},
    {"usuario_id": 1, "niño_id": 1, "rol_id": 2},
    {"usuario_id": 2, "niño_id": 2, "rol_id": 1},
    {"usuario_id": 2, "niño_id": 2, "rol_id": 2}
]

# Verificación
codigos_verificacion = [
    CodigoVerificacion(1, "ABC123"),
    CodigoVerificacion(2, "XYZ789")
]
