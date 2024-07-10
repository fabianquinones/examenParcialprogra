import funciones as fn

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]


while True:
    
        print("************************")
        print("bienvenido a la empresa")
        print("************************")
        print("elija una de las siguientes opciones")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opc=int(input())
        if opc ==1:
            fn.asignarSueldos(trabajadores)
        elif opc==2:
            fn.calificarSueldos()
        elif opc==3:
            fn.verEstats()
        elif opc==4:
            fn.reportes()
        elif opc==5:
            fn.salir()
            break

    