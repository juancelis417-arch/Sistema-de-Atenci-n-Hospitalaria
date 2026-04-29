from controlador.datos import citas
from controlador.log import escribir_log
def crear_cita():
    print()
    print("Creando la cita...")
    nombre=input("Nombre Paciente: ")
    fecha=int(input("Fecha de la Cita: "))
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
        "Tipo_Cita": tipo_cita 
    }

    citas.append(cita)
    escribir_log(f"Cita Creada para {nombre}")
    print("La cita esta Agendada...!\n")
    print(cita)