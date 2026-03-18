from modelo.paciente import registrar_paciente
from controlador.espera import ver_paciente_espera 
from modelo.cita import crear_cita             
from controlador.mostrar import mostrar_pacientes


while True:
    print("-------------------Sistema De Atencion Hospitalaria----------------------")
    print("1. Registro de paciente")
    print("2. ver paciente en espera")
    print("3. Creacion de citas")
    print("4. Mostrar pacientes")
    print("5. Simulacion de sistema concurrente")

    opcion = [1, 2, 3, 4, 5]
    
    seccion=input(f"ingrese una {opcion} del menu: " )



    if seccion == 1:
      registrar_paciente()
    
    elif seccion == 2:
     ver_paciente_espera()
    
    elif seccion == 3:
     crear_cita()
    
    elif seccion == 4:
     mostrar_pacientes()
    
    elif seccion == 5:
     print("Simulando atencion de pacientes...")
    

   