from controlador.datos import pacientes
from controlador.log import escribir_log

def registrar_paciente():
    print()
    print("-----Ingrese los datos para ser regidtraso en el sistema...!-----")
    nombre=input("Ingrese su nombre: ")
    print(f"Paciente {nombre} fue registrado\n")
    
    edad=(input("Ingrese su edad: "))
    print(f"Su edad {edad} fue registrada\n")
    
    sintoma=str(input("Ingrese su sintoma: "))
    print(f"Su sistma {sintoma} fue registrado\n")
    
    paciente=(nombre, edad, sintoma)
    print(paciente)
    
    
    pacientes.append(paciente)
    escribir_log(f"Paciente registrado: {nombre}")


    print("Paciente registrado exitosamente...!!")

   

