import threading
import time
from controlador.datos import pacientes
from controlador.log import escribir_log

lock = threading.Lock()

def atender(nombre):
    
    with lock:

        print(f"Doctor Salk atendiendo a {nombre}")
        escribir_log(f"Doctor  Salk atendiendo a {nombre}")
        
    time.sleep(3)

        
    with lock:

        print(f"{nombre} fue atendido")
        escribir_log(f"{nombre} fue atendido")

def simulacion():
    
     import threading
import time
from controlador.datos import pacientes
from controlador.log import escribir_log

lock = threading.Lock()

def atender(nombre):
    
    with lock:

        print(f"Doctor Salk atendiendo a {nombre}")
        escribir_log(f"Doctor atendiendo a {nombre}")
        
    time.sleep(3)
    
    print(f"Relizando diagnostico del paciente {nombre}")
    time.sleep(3)
    
    print(f"Examenes de laboratorio promedio basico")
    time.sleep(3)
    
    print(f"Examenes de diagnostico de {nombre}: fue estable")
    time.sleep(3)
    
    print(f"Paciente estable, Cumple con requesitos de alta ")
    time.sleep(3) 
    
        
    with lock:
        print(f"{nombre} fue atendido")
        escribir_log(f"{nombre} fue atendido")

def simulacion():
    
    

    hilos = []

    for p in pacientes:
        hilo = threading.Thread(target=atender, args=(p[0],))
        hilos.append(hilo)
        hilo.start()

    for h in hilos:
        h.join()
        

            
            
            
            