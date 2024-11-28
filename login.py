import tkinter as tk
from tkinter import messagebox
import mysql.connector
from crud_libros import ventanaEmpleados
from crud_usuarios import ventanaAdmin

def login():
    def verificar_usuario():
        user = entry_usuario.get()
        contrasena = entry_contrasena.get()
        
        try:
            conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'biblioteca'
            )
            
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s''',(user,contrasena))
            usuario = cursor.fetchone()
            
            if usuario:
                messagebox.showinfo("Login exitoso",f"Bienvenido {usuario[1]}")
                
                if usuario[5] == "Administrador":
                    ventanaAdmin(ventanaprincipal)
                
                else:
                    ventanaEmpleados(ventanaprincipal)
                
                
            else:
                messagebox.showerror("Error","Usuario o contraseña no encontrados.")
                
        except mysql.connector.Error as err:
            messagebox.showerror("Error de conexión",f"Error: {err}")
            
        finally:
            if conn.is_connected():
                conn.close()

    #Ventana 
    ventanaprincipal = tk.Tk()
    ventanaprincipal.title("Login")
    ventanaprincipal.geometry("300x200")

    #Entrada de correo
    label_usuario = tk.Label(ventanaprincipal, text = "Usuario")
    label_usuario.pack(pady=5)
    entry_usuario = tk.Entry(ventanaprincipal, width=30)
    entry_usuario.pack(pady=5)

    #Entrada de contraseña
    label_contraseña = tk.Label(ventanaprincipal, text = "Contraseña")
    label_contraseña.pack(pady=5)
    entry_contrasena = tk.Entry(ventanaprincipal,width=30, show="*")
    entry_contrasena.pack(pady=5)

    #Boton
    boton_login = tk.Button(ventanaprincipal,text="Login", command= verificar_usuario)
    boton_login.pack(pady=20)
    ventanaprincipal.mainloop()

login()