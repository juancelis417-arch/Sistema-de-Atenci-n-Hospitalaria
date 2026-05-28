from controlador.datos import citas
from controlador.log import escribir_log
from datetime import datetime

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
                if cita["Fecha"] == fecha:
                    
                    fecha_ocupada=True
                    break
                
            if fecha_ocupada:
                print("La fecha y hora seleccionada ya está ocupada, por favor elija otra fecha.\n")
                
            else:
                break

        except ValueError:
            print("Fecha inválida, Ingrese una fecha en el formato valido (dd/mm/yyyy)\n")
            
    hora=input("Hora de la cita si es AM o PM (HH:MM): ")
    
    
    print()
    print(f"------Que tipo de cita requiere-----")
    print("1.Consulta Externa")
    print("2.Consulta General")
    print("3.Cita Prioritaria\n")
    
    tipo_cita=input(f"Escriba el tipo de consulta:")
    
    if tipo_cita == '1':
        tipo_cita = "Consulta Externa"
       
    elif tipo_cita == '2':
        tipo_cita = "Consulta General"
    
    elif tipo_cita == '3':
        tipo_cita = "Cita Prioritaria"
    

    cita={
        "Nombre": nombre,
        "Fecha": fecha,
        "Hora": hora,
        "Tipo_Cita": tipo_cita 
    }

    citas.append(cita)
    escribir_log(f"Cita Creada para {nombre}")
    print(f"La cita esta Agendada para el dia: {fecha} a las {hora}...!\n")
    print(cita)