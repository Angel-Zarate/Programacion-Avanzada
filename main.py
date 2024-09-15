from paciente import Paciente
from hospital import Hospital
from medico import Medico

hospital = Hospital()


paciente = Paciente("Juan",2004,76,1.78,"Avenida Madero")
paciente_dos = Paciente("Messi",2008,100,1.50,"Avenida Madero")

medico = Medico("Alberto",1900,"SADF54SFDF","Av. Periodismo")
medico_dos = Medico("Manolo",1995,"SADF54S54G","Altozano")

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)
hospital.registrar_medico(medico=medico)
hospital.registrar_medico(medico=medico_dos)

hospital.mostrar_pacientes()
print("\n")
hospital.mostrar_medicos()
print("\n")
hospital.pacientes_menores_edad()
print("\n")
hospital.pacientes_mayores_edad()
print("\n")
hospital.eliminar_paciente()
print("\n")
hospital.eliminar_medico()