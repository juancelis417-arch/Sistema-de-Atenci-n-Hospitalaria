from controlador.datos import citas
from controlador.log import escribir_log
def crear_cita():
    print()
    print("Creando la cita...")
    nombre=input("Nombre Paciente: ")
    fecha=int(input("Fecha de la Cita: "))
    print(f"Que tipo de cita requiere")
    print("Consulta Externa, Consulta General, Cita Prioritaria")
    tipo_cita=input(f"Escriba el tipo de consulta:")
    

    cita={
        "nombre": nombre,
        "fecha": fecha,
        "tipo_cita": tipo_cita 
    }

    citas.append(cita)
    escribir_log(f"Cita Creada para {nombre}")
    print("La cita esta Agendada...!\n")
    print(cita)