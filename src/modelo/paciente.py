from controlador.datos import pacientes
from controlador.log import escribir_log

def registrar_paciente():
    print()
    print("-----ingrese los datos para ser regidtraso en el sistema...!-----")
    nombre=input("ingrese su nombre: ")
    print(f"paciente {nombre} fue registrado\n")
    
    edad=(input("ingrese su edad: "))
    print(f"su edad {edad} fue registrada\n")
    
    sintoma=str(input("ingrese su sintoma: "))
    print(f"su sistma {sintoma} fue registrado\n")
    
    paciente=(nombre, edad, sintoma)
    print(paciente)
    
    
    pacientes.append(paciente)
    escribir_log(f"Paciente registrado: {nombre}")


    print("Paciente registrado exitosamente!!")

   

