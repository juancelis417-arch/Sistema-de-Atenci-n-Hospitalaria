import os

print("-------------------Sistema De Atencion Hospitalaria----------------------")
print("1. Registro de paciente")
print("2. ver paciente en espera")
print("3. Creacion de citas")
print("4. Mostrar pacientes")
print("5. Simulacion de sistema concurrente")

opcion = [1, 2, 3, 4, 5]


seccion=int(input(f"ingrese una {opcion} del menu: " ))



if seccion == 1:
    os.system("python src/modelo/paciente.py")
    
elif seccion ==2:
    os.system("python src/controlador/mostrar.py")
    
elif seccion == 3:
    os.system("python src/modelo/cita.py")
    
elif seccion == 4:
    os.system("python src/controlador/mostrar.py")
    
elif seccion == 5:
    print("Simulando atencion de pacientes...")
    

   