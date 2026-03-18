from controlador.datos import pacientes

print("-----pacientes en espera-----")

if len(pacientes) == 0:
    print("no hay pacientes")
else:
    for p in pacientes:
        print(p)
