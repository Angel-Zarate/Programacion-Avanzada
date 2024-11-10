from producto.producto import Producto
from typing import List
import tkinter as tk
from tkinter import messagebox

class Tienda():
    productos: List[Producto] = []

    
    def mostrar_productos(self):
        try:
            for producto in self.productos:
                messagebox.showinfo("Productos", producto.mostrar_detalles())
        except:
            messagebox.showerror("Error","No existe producto en inventario")


    def calcular_inventario(self):
        for producto in self.productos:
            total = producto.calcular_valor_total()
            messagebox.showinfo("Inventario",f"El valor total que existe de {producto.nombre} es: {total}")
            
    
    def registrar_producto_tiendita(self,producto: Producto):
        try:
            self.productos.append(producto)
            messagebox.showinfo("Exito","Registro exitoso :)")
        except:
            messagebox.showerror("Error","Se ha cometido un error con los datos ingresados")