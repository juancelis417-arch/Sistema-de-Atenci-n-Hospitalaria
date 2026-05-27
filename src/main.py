from modelo.paciente import registrar_paciente
from controlador.espera import ver_paciente_espera 
from modelo.cita import crear_cita             
from controlador.mostrar import mostrar_pacientes
from simulacion import simulacion



# Sistema de Atencion Hospitalaria

def main():
    while True:
      print()
      print("-------------------Sistema De Atencion Hospitalaria----------------------")
      print("1. Registro de paciente")
      print("2. Ver paciente en espera")
      print("3. Creacion de citas")
      print("4. Mostrar pacientes")
      print("5. Simulacion de sistema concurrente")



      contador =0
      seccion=input("Ingrese una opcion del Menu: " ) 
       
      if seccion == "1":
        if contador < 3:
          registrar_paciente()
          contador +=1

          
      elif seccion == "2":
          ver_paciente_espera()
      
      elif seccion == "3":
          crear_cita()
      
      elif seccion == "4":
          mostrar_pacientes()
      
      elif seccion == "5":
          simulacion()
      else:
            print("Se ha alcanzado el limite de pacientes registrados, no se pueden registrar mas pacientes...!!")
   


    