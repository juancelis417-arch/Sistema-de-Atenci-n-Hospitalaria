from controlador.datos import pacientes
from controlador.log import escribir_log
from controlador.espera import ver_paciente_espera
from simulacion import atender


def registrar_paciente():
    print()
    print("-----Ingrese los datos para ser registraso en el sistema...!-----")
    
    nombre=input("Ingrese su nombre: ")
    print(f"Paciente {nombre} fue registrado\n")
    
    edad=(input("Ingrese su edad: "))
    print(f"Su edad {edad} fue registrada\n")
    
    sintoma=str(input("Ingrese su sintoma: "))
    print(f"Su sistma {sintoma} fue registrado\n")
    
    print()
    print(f"1.Prioridad baja (No Urgente)")
    print(f"2.Prioridad media (Urgente Moderado)")
    print(f"3.Prioridad alta (Urgente/Critico)")
    
    
    
    print()
    complejida=input("ingrese una opcion del menu:")
    
    if complejida == "1":
        complejida = "complejida baja"
        ver_paciente_espera()
        
    elif complejida == "2":
        complejida = "complegida media"
        ver_paciente_espera()
    
    elif complejida == "3":
        complejida = "complegida alta"
        atender(nombre)
    
    
    
    paciente=(nombre, edad, sintoma, complejida)
    print(paciente)
    
    
    pacientes.append(paciente)
    escribir_log(f"Paciente registrado: {nombre}")


    print("Paciente registrado exitosamente...!!")

   

