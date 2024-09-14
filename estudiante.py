class Estudiante:
    id_estudiante = 0
    nombre = ""
    ano_nacimiento = 0
    cursos = []
    
    
    #Metodo constructor
    def __init__(self,id_estudiante,nombre,ano_nacimiento):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        
    #Metodos de la clase
    def agregar_curso(self,curso_agregado):
        self.cursos.append(curso_agregado)
    
            
    def mostrar_informacion(self):
        for curso in self.cursos:
            print("\n")
            print("Nombre de la materia: ", curso.nombre)
            print("Codigo de la materia: ", curso.codigo_curso)
            print("Nombre del maestro: ", curso.instructor)
        