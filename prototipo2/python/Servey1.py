import DatosServidor as dades 
# DAO para usuarios
class UsuarioDAO:
    def __init__(self):
        self.usuarios = UsuarioDAO

    def get_all_usuarios(self):
        return [usuario.__dict__ for usuario in self.usuarios]

    def get_usuario_by_email(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario.__dict__
        return None


# DAO para niños
class NiñoDAO:
    def __init__(self):
        self.niños = NiñoDAO

    def get_all_niños(self):
        return [niño.__dict__ for niño in self.niños]

    def get_niños_by_usuario_id(self, usuario_id):
        niño_ids = [rel["niño_id"] for rel in NiñoDAO if rel["usuario_id"] == usuario_id]
        return [niño.__dict__ for niño in self.niños if niño.id in niño_ids]


# DAO para tratamientos
class TratamientoDAO:
    def __init__(self):
        self.tratamientos = TratamientoDAO

    def get_all_tratamientos(self):
        return [tratamiento.__dict__ for tratamiento in self.tratamientos]


# DAO para roles
class RolDAO:
    def __init__(self):
        self.roles = RolDAO

    def get_all_roles(self):
        return [rol.__dict__ for rol in self.roles]


# DAO para estados
class EstadoDAO:
    def __init__(self):
        self.estados = EstadoDAO

    def get_all_estados(self):
        return [estado.__dict__ for estado in self.estados]


# DAO para códigos de verificación
class CodigoVerificacionDAO:
    def __init__(self):
        self.codigos_verificacion = CodigoVerificacionDAO

    def get_codigo_by_usuario_id(self, usuario_id):
        for codigo in self.codigos_verificacion:
            if codigo.usuario_id == usuario_id:
                return codigo.__dict__
        return None