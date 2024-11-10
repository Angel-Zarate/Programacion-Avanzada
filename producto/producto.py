
class Producto():
    nombre: str
    precio: float
    cantidad: int
    
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def calcular_valor_total(self):
        valor_total = self.cantidad * self.precio
        return valor_total
        
    def mostrar_detalles(self):
        info = f"-Nombre: {self.nombre}\n-Precio: {self.precio}\n-Cantidad: {self.cantidad}\n" 
        return info
    