import threading
import time
from controlador.datos import pacientes
from controlador.log import escribir_log

lock = threading.Lock()

def atender(nombre):
    
    with lock:

        print(f"doctor atendiendo a {nombre}")
        escribir_log(f"Doctor atendiendo a {nombre}")
        time.sleep(3)
        
        with lock:
         print(f"{nombre} fue atendido")
         escribir_log(f"{nombre} fue atendido")

def simulacion():
    
    

    for p in pacientes:
        hilo = threading.Thread(target=atender, args=(p[0],))
        hilo.start()