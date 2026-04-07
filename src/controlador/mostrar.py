from controlador.datos import pacientes
def mostrar_pacientes():
    print()
    print("-----Lista de pacientes-----")

    if len(pacientes) == 0:
        print("No hay pacientes")
    else:
        for p in pacientes:
            print(p)
