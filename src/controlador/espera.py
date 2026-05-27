from controlador.datos import pacientes


def ver_paciente_espera():
    print()

    print("\n-----Pacientes en espera-----")

    if len(pacientes) == 0:
        print("No hay pacientes en espera")
    else:
         for p in pacientes:
            print(f"Nombre: {p[0]} | Edad: {p[1]} | Sintoma: {p[2]}")
    print()
            