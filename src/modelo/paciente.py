from controlador.datos import pacientes
input("-----ingrese los datos para ser regidtraso en el sistema...!-----")
  
def registrar_paciente():
  
 nombre=input("ingrese su nombre: ")
 print(f"paciente {nombre} fue registrado\n")
   
 edad=(input("ingrese su edad: "))
 print(f"su edad {edad} fue registrada")
   
 sintoma=str(input("ingrese su sintoma: "))
 print(f"su sistma {sintoma} fue registrado\n")
   
 paciente=("nombre: "+ nombre, "edad: "+ edad ,"sintoma: "+ sintoma)
 print(paciente)
 
 
 pacientes.append(paciente)

 print("Paciente registrado exitosamente!!")


 

registrar_paciente()

