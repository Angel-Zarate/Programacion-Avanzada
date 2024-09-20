from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
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
        numero_control = escuela.generar_numero_control()
        print(numero_control)
        
    
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa el curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano,mes,dia)
        
        
        
    elif opcion == "2":
        print("Seleccionaste la opcion para registrsar al maestro\n")
        
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa el RFC del maestro: ")
        sueldo = float(input("Ingresa el salario del maestro: "))
        
        maestro = Maestro(nombre=nombre,apellido=apellido,rfc=rfc,sueldo=sueldo)
        escuela.registrar_maestro(maestro=maestro)
        numero_control = escuela.numero_control_maestro()
        print(numero_control)

    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass 
    elif opcion == "6":
        print("Hasta luego\n")
        break