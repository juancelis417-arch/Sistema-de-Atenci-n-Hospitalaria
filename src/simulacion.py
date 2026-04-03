import threading
import time
from controlador.datos import pacientes

def atender_paciente(nombre):
    print(f"Atendiendo a {nombre}")
    time.sleep(3)
    print(f"{nombre} fue atendido")

def simulacion():
    for p in pacientes:
        t = threading.Thread(target=atender_paciente, args=(p[0],))
        t.start()