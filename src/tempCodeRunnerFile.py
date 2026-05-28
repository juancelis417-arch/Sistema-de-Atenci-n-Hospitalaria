from modelo.paciente import registrar_paciente
from controlador.espera import ver_paciente_espera 
from modelo.cita import crear_cita             
from controlador.mostrar import mostrar_pacientes
from simulacion import simulacion
from controlador.mostrar import mostrar_pacientes, mostrar_citas
from controlador.mostrar import mostrar_pacientes, mostrar_citas, mostrar_procesos



# Sistema de Atencion Hospitalaria

while True:
      print()
      print("-------------------Sistema De Atencion Hospitalaria----------------------")
      print("1. Registro de paciente")
      print("2. Ver paciente en espera")
      print("3. Creacion de citas")
      print("4. Mostrar pacientes")
      print("5. Mostrar citas agendadas")
      print("6. Simulacion de sistema concurrente")
      print("7. Mostrar procesos en ejecucion")
      print("8. Salir")



      contador =0
      seccion=input("Ingrese una opcion del Menu: " ) 
       
      if seccion == "1":
        if contador < 3:
          registrar_paciente()
          contador +=1
        else:
            print("Se ha alcanzado el limite de pacientes registrados, no se pueden registrar mas pacientes...!!")

          
      elif seccion   == "2":
          ver_paciente_espera()
      
      elif seccion == "3":
          crear_cita()
      
      elif seccion == "4":
          mostrar_pacientes()
      
      elif seccion == "5":
          mostrar_citas()
      
      elif seccion == "6":
          simulacion()
          
      elif seccion == "7":
            mostrar_procesos()
            
      elif seccion == "8":
            print("Gracias por usar el sistema de atencion hospitalaria...!!")
            break
      else:
            print("Se ha alcanzado el limite de pacientes registrados, no se pueden registrar mas pacientes...!!")
   


    