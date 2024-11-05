import tkinter as tk
from tkinter import messagebox
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multiplicacion = num1 * num2
        messagebox.showinfo("Resultado", f"La multiplicación es: {multiplicacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        division = num1 / num2
        messagebox.showinfo("Resultado", f"La division es: {division}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
 #Crea la ventana y le da formato
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("500x400")

#Agrega las funciones del boton numero 1 de la ventana
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)
 
#Agrega las funciones del boton numero 2 de la ventana
label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)
 
#Le coloca la funcion al boton de sumar
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=20)

#Le coloca la funcion al boton de restar
boton_restar = tk.Button(ventana, text="restar", command=restar)
boton_restar.pack(pady=20)

#Le coloca la funcion al boton de multiplicación
boton_multiplicar = tk.Button(ventana, text="multiplicar", command=multiplicar)
boton_multiplicar.pack(pady=20)

#Le coloca la funcion al boton de división
boton_dividir = tk.Button(ventana, text="dividir", command=dividir)
boton_dividir.pack(pady=20)

ventana.mainloop()