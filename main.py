from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia
escuela = Escuela()

while True:
    print("** MINDBOX **\n")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Salir")
    
    opcion = input("\nIngresa una opcion para continuar: ")

    
    if opcion == "1":
        print("Seleccionaste la opcion para registrsar al estudiante\n")

        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano,mes,dia)       
        
        numero_control = escuela.numero_control_estudiante()
        print(numero_control)
        
        estudiante = Estudiante(nombre=nombre,apellido=apellido,curp=curp, fecha_nacimiento=fecha_nacimiento) 
        
    elif opcion == "2":
        print("Seleccionaste la opcion para registrsar al maestro\n")
        
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
        print("Seleccionaste la opcion para registrsar materia\n")
        
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripcion de la materia: ")
        semestre = int(input("Ingresa el semestre de la materia: "))
        creditos = int(input("Ingresa el numero de creditos de la materia: "))
    
        numero_control = escuela.numero_control_materia(nombre=nombre,semestre=semestre,creditos=creditos)
        print(f"Numero de control: {numero_control}")
        
        materia = Materia(nombre=nombre,descripcion=descripcion,semestre=semestre,creditos=creditos,numero_control=numero_control)
        escuela.registrar_materia(materia=materia)
       
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass 
    elif opcion == "6":
        print("Hasta luego\n")
        break