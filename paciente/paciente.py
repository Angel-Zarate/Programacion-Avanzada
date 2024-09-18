import random

class Paciente:
    id: int
    nombre: str
    ano_nacimiento: int
    peso: float
    estatura: float
    direccion: str
    
    
    def __init__(self,nombre: str,ano_nacimiento: int,peso: float,estatura: float,direccion: str):
        self.id = random.randint(1,10001)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion
        
    def mostrar_informacion(self) -> None:
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
    
    