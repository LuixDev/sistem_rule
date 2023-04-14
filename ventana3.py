import mysql.connector
import tkinter as tk
from tkinter import ttk

class Ventana3:
    def __init__(self,master):
        # Conexión a la base de datos
        self.conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="sistema"
        )

        # Crear una consulta SQL para recuperar los datos de la tabla
        self.consulta = "SELECT * FROM `usuario` JOIN preguntas JOIN diagnostico_paciente"
      
        # Ejecutar la consulta y obtener los resultados
        self.cursor = self.conexion.cursor()
        self.cursor.execute(self.consulta)
        self.datos = self.cursor.fetchall()

        # Crear una ventana de Tkinter y un marco de tabla
        self.ventan3 = tk.Tk()
        self.ventan3.title("Datos guardados")
        self.ventan3.geometry("800x400")
        
        self.marco_tabla = ttk.Frame(self.ventan3, width=800, height=400)
        self.marco_tabla.pack(expand=tk.YES, fill=tk.BOTH)

        # Crear una tabla de Tkinter y agregar las columnas
        self.tabla = ttk.Treeview(self.marco_tabla)
        self.tabla['columns'] = tuple(range(len(self.datos[0])))

        # Agregar encabezados de columna a la tabla
        for i, encabezado in enumerate(self.cursor.column_names):
            self.tabla.column(i, width=100, anchor=tk.CENTER)
            self.tabla.heading(i, text=encabezado)

        # Agregar filas de datos a la tabla
        for fila in self.datos:
            self.tabla.insert('', tk.END, values=fila)

        # Empaquetar la tabla y la ventana
        self.tabla.pack(expand=tk.YES, fill=tk.BOTH)
        self.ventan3.mainloop()

        # Cerrar la conexión a la base de datos
        self.conexion.close()
        

if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana3(root)
    root.mainloop()
