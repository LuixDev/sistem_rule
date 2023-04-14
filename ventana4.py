import tkinter as tk
from PIL import Image, ImageTk

class Ventana4:
    def __init__(self, master):
        self.master = master
        self.master.title("Acerca")
        self.master.geometry("900x500")
        
        self.frame = tk.Frame(self.master)
        self.frame.config(bg="white")
        self.img1 = ImageTk.PhotoImage(Image.open("downloa.jpeg"))
        tk.Label(self.frame, image=self.img1).pack()
        
        self.frame.pack()
        
       
        self.label = tk.Label(self.frame, text="SISTEMA CARDIOVASCULAR", font=("Arial", 13), bg='#FFFFFF', fg='black' )
        self.label.pack()
        self.label1 = tk.Label(self.frame, text="INTEGRANTE:  William Alvarez, Kelvis Ariza, Jose Olascuaga,Luis Rodriguez  ", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label1.pack()
        self.label2 = tk.Label(self.frame, text="\n\nProyecto realizado con base a los sistemas expertos (SE), que son programas \ninformáticos que tienen el objetivo de solucionar un problema concreto y utilizan la Inteligencia Artificial (IA)\n para simular el razonamiento de un ser humano. se denominan sistemas expertos porque estos programas \nimitan la toma de decisiones de un profesional en la materia. ", font=("Arial", 11), bg='#FFFFFF', fg='black')
        self.label2.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana4(root)
    root.mainloop()
