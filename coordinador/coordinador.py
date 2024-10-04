from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    sueldo: float
    rfc: str
    anos_antiguedad: int
    
    
    def __init__(self,sueldo: float,rfc: str,anos_antiguedad: int,numero_control: str,nombre: str,apellido: str, contrasenia: str):
        super.__init__(numero_control= numero_control,nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol= Rol.COORDINADOR)
        self.sueldo = sueldo
        self.rfc = rfc
        self.anos_antiguedad = anos_antiguedad