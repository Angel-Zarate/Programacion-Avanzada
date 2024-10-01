from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from grupos.grupo import Grupo
import os
escuela = Escuela()

while True:
    print("** MINDBOX **\n")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")   
    print("6. Registrar carrera")
    print("7. Registrar semestre")
    print("8. Mostrar estudiantes")
    print("9. Mostrar maestros")
    print("10. Mostrar materias")
    print("11. Mostrar grupos")
    print("12. Mostrar semestres")
    print("13. Mostrar carreras")
    print("14. Eliminar estudiante")
    print("15. Eliminar maestro") 
    print("16. Eliminar materia") 
    print("17. Salir")
    
    opcion = input("\nIngresa una opcion para continuar: ")
    
    if opcion == "1":
        print("\nSeleccionaste la opcion para registrar al estudiante\n")
        
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano,mes,dia)       
        
        numero_control = escuela.numero_control_estudiante()
        print(f"Numero de control: {numero_control}")
        
        estudiante = Estudiante(numero_control=numero_control,nombre=nombre,apellido=apellido,curp=curp, fecha_nacimiento=fecha_nacimiento)
        escuela.registrar_estudiante(estudiante=estudiante) 
    
    elif opcion == "2":
        print("\nSeleccionaste la opcion para registrar al maestro\n")
        
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa el RFC del maestro: ")
        sueldo = float(input("Ingresa el salario del maestro: "))
        ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
    
        numero_control = escuela.numero_control_maestro(nombre=nombre,rfc=rfc,ano_nacimiento=ano_nacimiento)
        print(f"Numero de control: {numero_control}")
        
        maestro = Maestro(nombre=nombre,apellido=apellido,rfc=rfc,sueldo=sueldo,ano_nacimiento=ano_nacimiento,numero_control=numero_control)
        escuela.registrar_maestro(maestro=maestro)

    elif opcion == "3":
        print("\nSeleccionaste la opcion para registrar materia\n")
        
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripcion de la materia: ")
        semestre = int(input("Ingresa el semestre de la materia: "))
        creditos = int(input("Ingresa el numero de creditos de la materia: "))
    
        numero_control = escuela.numero_control_materia(nombre=nombre,semestre=semestre,creditos=creditos)
        print(f"Numero de control: {numero_control}")
        
        materia = Materia(nombre=nombre,descripcion=descripcion,semestre=semestre,creditos=creditos,numero_control=numero_control)
        escuela.registrar_materia(materia=materia)
       
    elif opcion == "4":
        print("\nSeleccionaste la opcion para registrar un nuevo grupo\n")
        tipo = input("Ingresa el tipo de grupo (A/B): ")
        id_semestre = input("Ingresa el ID del semestre al que pertenece el grupo: ")
        
        grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
        escuela.registrar_grupo(grupo=grupo)
        
    elif opcion == "5":
        pass #Registro horario
    
    elif opcion == "6":
        print("\nSeleccionaste la opcion para registrar una carrera\n")
        nombre = input("Ingresa el nombre de la carrera: ")
        carrera = Carrera(nombre=nombre)
        escuela.registrar_carrera(carrera=carrera)
        
    elif opcion == "7":
        print("Seleccionaste la opcion para registrar un semestre ")
        numero = int(input("Ingresa el numero del semestre: "))
        id_carrera = input("Ingresa el ID de la carrera: ")
        semestre = Semestre(numero=numero, id_carrera= id_carrera)
        escuela.registrar_semestre(semestre=semestre)
        
    elif opcion == "8":
        escuela.listar_estudiantes()
    
    elif opcion == "9":
        escuela.listar_maestros()
        
    elif opcion == "10":
        escuela.listar_materias()
    
    elif opcion == "11":
        escuela.listar_grupos()
    
    elif opcion == "12":
        escuela.listar_semestres()
    
    elif opcion == "13":
        escuela.listar_carreras()
        
    elif opcion == "14":
        print("\nSeleccionaste la opcion para eliminar a un estudiante\n")
        numero_control = input("Ingresa el numero de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control=numero_control)
    
    elif opcion == "15":
        print("\nSeleccionaste la opcion para eliminar un maestro\n")
        numero_control = input("Ingresa el numero de control del maestro: ")
        escuela.eliminar_maestro(numero_control=numero_control)

    elif opcion == "16":
        print("\nSeleccionaste la opcion para eliminar una materia\n")
        numero_control = input("Ingresa el numero de control de la materia: ")
        escuela.eliminar_materia(numero_control=numero_control)
   
    elif opcion == "17":
        print("Hasta luego\n")
        break