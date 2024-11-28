import tkinter as tk
import mysql.connector
from tkinter import ttk,messagebox
from tkinter import *

def ventanaEmpleados(ventanaprincipal):
    ventanaprincipal.withdraw()
    def mostrar():
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password ="",database = "biblioteca")
        micursor = mysqlC.cursor()
        micursor.execute("select * from libros")
        lista = micursor.fetchall()
        
        for i,(id,titulo,autor,editorial,anio,precio) in enumerate(lista,start=1):
            listbox.insert("","end",values=(id, titulo, autor, editorial,anio,precio))
            mysqlC.close()
            
    def add():
        tituloAdd =tittle.get()
        autorAdd = author.get()
        editAdd = editorial.get()
        idAdd = identificador.get()
        anioAdd = year.get()
        precioAdd = price.get()
        mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="biblioteca")
        micursor= mysqlC.cursor()
        try:
            micursor.execute(f"insert into libros (id,titulo,autor,editorial,año_publicacion,precio) values({idAdd},'{tituloAdd}','{autorAdd}','{editAdd}','{anioAdd}','{precioAdd}')")
            mysqlC.commit()
            tittle.delete(0,END)
            author.delete(0,END)
            editorial.delete(0,END)
            year.delete(0,END)
            price.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("informacion","Libro agregado")
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
        tituloAdd =tittle.get()
        autorAdd = author.get()
        editAdd = editorial.get()
        idAdd = identificador.get()
        anioAdd = year.get()
        precioAdd = price.get()
    
        mysqlC = mysql.connector.connect(host ="localhost",user = "root", password = "",database ="biblioteca")
        micursor= mysqlC.cursor()
        
        try:
            micursor.execute(f"UPDATE libros set titulo = '{tituloAdd}',autor = '{autorAdd}',editorial = '{editAdd}',año_publicacion = '{anioAdd}',precio = '{precioAdd}' where id={idAdd}")
            mysqlC.commit()
            tittle.delete(0,END)
            author.delete(0,END)
            editorial.delete(0,END)
            year.delete(0,END)
            price.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("informacion","Libro editado")
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
            micursor.execute(f"DELETE FROM LIBROS WHERE id ={idAdd}")
            mysqlC.commit()
            tittle.delete(0,END)
            author.delete(0,END)
            editorial.delete(0,END)
            year.delete(0,END)
            price.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("informacion","Libro eliminado")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        
    def obtenerR(event):
        tittle.delete(0,END)
        author.delete(0,END)
        editorial.delete(0,END)
        year.delete(0,END)
        price.delete(0,END)
        identificador.delete(0,END)
        
        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0,seleccion["ID"])
        tittle.insert(0,seleccion["Titulo"])
        author.insert(0,seleccion["Autor"])
        editorial.insert(0,seleccion["Editorial"])
        year.insert(0,seleccion["Año"])
        price.insert(0,seleccion["Precio"])
    
    def filtrar():
        filtroAdd = yearfilter.get()
        mysqlC = mysql.connector.connect(host ="localhost",user = "root", password = "",database = "biblioteca")
        micursor= mysqlC.cursor()
        micursor.execute(f"SELECT * FROM libros WHERE año_publicacion = '{filtroAdd}'")
        filtrado = micursor.fetchall()
        
        if filtrado:
            for i,(id,titulo,autor,editorial,anio,precio) in enumerate(filtrado,start=0):
                messagebox.showinfo("Busquda Exitosa",f"El libro {titulo} hecho por {autor}, por la editorial {editorial}, del año {anio}, tiene el precio de {precio}")
                yearfilter.delete(0,END)
                mysqlC.close()
                
        else:
            messagebox.showerror("Error","El año ingresado no conicide con los existentes, vuelve a intentarlo")
            mysqlC.close()
            
    def regresar():
        root.destroy()
        ventanaprincipal.deiconify()  


        
    root = tk.Toplevel(ventanaprincipal)
    root.title("Libreria")
    root.geometry("1200x500")
    root.configure(background="#D96941")
    label1 = tk.Label(root,text="Registro de Libros", fg = "#A62B1F", font=("Bahnschrift",28),bg="#D96941").place(x=170,y=0)

    global tittle
    global author
    global identificador
    global price
    global editorial 
    global year

    labelid = tk.Label(root, text= "ID", font =("Georgia",12),bg="#D96941")
    labelid.place(x=100,y=50)

    labeltitulo = tk.Label(root, text="Título",font = ("Gerogia",12),bg="#D96941")
    labeltitulo.place(x=100,y=80)

    labelautor = tk.Label(root, text= "Autor", font =("Georgia",12),bg="#D96941")
    labelautor.place(x=100,y=110)

    labeleditorial = tk.Label(root, text= "Editorial", font =("Georgia",12),bg="#D96941")
    labeleditorial.place(x=100,y=140)

    labelanio = tk.Label(root, text= "Año", font =("Georgia",12),bg="#D96941")
    labelanio.place(x=100,y=170)

    labelprecio = tk.Label(root, text= "Precio", font =("Georgia",12),bg="#D96941")
    labelprecio.place(x=100,y=200)
    
    labelfiltrar = tk.Label(root, text="Filtrar por año", font=("Georgia",12),bg="#D96941")
    labelfiltrar.place(x=500,y=50)

    identificador = tk.Entry(root)
    identificador.place(x=200, y=50)

    tittle = tk.Entry(root)
    tittle.place(x=200, y=80)

    author = tk.Entry(root)
    author.place(x=200, y=110)

    editorial = tk.Entry(root)
    editorial.place(x=200, y=140)

    year = tk.Entry(root)
    year.place(x=200,y=170)

    price = tk.Entry(root)
    price.place(x=200,y=200)
    
    yearfilter = tk.Entry(root)
    yearfilter.place(x=630,y=50)
    

    tk.Button(root,text="Crear",command=add, height=3, width=8,font=("Haettenschweiler",12),bg="#193C40",fg="White").place(x=100,y=250)
    tk.Button(root,text= "Editar",command=edit, height=3, width=8, font=("Haettenschweiler",12),bg="#193C40",fg="White").place(x=250,y=250)
    tk.Button(root, text="Eliminar",command=delete, height= 3, width=8, font=("Haettenschweiler",12),bg="#193C40",fg="White").place(x=400,y=250)
    tk.Button(root,text="Filtrar",command=filtrar,height=3,width=8,font=("Haettenschweiler",12),bg="#193C40",fg="White").place(x=550,y=250)
    tk.Button(root, text="Regresar",command=regresar, height=3, width=8, font=("Haettenschweiler",12),fg="White",bg="#193C40").place(x=700,y=250)

    columnas = ("ID","Titulo","Autor","Editorial","Año","Precio")
    listbox = ttk.Treeview(root,columns = columnas,show="headings")

    for col in columnas:
        listbox.heading(col, text= col)
        listbox.grid(row=1,column=0,columnspan=1)
        listbox.place(x=0,y=400)
        
    mostrar()
    listbox.bind("<Double-Button-1>",obtenerR)
    root.mainloop()

