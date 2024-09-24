from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint
import os

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_maeterias: List[Materia] = []
    
   
        
    def numero_control_estudiante(self):
            #L - 2024 - 09 - longitud lista estudiantes
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes)+1}{randint(0,10000)}"
            
        return numero_control
    
    def numero_control_materia(self, nombre,semestre,creditos):
        primeros_digitos = nombre[0:2].upper()
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
    
    def listar_estudiantes(self):
       print("** ESTUDIANTES **")
       for estudiante in self.lista_estudiantes:
           print(estudiante.mostrar_info_estudiante())
    
    def listar_maestros(self):
        print("** MAESTROS **\n")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())
    
    def listar_materias(self):
        print("** MATERIAS **\n")
        for materia in self.lista_maeterias:
            print(materia.mostrar_info_materia())
    
    def eliminar_estudiante(self,numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado exitosamente\n")
                return #Para que deje de buscar en la lista 
        print(f"No se encontro el estudiante con el numero de control: {numero_control}")  
    
    def eliminar_maestro(self,numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control:
                self.lista_maestros.remove(maestro)
                print("Maestro eliminado exitosamente\n")
                return
        print(f"No se encontro el maestro con el numero de control: {numero_control}")
        
    def eliminar_materia(self,numero_control: str):
        for materia in self.lista_maeterias:
            if materia.numero_control == numero_control:
                self.lista_maeterias.remove(materia)
                print("Materia eliminada exitosamente\n")
                return
        print(f"No se encontro la materia con el numero de control: {numero_control}")