from controlador.datos import pacientes
from controlador.datos import citas
import psutil

def mostrar_pacientes():
    print()
    print("-----Lista de pacientes-----")

    if len(pacientes) == 0:
        print("No hay pacientes")
    else:
        for p in pacientes:
            print(p)

def mostrar_citas():

    print()
    print("-----Lista de citas agendadas-----")

    if len(citas) == 0:

        print("No hay citas agendadas")

    else:

        for c in citas:
            print(f"paciente: {c['Nombre']}")
            print(f"Fecha: {c['Fecha']}")
            print(f"Hora: {c['Hora']} | Tiempo: {c['tiempo']}")
            print("------------------------")
            
def mostrar_procesos():

    print()
    print("-----Procesos en Ejecucion-----")

    contador = 0

    for proceso in psutil.process_iter():

        try:
            print(f"PID: {proceso.pid} | Nombre: {proceso.name()}")

            contador += 1

            if contador == 15:
                break

        except:
            pass

