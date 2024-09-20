from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_maeterias: List[Materia] = []
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        
    def generar_numero_control(self):
            #L - 2024 - 09 - longitud lista estudiantes
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes)+1}{randint(0,10000)}"
            
        return numero_control
    
    def registrar_maestro(self,maestro):
        self.lista_maestros.append(maestro)
        print("Registro exitoso\n")        
    
    def numero_control_maestro(self):
        for maestro in self.lista_maestros():
            if len(maestro) == 1 or len(maestro) == 2:
                primeras_letras = len(maestro)
            
        numero_control = f"M{datetime.now().day}{randint(500,5000)}{primeras_letras}{len(self.lista_maestros)+1}"
        return numero_control
        