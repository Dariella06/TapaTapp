import DatosServidor as dades
from DatosServidor import Usuario, Niño, Tratamiento, Estado, CodigoVerificacion

class UsuarioDAO:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def get_todos_usuarios(self):
        return [usuario.__dict__ for usuario in self.usuarios]

    def get_usuario_por_email(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario.__dict__
        return None

class NiñoDAO:
    def __init__(self, niños, relaciones):
        self.niños = niños
        self.relaciones = relaciones

    def get_todos_niños(self):
        return [niño.__dict__ for niño in self.niños]

    def get_niños_por_usuario(self, usuario_id):
        ids = [rel["niño_id"] for rel in self.relaciones if rel["usuario_id"] == usuario_id]
        return [niño.__dict__ for niño in self.niños if niño.id in ids]

class TratamientoDAO:
    def __init__(self, tratamientos):
        self.tratamientos = tratamientos

    def get_todos_tratamientos(self):
        return [tratamiento.__dict__ for tratamiento in self.tratamientos]

class EstadoDAO:
    def __init__(self, estados):
        self.estados = estados

    def get_todos_estados(self):
        return [estado.__dict__ for estado in self.estados]

class CodigoVerificacionDAO:
    def __init__(self, codigos):
        self.codigos = codigos

    def get_codigo_por_usuario(self, usuario_id):
        for codigo in self.codigos:
            if codigo.usuario_id == usuario_id:
                return codigo.__dict__
        return None
