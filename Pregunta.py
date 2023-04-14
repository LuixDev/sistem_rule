from sistemadereglas import *
from random import choice





engine = sistemadereglas()
engine.reset()

v_dolorpecho = input("¿Presenta usted dolor en el pecho? responda: \n si  no ")
engine.declare(reglas(dolorpecho=choice([str(v_dolorpecho)])))

v_desmayos = input("¿Sufre desmayos? \n si   no ")
engine.declare(reglas(desmayo=choice([str(v_desmayos)])))

v_latidoscorazon = input("¿Siente latidos irregulares en el corazón? \n si   no ")
engine.declare(reglas(latidoscorazon=choice([str(v_latidoscorazon)])))

v_faltadeaire = input("¿Se siente con falta de aire? \n si   no   ")
engine.declare(reglas(faltadeaire=choice([str(v_faltadeaire)])))

v_hinchazonpies = input("¿Se inflaman sus pies o tobillos? \n si   no ")
engine.declare(reglas(hinchazonpies=choice([str(v_hinchazonpies)])))
engine.run()


