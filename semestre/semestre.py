from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint

class Semestre:
    id: str
    numero: int
    id_carrera: str
    materias: List[Materia]
    grupos: List[Grupo]
    
    def __init__(self, numero: int, id_carrera: str):
        self.id = self.generar_id(numero)
        self.numero = numero
        self.id_carrera = id_carrera
        
    def generar_id(self,numero_semestre: int) -> str :
        return f"{numero_semestre}-{randint(0,10000)}-{randint(0,10000)}"
    
    def registrar_grupo_en_semestre(self, grupo: Grupo):
        self.grupos.append(grupo)
        
    def mostrar_info_semestre(self):
        info = f"- ID: {self.id}\n- Numero: {self.numero}\n- ID Carrera: {self.id_carrera}"
        return info