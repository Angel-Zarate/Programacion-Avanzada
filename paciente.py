import random

class Paciente:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    peso = 0
    estatura = 0
    direccion = ""
    
    
    def __init__(self,nombre,ano_nacimiento,peso,estatura,direccion):
        self.id = random.randint(1,10001)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion
        
    def mostrar_informacion(self):
        print("Id: ", self.id)
        print(f"Nomre: {self.nombre}")
        print(f"Ano de nacimiento: {self.ano_nacimiento}")
        print(f"Estatura: {self.estatura}")
        print(f"Direccion: {self.direccion}")

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
    #     return self.peso

    # @property
    # def id(self):
    #     return self.estatura

    # @property
    # def id(self):
    #     return self.direccion
    
    