from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from datetime import datetime
from random import randint

import os

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_maeterias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List [Semestre] = []
   
        
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
    
    def registrar_carrera(self,carrera: Carrera):
        self.lista_carreras.append(carrera)
        
    def registrar_grupo(self,grupo: Grupo):
        id_semestre = grupo.id_semestre
        for semestre in self.lista_semestres:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break
        
        self.lista_grupos.append(grupo)

    def registrar_semestre(self,semestre: Semestre):
        id_carrera = semestre.id
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break
        self.lista_semestres.append(semestre)
            
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
    
    def listar_grupos(self):
        print("** GRUPOS **\n")
        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupo())
    
    def listar_semestres(self):
        print("** SEMESTRES **")
        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestre())

    def listar_carreras(self):
        print("** CARRERAS **")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carreras())
            
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