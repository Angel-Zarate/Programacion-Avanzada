from typing import List
from paciente.paciente import Paciente
from medico.medico import Medico
from consulta.consulta import Consulta


class Hospital:
    pacientes: List[Paciente] = []
    medicos: List[Medico] = []
    consultas: List[Consulta] = []

    def registrar_consulta(self,id_paciente,id_medico):
        if not self.validar_cantidad_usuarios():
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el medico o el pacinete")
            return
        print("Continuamos con el registro\n")
    
    def pacientes_menores_edad(self):
        print("Pacientes menores de edad: ")
        for paciente in self.pacientes:
            if paciente.ano_nacimiento > 2006:
                print(paciente.mostrar_informacion())
            
                
    def pacientes_mayores_edad(self):
        print("Pacientes mayores de edad: ")
        for paciente in self.pacientes:
            if paciente.ano_nacimiento < 2006:
                print(paciente.mostrar_informacion())
    
    def eliminar_paciente(self):
        print("Para eliminar, coloque el ID de un paciente")
        eleccion = int(input("Observe el ID que contiene cada uno: "))
        for paciente in self.pacientes:
            if eleccion == paciente.id:
                self.pacientes.remove(paciente)
                print("\nSe ha eliminado con exito")
                print("\nPacientes en elsistema:")
                for paciente in self.pacientes:
                    paciente.mostrar_informacion()
                    print("\n")
                return True
        print("\nLo sentimos, el ID que ha ingresado es erroneo")
        return False
    
    def eliminar_medico(self):
        print("\nPara eliminar, coloque el ID de un medico en el sistema")
        eleccion = int(input("Observe el ID que contiene cada uno: "))
        for medico in self.medicos:
            if eleccion == medico.id:
                self.medicos.remove(medico)
                print("\nSe ha eliminado con exito")
                print("\nMedicos en sistema:")
                for medico in self.medicos:
                    medico.mostrar_informacion()
                    print("\n")
                return True
        print("\nLo sentimos, el ID que ha ingresado es erroneo")
        return False
        
    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
           if paciente.id == id_paciente: 
               return True
           
        return False 
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
        
        return False
        
    def mostrar_pacientes(self):
        print("*** Pacientes en el sistema ***")
        for paciente in self.pacientes:
            # print("Id: ", paciente.id)
            # print(f"Nomre: {paciente.nombre}")
            # print(f"Año de nacimiento: {paciente.ano_nacimiento}")
            # print(f"Estatura: {paciente.estatura}")
            # print(f"Direccion: {paciente.direccion}")
            paciente.mostrar_informacion()
            print("\n")
            
    def mostrar_medicos(self):
        print("*** Medicos en el sistema ***")
        for medico in self.medicos:
            medico.mostrar_informacion()
            print("\n")
    
    def registrar_paciente(self,paciente):
        self.pacientes.append(paciente)
        
    def registrar_medico(self,medico):
        self.medicos.append(medico)
        
    def validar_cantidad_usuarios(self):
        if(len(self.pacientes)==0):
            print("No puedes registrar consulta, no existen pacientes")
            return False

        elif(len(self.medicos)==0):
            print("No puedes registrar consulta, no existen medicos")
            return False
        return True