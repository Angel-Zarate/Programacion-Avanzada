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
    
   
        
    def numero_control_estudiante(self):
            #L - 2024 - 09 - longitud lista estudiantes
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes)+1}{randint(0,10000)}"
            
        return numero_control
    
    def numero_control_materia(nombre,semestre,creditos):
        primeros_digitos = nombre[0:2].upper
        numero_control = f"MT{primeros_digitos}{semestre}{creditos}{randint(1,1000)}"
        return numero_control
    
    def numero_control_maestro(self,nombre,rfc,ano_nacimiento):
        primeras_letras = nombre[0:2].upper()
        ultimos_digitos = rfc[-2:].upper()
       
        numero_control = f"M{ano_nacimiento}{datetime.now().day}{randint(500,5000)}{primeras_letras}{ultimos_digitos}{len(self.lista_maestros)+1}"
        return numero_control
    
    def registrar_estudiante(self,estudiante):
        self.lista_estudiantes.append(estudiante)
        print("Registro exitoso\n")
        
    def registrar_maestro(self,maestro):
        self.lista_maestros.append(maestro)
        print("Registro exitoso\n")        
        
    def registrar_materia(self,materia):
        self.lista_maeterias.append(materia)
        print("Registro exitoso\n")
    
   
    
        