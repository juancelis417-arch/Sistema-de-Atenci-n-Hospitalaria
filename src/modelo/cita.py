from controlador.datos import citas
def crear_cita():
    print("Creando la cita...")
nombre=input("nombre paciente")
fecha=("fecha de la cita")

cita={
    "nombre": nombre,
    "fehca":fecha
}

citas.append(cita)
print("la sita esta agendada")
print(cita)