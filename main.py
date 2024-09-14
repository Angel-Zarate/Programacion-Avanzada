from curso import Curso
from estudiante import Estudiante

estudiante = Estudiante()
curso = Curso()
#Instancias de Estudiante
estudiante_uno = Estudiante(1,"Jose Torres",2000)
estudiante_dos = Estudiante(2,"Chava Iglesias",2005)

#Instancias de Curso
curso_uno = Curso("Apreciacion al arte",435,"Agripino Solis")
curso_dos = Curso("Deportes",345,"Han Solo")
curso_tres = Curso("Ajedrez",342,"Juan Manuel")

estudiante.agregar_curso(curso_uno)
estudiante.agregar_curso(curso_dos)
estudiante.agregar_curso(curso_tres)

estudiante.mostrar_informacion(estudiante_uno,estudiante_dos)
