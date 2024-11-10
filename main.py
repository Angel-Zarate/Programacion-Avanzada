import tkinter as tk
from tienda.tienda import Tienda
from producto.producto import Producto
tiendita = Tienda()

def registrar_producto():
        nombre = str(entry_nombre.get())
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())

        producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
        tiendita.registrar_producto_tiendita(producto=producto)


#Formato a la ventana
ventana = tk.Tk()
ventana.title("Tiendita.exe")
ventana.geometry("500x600")
ventana.configure(background="#591C21")

label = tk.Label(ventana, text="Bienvenido a la tiendita", bg="#591C21", fg="black",font=("Arial",11,"bold"),padx=10,pady=10)
label.pack(padx=10,pady=10)

#Botón para mostrar productos
boton_productos = tk.Button(ventana, text="Mostrar Productos", bg="black", fg="white",font=("Arial",11,"bold"), command= tiendita.mostrar_productos)
boton_productos.pack(pady=10)

#Botón para calcular el costo de inventario
boton_costo = tk.Button(ventana, text="Calcular Costo de Inventario", bg="black", fg="white",font=("Arial",11,"bold"),command= tiendita.calcular_inventario)
boton_costo.pack(pady=10)

#Botón para registrar un nuevo producto

label = tk.Label(ventana, text="Nombre del producto", bg="#591C21", fg="black",font=("Arial",11,"bold"),padx=10,pady=10)
label.pack(padx=10,pady=10)

entry_nombre = tk.Entry(ventana, font=("Arial",12),bd=2)
entry_nombre.pack(padx=10, pady=10)

label = tk.Label(ventana, text="Costo del producto", bg="#591C21", fg="black",font=("Arial",11,"bold"),padx=10,pady=10)
label.pack(padx=10,pady=10)

entry_precio = tk.Entry(ventana, font=("Arial",12),bd=2)
entry_precio.pack(padx=10, pady=10)

label = tk.Label(ventana, text="Cantidad", bg="#591C21", fg="black",font=("Arial",11,"bold"),padx=10,pady=10)
label.pack(padx=10,pady=10)

entry_cantidad = tk.Entry(ventana,font=("Arial",12),bd=2)
entry_cantidad.pack(padx=10, pady=10)

boton_registro = tk.Button(ventana, text="Registrar Producto", bg="black", fg="white",font=("Arial",11,"bold"), command= registrar_producto)
boton_registro.pack(pady=10)

ventana.mainloop()