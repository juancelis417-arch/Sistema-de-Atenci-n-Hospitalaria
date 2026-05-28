from controlador.datos import pacientes
from controlador.log import escribir_log
from controlador.espera import ver_paciente_espera
from simulacion import atender



def registrar_paciente():
    print()
    print("-----Ingrese los datos para ser registraso en el sistema...!-----")
    
    while True:
        nombre=str(input("Ingrese su Nombre: "))
        if not nombre.isdigit():
            print(f"Paciente {nombre} fue registrado\n")
            break
        
        else:
            print("El nombre debe contener solo letras, por favor ingrese un nombre valido\n")
            nombre=str(input("Ingrese su Nombre: "))
            
            print(f"Paciente {nombre} fue registrado\n")

        
    while True:
        edad=(input("Ingrese su Edad: "))
        
        if edad.isdigit():
            print(f"Su edad {edad} fue registrada\n")
            break
        
        else:
            print("La edad debe ser un número, por favor ingrese una edad valida\n")
            edad=input("Ingrese su Edad: ")
            print(f"Su edad {edad} fue registrada\n")
        


    while True:
        sintoma=str(input("Ingrese su Sintoma: "))
        if not sintoma.isdigit():
            print(f"Su sistoma {sintoma} fue registrado\n")
            break
        
        else:
            print("El síntoma debe contener solo letras, por favor ingrese un síntoma valido\n")
            sintoma=str(input("Ingrese su Sintoma: "))
        print(f"Su sistoma {sintoma} fue registrado\n")
        
        tiempo=str(input("Ingrese horario de llegada si es AM o PM: "))
        if tiempo.upper() in ["AM", "PM"]:
            print(f"Horario de llegada {tiempo} fue registrado\n")
            break
        else:
            print("Por favor, ingrese 'AM' o 'PM'\n")


    while True:
        print("\n-----Nivel de prioridad-----")
        print(f"1.Prioridad Baja (No Urgente)")
        print(f"2.Prioridad Media (Urgente Moderado)")
        print(f"3.Prioridad Alta (Urgente/Critico)")
        print(f"4.Salir")

        
        
        
        print()
        complejida=input("ingrese una opcion del menu: ")

        
        if complejida == "1":
            complejida = "Baja"
            print("\nPaciente Complejida baja, Atención espera")
            break

            
        elif complejida == "2":
            complejida = "Media"
            print("\nPaciente Complejida media, Atención espera")
            break

        
        elif complejida == "3":
            complejida = "Alta"
            print("\nPaciente crítico, Atención inmediata")
            atender(nombre, "Alta")
            break
            
        elif complejida == "4":
            print("Saliendo...")
            return
        
        else:
            print("Opción no válida. Por favor, ingrese una opción del menú válida.")
            continue
        

            

        
        
        
    paciente=(nombre, edad, sintoma, complejida)
    print(paciente)
        
        
    pacientes.append(paciente)
    escribir_log(f"Paciente registrado: {nombre}")

    print()
    print("Paciente registrado exitosamente...!!")

    
