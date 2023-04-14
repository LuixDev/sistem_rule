from Reglas import *
from experta import *
from tkinter import messagebox, Tk, Label
import mysql.connector

class sistemadereglas(KnowledgeEngine):

  
   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="no")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="no")),(reglas(hinchazonpies="no")))
   def m1(self):
        print("Salud ok")
        messagebox.showinfo(title="Resultado", message="Bien de salud")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Bien de salud"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()
  
   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="no")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="si")))
   def m2(self):
        print("Edema")
        messagebox.showinfo(title="Resultado", message="Edema")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Edema"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="no")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="no")))
   def m3(self):
        print("Disnea")
        messagebox.showinfo(title="Resultado", message="Disnea")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Disnea"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="no")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="si")))
   def m4(self):
        print("Insuficiencia cardiaca")
        messagebox.showinfo(title="Resultado", message="Insuficiencia cardiaca")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Insuficiencia cardiaca"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="no")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="no")))
   def m5(self):
        print("Fibrilación auricular")
        messagebox.showinfo(title="Resultado", message="Fibrilación auricular")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Fibrilación auricular"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="no")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="si")))
   def m6(self):
        print("no hay relacion clara con la enfermedad")
        messagebox.showinfo(title="Resultado", message="no hay relacion clara con la enfermedad")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "no hay relacion clara con la enfermedad"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="no")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="no")))
   def m7(self):
        print("Buscar ayuda medica inmediata")
        messagebox.showinfo(title="Resultado", message="Buscar ayuda medica inmediata")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Buscar ayuda medica inmediata"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="no")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="si")))
   def m8(self):
        print("Insuficiencia cardiaca. fibrilación auricular")
        messagebox.showinfo(title="Resultado", message="Insuficiencia cardiaca. fibrilación auricular")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Insuficiencia cardiaca. fibrilación auricular"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="si")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="no")))
   def m9(self):
        print("Muchas causas posibles (calor o deshidratacion. Aungustia. problemas del corazon)")
        messagebox.showinfo(title="Resultado", message="Muchas causas posibles (calor o deshidratacion. Aungustia. problemas del corazon")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Muchas causas posibles (calor o deshidratacion. Aungustia. problemas del corazon"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="si")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="si")))
   def m10(self):
        print("No hay una relacion clara de la enfermedad")
        messagebox.showinfo(title="Resultado", message="No hay una relacion clara de la enfermedad")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "No hay una relacion clara de la enfermedad"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="si")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="no")))
   def m11(self):
        print("Signo de ataque cardiaco o embolia pulmunar")
        messagebox.showinfo(title="Resultado", message="Signo de ataque cardiaco o embolia pulmunar")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Signo de ataque cardiaco o embolia pulmunar"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="si")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="si")))
   def m12(self):
        print("Coagulo sanguineo en los pulmones o una enfermedad grave del corazon")
        messagebox.showinfo(title="Resultado", message="Coagulo sanguineo en los pulmones o una enfermedad grave del corazon")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Coagulo sanguineo en los pulmones o una enfermedad grave del corazon"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="si")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="no")))
   def m13(self):
        print("Sin diagnostico (posibles problemas de azucar)")
        messagebox.showinfo(title="Resultado", message="Coagulo sanguineo en los pulmones o una enfermedad grave del corazon")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Coagulo sanguineo en los pulmones o una enfermedad grave del corazon"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="si")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="si")))
   def m14(self):
        print("No hay relacion con la enfermedad")
        messagebox.showinfo(title="Resultado", message="No hay relacion con la enfermedad")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "No hay relacion con la enfermedad"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="si")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="no")))
   def m15(self):
        print("No hay relacion con la enfermedad") 
        messagebox.showinfo(title="Resultado", message="No hay relacion con la enfermedad")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "No hay relacion con la enfermedad"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()
    
   @Rule(AND(reglas(dolorpecho="no")),(reglas(desmayo="si")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="si")))
   def m16(self):
        print("Problemas cariacos")
        messagebox.showinfo(title="Resultado", message="Problemas cariacos")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Problemas cariacos"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="no")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="no")))
   def m17(self):
        print("Ataque cardíaco o un coágulo de sangre en los pulmones")
        messagebox.showinfo(title="Resultado", message="Ataque cardíaco o un coágulo de sangre en los pulmones")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Ataque cardíaco o un coágulo de sangre en los pulmones"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="no")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="si")))
   def m18(self):
        print("Edema pulmonar")
        messagebox.showinfo(title="Resultado", message="Edema pulmonar")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Edema pulmonar"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="no")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="no")))
   def m19(self):
        print("Embolia pulmonar")
        messagebox.showinfo(title="Resultado", message="Embolia pulmonar")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Embolia pulmonar"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="no")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="si")))
   def m20(self):
        print("Miocarditis")
        messagebox.showinfo(title="Resultado", message="Miocarditis")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Miocarditis"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()
        

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="no")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="no")))
   def m21(self):
        print("Arritmia cardiaca")
        messagebox.showinfo(title="Resultado", message="Arritmia cardiaca")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Arritmia cardiaca"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="no")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="si")))
   def m22(self):
        print("Enfermedad cardiaca (Someterse a estudios profundos)")
        messagebox.showinfo(title="Resultado", message="Enfermedad cardiaca (Someterse a estudios profundos)")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Enfermedad cardiaca (Someterse a estudios profundos)"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="no")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="no")))
   def m23(self):
        print("Taticardia")
        messagebox.showinfo(title="Resultado", message="Taticardia")
       
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Taticardia"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="no")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="si")))
   def m24(self):
        print("Síntomas de advertencia de enfermedad cardíaca (Someterse a estudios profundos)")
        messagebox.showinfo(title="Resultado", message="Síntomas de advertencia de enfermedad cardíaca (Someterse a estudios profundos)")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Síntomas de advertencia de enfermedad cardíaca (Someterse a estudios profundos)"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="si")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="no")))
   def m25(self):
        print("Sin diagnostico")
        messagebox.showinfo(title="Resultado", message="Sin diagnostico")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Sin diagnostico"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="si")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="si")))
   def m26(self):
        print("Sin diagnostico (Someterse a estudios profundos)")
        messagebox.showinfo(title="Resultado", message="Sin diagnostico (Someterse a estudios profundos)")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Sin diagnostico (Someterse a estudios profundos)"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="si")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="no")))
   def m27(self):
        print("Posible ataque cardiaco")
        messagebox.showinfo(title="Resultado", message="Posible ataque cardiaco")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Posible ataque cardiaco"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="si")),(reglas(latidoscorazon="no")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="si")))
   def m28(self):
        print("Insuficiencia cardiaca/Miocarditis")
        messagebox.showinfo(title="Resultado", message="Insuficiencia cardiaca/Miocarditis")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Insuficiencia cardiaca/Miocarditis"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="si")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="no")))
   def m29(self):
        print("Síndrome de taquicardia ortostática postural")
        messagebox.showinfo(title="Resultado", message="Síndrome de taquicardia ortostática postural")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Síndrome de taquicardia ortostática postural"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="si")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="no")), (reglas(hinchazonpies="si")))
   def m30(self):
        print("Miocarditis/Posible Ataque al corazón")
        messagebox.showinfo(title="Resultado", message="Miocarditis/Posible Ataque al corazón")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Miocarditis/Posible Ataque al corazón"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="si")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="no")))
   def m31(self):
        print("Taticardia/Arritmias")
        messagebox.showinfo(title="Resultado", message="Taticardia/Arritmias")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Taticardia/Arritmias"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()

   @Rule(AND(reglas(dolorpecho="si")),(reglas(desmayo="si")),(reglas(latidoscorazon="si")),(reglas(faltadeaire="si")), (reglas(hinchazonpies="si")))
   def m32(self):
        print("Problemas en la válvula cardíaca")
        messagebox.showinfo(title="Resultado", message="Problemas en la válvula cardíaca")
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO diagnostico_paciente (Diagnostico) VALUES (%s)"
        valor = "Problemas en la válvula cardíaca"
        cursor.execute(sql, (valor,))
        conexion.commit()
        conexion.close()