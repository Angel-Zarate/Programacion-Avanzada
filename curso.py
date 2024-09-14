class Curso:
    nombre_del_curso = ""
    codigo_curso = 0
    instructor = ""   
    
    #Metodo constructor
    def __init__(self,nombre_del_curso,codigo_curso,instructor):
        self.nombre_del_curso = nombre_del_curso
        self.codigo_curso = codigo_curso
        self.instructor = instructor
        
    #Metodos de la clase
    def mostrar_info_curso(self):
        print("\nInformacion del curso: ")
        print("Materia: ", self.nombre)
        print("Codigo del curso: ", self.codigo_curso)
        print("Maestro: ", self.instructor)
     
    
    