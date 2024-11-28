import tkinter as tk
import mysql.connector
from tkinter import ttk,messagebox
from tkinter import *

def ventanaAdmin(ventanaprincipal):
    ventanaprincipal.withdraw()

    def mostrar():
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password ="",database = "biblioteca")
        micursor = mysqlC.cursor()
        micursor.execute("select * from usuarios")
        lista = micursor.fetchall()
        
        for i,(id,nombre,apellido,usuario,contrasena,rol) in enumerate(lista,start=1):
            listbox.insert("","end",values=(id, nombre, apellido, usuario,contrasena,rol))
            mysqlC.close()
            
    def add():
        idAdd = identificador.get()
        nombreAdd =name.get()
        apellidoAdd = lastname.get()
        usuarioAdd = user.get()
        contraAdd = password.get()
        rolAdd = rol.get()
        mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
        micursor= mysqlC.cursor()
        try:
            micursor.execute(f"INSERT INTO usuarios(id, nombre, apellido, usuario, contraseña, rol) values({idAdd},'{nombreAdd}','{apellidoAdd}','{usuarioAdd}','{contraAdd}','{rolAdd}')")
            mysqlC.commit()
            name.delete(0,END)
            lastname.delete(0,END)
            user.delete(0,END)
            password.delete(0,END)
            rol.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("informacion","usuario agregado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()

    def edit():
        idAdd = identificador.get()
        nombreAdd =name.get()
        apellidoAdd = lastname.get()
        usuarioAdd = user.get()
        contraAdd = password.get()
        rolAdd = rol.get()

        mysqlC = mysql.connector.connect(host ="localhost",user = "root", password = "",database ="biblioteca")
        micursor= mysqlC.cursor()
        
        try:
            micursor.execute(f"UPDATE usuarios set nombre = '{nombreAdd}',apellido = '{apellidoAdd}',usuario = '{usuarioAdd}',contraseña = '{contraAdd}',rol = '{rolAdd}' where id={idAdd}")
            mysqlC.commit()
            name.delete(0,END)
            lastname.delete(0,END)
            user.delete(0,END)
            password.delete(0,END)
            rol.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("informacion","usuario editado")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
            
    def delete():
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host="localhost",user= "root", password= "",database = "biblioteca")
        micursor = mysqlC.cursor()
        
        try:
            micursor.execute(f"DELETE FROM USUARIOS WHERE id ={idAdd}")
            mysqlC.commit()
            name.delete(0,END)
            lastname.delete(0,END)
            user.delete(0,END)
            password.delete(0,END)
            rol.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("informacion","usuario eliminado")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        
    def obtenerR(event):
        name.delete(0,END)
        lastname.delete(0,END)
        user.delete(0,END)
        password.delete(0,END)
        rol.delete(0,END)
        identificador.delete(0,END)
        
        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0,seleccion["ID"])
        name.insert(0,seleccion["Nombre"])
        lastname.insert(0,seleccion["Apellido"])
        user.insert(0,seleccion["Usuario"])
        password.insert(0,seleccion["Contraseña"])
        rol.insert(0,seleccion["Rol"])

    def regresar():
        root.destroy()
        ventanaprincipal.deiconify()
        
    global name
    global password
    global identificador
    global lastname
    global user 
    global rol
    
    root = tk.Toplevel(ventanaprincipal)
    root.title("Ventana Administrador")
    root.configure(background="#5C8EF2")

    root.geometry("1200x500")
    label1 = tk.Label(root,text="Registro de usuarios", fg = "#F26716", font=("Bahnschrift",28),bg="#5C8EF2").place(x=170,y=0)
    
    
    labelid = tk.Label(root, text= "ID", font =("Georgia",12),bg="#5C8EF2")
    labelid.place(x=100,y=50)

    labelnombre = tk.Label(root, text="Nombre",font = ("Georgia",12),bg="#5C8EF2")
    labelnombre.place(x=100,y=80)

    labelapellido = tk.Label(root, text= "Apellido", font =("Georgia",12),bg="#5C8EF2")
    labelapellido.place(x=100,y=110)

    labelusuario = tk.Label(root, text= "Usuario", font =("Georgia",12),bg="#5C8EF2")
    labelusuario.place(x=100,y=140)

    labelcontrasena = tk.Label(root, text= "Contraseña", font =("Georgia",12),bg="#5C8EF2")
    labelcontrasena.place(x=100,y=170)

    labelrol = tk.Label(root, text= "Rol", font =("Georgia",12),bg="#5C8EF2")
    labelrol.place(x=100,y=200)

    identificador = tk.Entry(root)
    identificador.place(x=200, y=50)

    name = tk.Entry(root)
    name.place(x=200, y=80)

    lastname = tk.Entry(root)
    lastname.place(x=200, y=110)

    user = tk.Entry(root)
    user.place(x=200, y=140)

    password = tk.Entry(root)
    password.place(x=200,y=170)

    rol = tk.Entry(root)
    rol.place(x=200,y=200)

    tk.Button(root,text="Crear",command=add, height=3, width=8,font=("Haettenschweiler",12),bg="#262626",fg="white").place(x=100,y=250)
    tk.Button(root,text= "Editar",command=edit, height=3, width=8, font=("Haettenschweiler",12),bg="#262626",fg="white").place(x=250,y=250)
    tk.Button(root, text="Eliminar",command=delete, height= 3, width=8, font=("Haettenschweiler",12),bg="#262626",fg="white").place(x=400,y=250)
    tk.Button(root, text="Regresar",command=regresar, height=3, width=8, font=("Haettenschweiler",12),fg="White",bg="#262626").place(x=550,y=250)
    
    columnas = ("ID","Nombre","Apellido","Usuario","Contraseña","Rol")
    listbox = ttk.Treeview(root,columns = columnas,show="headings")

    for col in columnas:
        listbox.heading(col, text= col)
        listbox.grid(row=1,column=0,columnspan=1)
        listbox.place(x=0,y=400)
        
    mostrar()
    listbox.bind("<Double-Button-1>",obtenerR)
    root.mainloop()



