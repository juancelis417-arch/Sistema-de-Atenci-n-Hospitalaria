import threading
import time
from controlador.datos import pacientes

def atender(nombre):
    print(f"doctor atendiendo a {nombre}")
    time.sleep(3)
    print(f"{nombre} fue atendido")

def simulacion():

    for p in pacientes:
        hilo = threading.Thread(target=atender, args=(p[0],))
        hilo.start()