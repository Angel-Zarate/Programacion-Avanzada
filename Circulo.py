import math

class circle:
    Radio: 0
    
    #Constructor 
    def __init__(self,Radio):
        self.Radio = Radio
        
    #Metodo para calcular area
    def calcular_area(self):
        area = math.pi * pow(self.Radio,2)
        print("Area del circulo: "+ str(area))
        # print("\n")
        
    #Metodo para calcular el perimetro
    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.Radio 
        print("Perimetro del circulo: "+str(perimetro))
        # print("\n")
