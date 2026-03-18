from controlador.datos import pacientes


def ver_paciente_espera():

    print("\n-----pacientes en espera-----")

    if len(pacientes) == 0:
        print("no hay pacientes")
    else:
         for p in pacientes:
            print(f"Nombre: {p[0]} | Edad: {p[1]} | Síntoma: {p[2]}")
            return pacientes
         