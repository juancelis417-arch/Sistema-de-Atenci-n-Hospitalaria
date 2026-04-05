from controlador.datos import citas
from controlador.log import escribir_log
def crear_cita():
    print()
    print("Creando la cita...")
    nombre=input("nombre paciente: ")
    fecha=input("fecha de la cita: ")

    cita={
        "nombre": nombre,
        "fecha": fecha
    }

    citas.append(cita)
    escribir_log(f"Cita creada para {nombre}")
    print("la cita esta agendada\n")
    print(cita)