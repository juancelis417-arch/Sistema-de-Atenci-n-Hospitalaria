from controlador.datos import pacientes
def ver_paciente_espera():
    pass
print("-----pacientes en espera-----")

if len(pacientes) == 0:
    print("no hay pacientes")
else:
    for p in pacientes:
        print(p)
