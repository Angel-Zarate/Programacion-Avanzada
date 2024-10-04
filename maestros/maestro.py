from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    rfc: str
    sueldo: float
    ano_nacimiento: int
    
    def __init__(self,rfc: str,sueldo: float,ano_nacimiento:int, nombre: str, apellido: str,numero_control:str,contrasenia: str):
        super.__init__(numero_control= numero_control, nombre= nombre, apellido= apellido, contrasenia= contrasenia, rol = Rol.MAESTRO)
        self.rfc = rfc
        self.sueldo = sueldo
        self.ano_nacimiento = ano_nacimiento
    
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"- Número de control: {self.numero_control}\n- Nombre completo: {nombre_completo}\n- RFC: {self.rfc}\n- Sueldo: {self.sueldo}\n- Año de nacimiento: {self.ano_nacimiento}\nRol: {self.rol.value}"
        return info
