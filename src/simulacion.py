import threading
import time
from controlador.datos import pacientes
from controlador.log import escribir_log

lock = threading.Lock()

def atender(nombre, prioridad):
    
    if prioridad == "Alta":
        doctor = "Doctor Julian Especialista"
    elif prioridad == "Media":
        doctor = "Doctor Fabian Especialista General"
    elif prioridad == "Baja":
        doctor = "Doctor Maurico Especialista En Consulta"
    
    
    
    
    with lock:

      print("------------------------------------")
      print(f"{doctor} atendiendo a {nombre}")
      time.sleep(3)
    
      print(f"Relizando diagnostico del paciente {nombre}")
      time.sleep(3)
    
      print(f"Examenes de laboratorio promedio basico")
      time.sleep(3)
    
      print(f"Examenes de diagnostico de {nombre}: fue estable")
      time.sleep(3)
    
      print(f"Paciente estable, Cumple con requesitos de alta ")
      time.sleep(3) 
    
      print(f"{nombre} fue atendido por {doctor}")
      print("-----------------------------------")
        
      escribir_log(f"{nombre} fue atendido")

def simulacion():
    
    

    hilos = []
    alta=[]
    media=[]
    baja=[]
    
    for p in pacientes:
     if p[3] == "Alta":
        alta.append(p)
     elif p[3] == "Media":
        media.append(p)
     else:
        baja.append(p)

    ordenados = alta + media + baja
    

    for p in ordenados:
        hilo = threading.Thread(target=atender, args=(p[0], p[3]))
        hilos.append(hilo)
        hilo.start()

    for h in hilos:
        h.join()
        

            
            
            
            