import random

class Consulta:
    id = 0
    fecha_hora = ""
    consultorio = ""
    medico = ""
    paciente = ""
    
    def __init__(self,fecha_hora,consultorio,medico,paciente):
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
    

