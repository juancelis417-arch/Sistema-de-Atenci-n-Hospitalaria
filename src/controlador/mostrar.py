from controlador.datos import pacientes
def mostrar_pacientes():
    print()
    print("-----lista de pacientes-----")

    if len(pacientes) == 0:
        print("no hay pacientes")
    else:
        for p in pacientes:
            print(p)
