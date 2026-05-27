import threading
import time
import psutil
from controlador.datos import pacientes
from controlador.log import escribir_log

lock = threading.Lock()

def atender(nombre, prioridad):
    
    if prioridad == "Alta":
        doctor = "Doctor Julian Especialista"
        
    elif prioridad == "Media":
        doctor = "Doctor Fabian Especialista General"
        
    else:
        doctor = "Doctor Maurico Especialista En Consulta"
        
    
    with lock:

      print("------------------------------------")
      print(f"{doctor} atendiendo a {nombre}")
      time.sleep(3)
      
      escribir_log("------------------------------------")
      escribir_log(f"{doctor} atendiendo a {nombre}")
      
    
      print(f"Realizando diagnostico del paciente {nombre}")
      escribir_log(f"Realizando diagnostico del paciente {nombre}")
      time.sleep(3)
    
      print(f"Examenes de laboratorio promedio basico")
      escribir_log(f"Examenes de laboratorio promedio basico")
      time.sleep(3)
    
      print(f"Examenes de diagnostico de {nombre}: fue estable")
      escribir_log(f"Examenes de diagnostico de {nombre}: fue estable")
      time.sleep(3)
    
      print(f"Paciente estable, Cumple con requesitos de alta ")
      escribir_log(f"Paciente estable, Cumple con requesitos de alta ")
      time.sleep(3) 
    
      print(f"{nombre} fue atendido por {doctor}")
      escribir_log(f"{nombre} fue atendido por {doctor}")
      print("-----------------------------------")
        
      escribir_log("-----------------------------------")

def simulacion():
    
    print("\n--------- Monitoreo Del Sistema Operativo ---------")
    print(f"Hilos activos: {threading.active_count()}")
    print(f"Uso de CPU: {psutil.cpu_percent()}%")
    print(f"Uso de Memoria RAM: {psutil.virtual_memory().percent}%")
    print("-----------------------------------------\n")

    hilos = []
    alta = []
    media = []
    baja = []
    
    
    for p in pacientes:
     if p[3] == "Alta":
        alta.append(p)
     elif p[3] == "Media":
        media.append(p)
     else:
        baja.append(p)

    ordenados = alta + media + baja
    
    print("Orden de atencion por prioridad:\n")
    for paciente in ordenados:
        print(f"{paciente[0]} --> {paciente[3]}\n")

    for p in ordenados:
        hilo = threading.Thread(target=atender, args=(p[0], p[3]))
        hilos.append(hilo)
        hilo.start()

    for h in hilos:
        h.join()
        

            
            
            
            