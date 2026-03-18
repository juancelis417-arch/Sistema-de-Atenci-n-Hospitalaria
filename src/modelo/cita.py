from controlador.datos import citas
def crear_cita():
    print()
    print("Creando la cita...")
    nombre=input("nombre paciente")
    fecha=input("fecha de la cita")

    cita={
        "nombre": nombre,
        "fecha": fecha
    }

    citas.append(cita)
    print("la sita esta agendada")
    print(cita)