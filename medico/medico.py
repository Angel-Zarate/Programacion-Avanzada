import random

class Medico:
    id: int
    nombre: str
    ano_nacimiento: int
    rfc: str
    direccion: str
    
    def __init__(self,nombre: str,ano_nacimiento: int,rfc: str,direccion: str):
        self.id = random.randint(1,1000)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.direccion = direccion
        
    def mostrar_informacion(self):
        print("ID del medico: ",self.id)
        print("Nombre del medico: ", self.nombre)
        print("Ano de nacimiento: ", self.ano_nacimiento)
        print("RFC: ", self.rfc)
        print("Direccion del medico: ", self.direccion)
        
    # @property
    # def id(self):
    #     return self.id
    
    # @property
    # def id(self):
    #     return self.nombre
    
    # @property
    # def id(self):
    #     return self.ano_nacimiento
    
    # @property
    # def id(self):
    #     return self.direccion