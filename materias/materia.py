class Materia:
    # id: "MT{ultimos 2 digitos del nombre}{semestre}{cantidad creditos}{randit(1,)}"
    nombre: str
    descripcion: str
    semestre: int
    creditos: int
    numero_control: str
    
    def __init__(self,nombre: str,descripcion: str,semestre: int,creditos: int,numero_control: str):
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos 
        self.numero_control = numero_control
        
    def mostrar_info_materia(self):
        info = f"Numero de control de la materia: {self.numero_control}\n- Nombre de la materia: {self.nombre}\n- Descripcion de la materia: {self.descripcion}\n- Semestre: {self.semestre}\n- Creditos: {self.creditos}\n "
        return info