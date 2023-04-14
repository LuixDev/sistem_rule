import tkinter as tk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from sistemadereglas import *
from random import choice




class Ventana2:
    def __init__(self, master):
        self.master = master
        self.master.title("Diagnosticar")
        self.master.geometry("1100x600")
        self.frame = tk.Frame(self.master)
        self.frame.config(bg="white")
       
        self.frame.place(x=0, y=0, width=1100, height=600)
        self.img = ImageTk.PhotoImage(Image.open("img.jpeg"))
        tk.Label(self.frame, image=self.img).place(x=50, y=50)
        
        self.labe1 = tk.Label(self.frame, text="Sistema cadiovascular responde si o no la siguente pregunta", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.labe1.place(x=460, y=50)

        self.label1 = tk.Label(self.frame, text=" ¿Siente dolor en el pecho?", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label1.place(x=460, y=150)
        self.caja01 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja01.place(x=680, y=150)
        
        self.label2 = tk.Label(self.frame, text="¿Sufre desmayos?", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label2.place(x=480, y=200)
        self.caja02 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja02.place(x=650, y=200)
        
        
        self.label3 = tk.Label(self.frame, text=" ¿Siente latidos irregulares en el corazón?", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label3.place(x=450, y=250)
        self.caja03 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja03.place(x=780, y=255)
        
        
        self.label4 = tk.Label(self.frame, text=" ¿Se siente con falta de aire?", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label4.place(x=450, y=300)
        self.caja04 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja04.place(x=700, y=305)
        
        
        self.label5 = tk.Label(self.frame, text=" ¿Se inflaman sus pies o tobillos?", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label5.place(x=450, y=350)
        self.caja05 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja05.place(x=730, y=355)
        self.engine = sistemadereglas()
        self.engine.reset()

    
        v_dolorpecho = self.caja01.get()
        self.engine.declare(reglas(dolorpecho=choice([str(v_dolorpecho)])))
     


        v_desmayos = self.caja02.get()
        self.engine.declare(reglas(desmayo=choice([str(v_desmayos)])))
       


        v_latidoscorazon = self.caja03.get()
        self.engine.declare(reglas(latidoscorazon=choice([str(v_latidoscorazon)])))
    

        v_faltadeaire = self.caja04.get()
        self.engine.declare(reglas(faltadeaire=choice([str(v_faltadeaire)])))
        


        v_hinchazonpies = self.caja05.get()
        self.engine.declare(reglas(hinchazonpies=choice([str(v_hinchazonpies)])))
        self.engine.run()



    
        self.button = tk.Button(self.frame, text="Guardar dato" , command=lambda: guardar_registro(self, self.caja01.get(),self.caja02.get(),self.caja03.get(),self.caja04.get(),self.caja05.get()))
        self.button.place(x=700,y=530)


        
        self.button1 = tk.Button(self.frame, text="Diagnosticar" , command=lambda: make_diagnosis(self, self.caja01.get(),self.caja02.get(),self.caja03.get(),self.caja04.get(),self.caja05.get()))
        self.button1.place(x=500,y=530)


def make_diagnosis(self,dolorpecho, desmayo, latidoscorazon, faltadeaire, hinchazonpies):
    engine = sistemadereglas()
    engine.reset()

    engine.declare(reglas(dolorpecho=choice([dolorpecho])))
    engine.declare(reglas(desmayo=choice([desmayo])))
    engine.declare(reglas(latidoscorazon=choice([latidoscorazon])))
    engine.declare(reglas(faltadeaire=choice([faltadeaire])))
    engine.declare(reglas(hinchazonpies=choice([hinchazonpies])))

    engine.run()

    # Return the diagnosis
    return 



def guardar_registro(ventana, columna1,columna2,columna3,columna4,columna5):
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistema'
    )

    # Crear un cursor para realizar operaciones en la base de datos
    cursor = conexion.cursor()

    # Insertar los datos en la tabla correspondiente
   
    consulta = "INSERT INTO `preguntas` (`Presenta usted dolor en el pecho`, `Sufre desmayos`, `Siente latidos irregulares en el corazón`, `Se siente con falta de aire`, `inflamacion en pies o tobillos`) VALUES (%s,%s,%s,%s,%s)"

    valores = (columna1,columna2,columna3,columna4,columna5)
    cursor.execute(consulta, valores)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión y el cursor
    cursor.close()
    conexion.close()

    messagebox.showinfo("Registro guardado", "se ha guadado en la base de dato.")






      
if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana2(root)
    root.mainloop()
