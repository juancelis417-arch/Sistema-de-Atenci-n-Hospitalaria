from controlador.datos import citas
from controlador.log import escribir_log
from datetime import datetime
import re

def crear_cita():
    print()
    print("Creando la cita...")
    nombre=input("Nombre Paciente: ")
        
    while True:
        fecha=input("Fecha de la Cita(dd/mm/yyyy): ")
    
        try:

            fecha_valida = datetime.strptime(fecha, "%d/%m/%Y")
            fecha_ocupada=False 
            
            for cita in citas:
                if cita["Fecha"] == fecha and cita["Hora"] == f"{hora} {jornada}":
                    
                    fecha_ocupada=True
                    break
                
            if fecha_ocupada:
                print("La fecha y hora seleccionada ya está ocupada, por favor elija otra fecha.\n")
                
            else:
                break

        except ValueError:
            print("Fecha inválida, Ingrese una fecha en el formato valido (dd/mm/yyyy)\n")
            
    while True:

        hora = input("Ingrese la hora de la cita (HH:MM): ")
        if re.match(r"^\d{1,2}:\d{2}$", hora):

            break

        else:

            print("Hora inválida. Ejemplo válido: 08:30")


    while True:

        jornada = input("Ingrese AM o PM: ").upper()

        if jornada == "AM" or jornada == "PM":
            break

        else:

            print("Solo puede ingresar AM o PM")
    
    print()
    print(f"------Que tipo de cita requiere-----")
    print("1.Consulta Externa")
    print("2.Consulta General")
    print("3.Cita Prioritaria\n")
    
    while True:
        tipo_cita=input(f"Escriba el tipo de consulta:")
        
        if tipo_cita == '1':
            tipo_cita = "Consulta Externa"
            break
        
        elif tipo_cita == '2':
            tipo_cita = "Consulta General"
            break
        
        elif tipo_cita == '3':
            tipo_cita = "Cita Prioritaria"
            break
            
        else:
            print("Opcion no valida, por favor ingrese una opcion valida")

        
    

    cita={
        "Nombre": nombre,
        "Fecha": fecha,
        "Hora": f"{hora} {jornada}",
        "Tipo_Cita": tipo_cita 
    }

    citas.append(cita)
    escribir_log(f"Cita Creada para {nombre}")
    print(f"La cita esta Agendada para el dia: {fecha} a las {hora} {jornada}...!\n")
    print(cita)