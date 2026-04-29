from controlador.datos import pacientes
from controlador.log import escribir_log
from controlador.espera import ver_paciente_espera
from simulacion import atender


def registrar_paciente():
    print()
    print("-----Ingrese los datos para ser registraso en el sistema...!-----")
    
    nombre=input("Ingrese su Nombre: ")
    print(f"Paciente {nombre} fue registrado\n")
    
    edad=(input("Ingrese su Edad: "))
    print(f"Su edad {edad} fue registrada\n")
    
    sintoma=str(input("Ingrese su Sintoma: "))
    print(f"Su sistoma {sintoma} fue registrado\n")
    
    print("\n-----Nivel de prioridad-----")
    print(f"1.Prioridad Baja (No Urgente)")
    print(f"2.Prioridad Media (Urgente Moderado)")
    print(f"3.Prioridad Alta (Urgente/Critico)")
    
    
    
    print()
    complejida=input("ingrese una opcion del menu:")
    
    if complejida == "1":
        complejida = "Complejida Baja"
        print("\nPaciente Complejida baja, Atención espera")
        ver_paciente_espera()
        
    elif complejida == "2":
        complejida = "Complejida Media"
        print("\nPaciente Complejida media, Atención espera")
        ver_paciente_espera()
    
    elif complejida == "3":
        complejida = "Complejida Alta"
        print("\nPaciente crítico, Atención inmediata")
        atender(nombre)
    
    
    
    paciente=(nombre, edad, sintoma, complejida)
    print(paciente)
    
    
    pacientes.append(paciente)
    escribir_log(f"Paciente registrado: {nombre}")

    print()
    print("Paciente registrado exitosamente...!!")

   
