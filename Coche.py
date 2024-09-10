class coche:
    marca = ""
    modelo = ""
    año = 0
    
    
    #Metodo Constructivo
    def __init__ (self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
        
    #Primer Metodo
    def mostrar_informacion(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Ano: ", self.año)