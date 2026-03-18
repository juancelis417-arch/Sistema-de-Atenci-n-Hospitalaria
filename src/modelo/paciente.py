from controlador.datos import pacientes

def registrar_paciente():
    print()
    print("-----ingrese los datos para ser regidtraso en el sistema...!-----")
    nombre=input("ingrese su nombre: ")
    print(f"paciente {nombre} fue registrado\n")
    
    edad=(input("ingrese su edad: "))
    print(f"su edad {edad} fue registrada\n")
    
    sintoma=str(input("ingrese su sintoma: "))
    print(f"su sistma {sintoma} fue registrado\n")
    
    paciente=("nombre: "+ nombre, "edad: "+ edad ,"sintoma: "+ sintoma)
    print(paciente)
    
    
    pacientes.append(paciente)


    print("Paciente registrado exitosamente!!")

   

