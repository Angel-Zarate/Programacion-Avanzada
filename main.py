from paciente.paciente import Paciente
from hospital.hospital import Hospital
from medico.medico import Medico

hospital = Hospital()

while True:
    print("\n**Bienvenido al sistema del hospital!**")
    print("1. Registrar Paciente")
    print("2. Registrar Medico")
    print("3. Mostrar Pacientes")
    print("4. Mostrar Medicos")
    print("5. Eliminar Pacientes")
    print("6. Eliminar Medicos")
    print("7. Mostrar pacientes menores de edad")
    print("8. Mostrar pacientes mayores de edad")
    print("9. Salir")
    
    opcion_usuario = input("\nSelecciona la opcion deseada: ")
    
    if opcion_usuario == "1":
        #Registrar Paciente
        print("Seleccionaste la opcion para registrar un paciente")
        
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
        peso = float(input("Ingresa el peso: "))
        estatura = float(input("Ingresa la estatura: "))
        direccion = input("Ingresa la direccion: ")
        
        paciente = Paciente(nombre=nombre,ano_nacimiento=ano_nacimiento,peso=peso,estatura=estatura,direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)
        
        print("Paciente registrado correctamente\n")
        pass
    
    elif opcion_usuario == "2":
        #Registrar medico
        print("Seleccionaste la opcion para registrar un medico")
        
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
        rfc = input("Ingresa el RFC: ")
        direccion = input("Ingresa la direccion: ")
        
        medico = Medico(nombre=nombre,ano_nacimiento=ano_nacimiento,rfc=rfc,direccion=direccion)
        hospital.registrar_medico(medico=medico)
        
        print("Medico registrado correctamente\n")
    
        
    elif opcion_usuario == "3":
        #Mostrar pacientes
        hospital.mostrar_pacientes()
        
    elif opcion_usuario=="4":
        #Mostrar medicos
        hospital.mostrar_medicos()
        
    elif opcion_usuario=="5":
        #Eliminar paciente
        hospital.eliminar_paciente()
        
    elif opcion_usuario=="6":
        #Eliminar medico
        hospital.eliminar_medico()
        
    elif opcion_usuario=="7":
        #Mostrar pacientes menores de edad
        hospital.pacientes_menores_edad()
        
    elif opcion_usuario=="8":
        #Mostrar pacientes mayores de edad
        hospital.pacientes_mayores_edad()
        
    elif opcion_usuario=="9":
        print("Hasta luego\n")
        break
        
    
    
    