import random
from medico.medico import Medico
from paciente.paciente import Paciente

class Consulta:
    id: int
    fecha_hora: str
    consultorio: str
    medico: Medico
    paciente: Paciente
    
    def __init__(self,fecha_hora: str,consultorio: str,medico: Medico,paciente: Paciente):
        self.id = random.randint(1,10000)
        self.fecha_hora = fecha_hora
        self.consultorio = consultorio
        self.medico = medico
        self.paciente = paciente
        
        
    @property
    def id(self):
        return self.id
    
    @property
    def id(self):
        return self.fecha_hora
    
    @property
    def id(self):
        return self.consultorio
    
    @property
    def id(self):
        return self.medico
    
    @property
    def id(self):
        return self.paciente
    

