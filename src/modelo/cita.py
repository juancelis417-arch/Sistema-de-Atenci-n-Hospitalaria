from controlador.datos import citas
from controlador.log import escribir_log
def crear_cita():
    print()
    print("Creando la cita...")
    nombre=input("Nombre paciente: ")
    fecha=input("Fecha de la cita: ")

    cita={
        "nombre": nombre,
        "fecha": fecha
    }

    citas.append(cita)
    escribir_log(f"Cita creada para {nombre}")
    print("La cita esta agendada...!\n")
    print(cita)