import tkinter as tk
import ventana3
import ventana4

import ventana2 # Importamos el archivo de la Ventana 2
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Ventana1():
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("800x400")
        self.master.resizable(0, 0)
        self.frame = tk.Frame(self.master)
        self.frame.config(bg="white")
       
        self.frame.place(x=0, y=0, width=800, height=400)
        self.img = ImageTk.PhotoImage(Image.open("downloa.jpeg"))
        tk.Label(self.frame, image=self.img).place(x=50, y=50)
        self.label1 = tk.Label(self.frame, text="Usuario", font=("Arial", 13), bg='#FFFFFF', fg='black', width=10, height=2)
        self.label1.place(x=450, y=90)
        self.caja01 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja01.place(x=560, y=95)
        self.label2 = tk.Label(self.frame, text="Contraseña", font=("Arial", 13), bg='#FFFFFF', fg='black', width=10, height=2)
        self.label2.place(x=450, y=150)
        self.caja02 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja02.place(x=560, y=150)
        
        self.button = tk.Button(self.frame, text="Aceptar", command=self.login)
        self.button.place(x=620,y=230)
        self.button2 = tk.Button(self.frame, text="Registrar", command=self.insertar)
        self.button2.place(x=680,y=230)



    def open_ventana2(self):
        # Creamos una instancia de la Ventana 2 y la mostramos
        self.new_window = tk.Toplevel(self.master)
        self.app = ventana2.Ventana2(self.new_window)
    
    def open_ventana3(self):
        self.app = ventana3.Ventana3(self.master)
       
    
    def open_ventana4(self):
        
        self.new_window = tk.Toplevel(self.master)
        self.app = ventana4.Ventana4(self.new_window)
    

    def insertar(self):
    
        
        # Conexión a la base de datos
        conexion = mysql.connector.connect(host='127.0.0.1', user='root', passwd='', db='sistema')
        cursor = conexion.cursor()
        
        # Recuperar los valores de la caja01 y caja02
        usuario = self.caja01.get()
        contrasena = self.caja02.get()
        
        # Consulta SQL para insertar un nuevo usuario y contraseña en la tabla de usuarios
        sql = "INSERT INTO usuario (usuario, contraseña) VALUES (%s, %s)"
        
        # Tupla con los valores de usuario y contraseña
        valores = (usuario, contrasena)
        
        # Ejecutar la consulta y confirmar los cambios en la base de datos
        cursor.execute(sql, valores)
        conexion.commit()
        
        # Cerrar la conexión a la base de datos
        cursor.close()
        conexion.close()
       
        messagebox.showinfo("Registro guardado", "se ha guadado en la base de dato.")



  
    def login(self):

        conexion = mysql.connector.connect(host='127.0.0.1', user='root', passwd='', db='sistema')
        cur = conexion.cursor()
        user = self.caja01.get()
        contr = self.caja02.get()

        cur.execute("select * from usuario where usuario='" + user + "' and contraseña='" + contr + "' ")
        if cur.fetchall():
            messagebox.showinfo(title="Login correcto", message="Usuario y contraseña correctos")
            
            global img1
            root = tk.Toplevel()
            root.geometry("800x400")
            root.title("Ventana principal")
            barraMenu = tk.Menu(root)
            
            img1 = ImageTk.PhotoImage(Image.open("img.jpeg"))
            tk.Label(root, image=img1).place(x=0, y=0)
            
            root.config(menu=barraMenu, width=300, height=300)

    

            barraMenu.add_cascade(label="Diagnosticar", command=self.open_ventana2)#acomodo los elementos en el menú
            barraMenu.add_cascade(label="Visualizar ", command=self.open_ventana3)
            barraMenu.add_cascade(label="Acerca de ",command=self.open_ventana4)
            boton2 = tk.Button(root, text="Salir", command=root.quit, bg='red', fg='white')
            boton2.configure(width=15, height=4)
            boton2.place(x=620,y=230)
            
            miFrame =tk.Frame(root)
            miFrame.pack()
   
        

if __name__ == "__main__":
    root = tk.Tk()
    
    app = Ventana1(root)
    root.mainloop()
