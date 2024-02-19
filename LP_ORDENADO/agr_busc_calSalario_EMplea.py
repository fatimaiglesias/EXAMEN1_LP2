empleados = []
idEmpleado = 0

def comprobarEmpleados():
    if len(empleados) == 0: # si la longitud de la lista es 0 entonces esta vacia y returno false
        # es como si preguntaramos -> ¿hay empleados?
        return False
    else:
        return True

def agregarEmpleados():    
    id_empleado = len(empleados) + 1
    nombreEmpleado = input("INGRESE EL NOMBRE DEL EMPLEADO : ")
    departamentoSalario = input("INGRESE EL DEPARTAMENTO DEL EMPLEADO : ")
    salarioEmpleado = float(input("INGRESE EL SALARIO DEL EMPLEADO : S/."))
    while salarioEmpleado <= 0:
        print("ERROR! SALARIO INVÁLIDO. INGRESE EL SALARIO NUEVAMENTE.")
        salarioEmpleado = float(input("INGRESE EL SALARIO DEL EMPLEADO : S/."))

    empleados.append([id_empleado, nombreEmpleado, departamentoSalario, salarioEmpleado])

    

def eliminarEmpleado():

    global empleados

    if comprobarEmpleados():
        nombreEmpleadoEliminar = input("INGRESE EL NOMBRE DEL EMPLEADOS A ELIMINAR : ")

        empleadoEliminar = [empleado for empleado in empleados if empleado[1] == nombreEmpleadoEliminar]

        if len(empleadoEliminar) == 0:
            print("EMPLEADO NO ENCONTRADO!")
        else:
            empleados = [empleado for empleado in empleados if empleado[1] != nombreEmpleadoEliminar]
            print(f"EMPLEADO {nombreEmpleadoEliminar} ELIMINADO CORRECTAMENTE!")
    else:
        print("ERROR! LISTA DE EMPLEADOS VACÍA.")

def mostarEmpleados():

    global empleados
    global idEmpleado

    if comprobarEmpleados():
        for empleado in empleados:
            print(f"ID : {empleado[0]}, NOMBRE : {empleado[1]}, DEPARTAMENTO : {empleado[2]}, SALARIO : {empleado[3]}")
    else:
        print("ERROR! LISTA DE EMPLEADOS VACÍA.")

def calcularSalarioPromDepartamento():

    global empleados
    global idEmpleado

    sumaDepartamental = 0
    promedioDepartamental = 0

    if comprobarEmpleados():
        nombreDepartamento = input("INGRESE EL NOMBRE DEL DEPARTAMENTO: ")

        departamento= [empleado for empleado in empleados if empleado[2] == nombreDepartamento]

        if len(departamento) == 0:
            print("NO SE ENCONTRARON COINCIDENCIAS!")
        else:
            print("SE ENCONTRARON COINCIDENCIAS")
            for empleado in departamento:
                print(f"ID : {empleado[0]}, NOMBRE : {empleado[1]}, DEPARTAMENTO : {empleado[2]}, SALARIO : {empleado[3]}")
                sumaDepartamental += empleado[3]
            promedioDepartamental = sumaDepartamental/len(departamento)
    else:
        print("ERROR! LISTA DE EMPLEADOS VACÍA.")

    return promedioDepartamental

def salarioGeneral():
    global empleados

    sumGeneral = 0
    promedioGeneral = 0

    if comprobarEmpleados():
        for empleado in empleados:
            sumGeneral += empleado[3]
        promedioGeneral = sumGeneral/len(empleados)
    else:
        print("ERROR! LISTA DE EMPLEADOS VACÍA.")

    return promedioGeneral

def menuEmpleados():
    print("1. AÑADIR EMPLEADO.")
    print("2. ELIMINAR EMPLEADO.")
    print("3. MOSTRAR TODOS LOS EMPLEADOS.")
    print("4. BUSCAR EMPLEADO POR ID O NOMBRE.")
    print("5. CALCULAR SALARIO PROMEDIO POR DEPARTAMENTO.")
    print("6. CALCULAR SALARIO PROMEDIO GENERAL.")
    print("7. SALIR.")

def buscarEmpleado():

    global empleados
    global idEmpleado

    if comprobarEmpleados():
        while True:
            print("1. BUSCAR EMPLEADO POR ID.")
            print("2. BUSCAR EMPLEADO POR NOMBRE.")
            print("3. SALIR.")
            opcion = int(input("OPCION = "))
            while opcion < 1 or opcion > 3:
                print("ERROR! OOCIÓN INVÁLIDA. INGRESE LA OPCIÓN NUEVAMENTE.")
                opcion = int(input("OPCION = "))
            if opcion == 1:
                idEmpleadoBuscar = int(input("INGRESE EL ID DEL EMPLEADO A BUSCAR : "))
                while idEmpleadoBuscar < 0:
                    print("ERROR! ID INVÁLIDO. INGRESE EL ID NUEVAMENTE.")
                    idEmpleadoBuscar = int(input("INGRESE EL ID DEL EMPLEADO A BUSCAR : "))

                empleadoIdBuscar = [empleado for empleado in empleados if empleado[0] == idEmpleadoBuscar]

                if len(empleadoIdBuscar) == 0:
                    print("NO SE ENCONTRARON COINCIDENCIAS.")
                else:
                    for empleado in empleadoIdBuscar:
                        print(f"ID : {empleado[0]}, NOMBRE : {empleado[1]}, DEPARTAMENTO : {empleado[2]}, SALARIO : S/.{empleado[3]}")

            elif opcion == 2:
                nombreEmpleadoBuscar = input("INGRESE EL NOMBRE DEL EMPLEADO A BUSCAR : ")

                empleadoNombreBuscar = [empleado for empleado in empleados if empleado[1] == nombreEmpleadoBuscar]

                if len(empleadoNombreBuscar) == 0:
                    print("NO SE ENCONTRARON COINCIDENCIAS.")
                else:
                    print("SE ENCONTRARON COINCIDENCIAS.")
                    for empleado in empleadoNombreBuscar:
                        print(f"ID : {empleado[0]}, NOMBRE : {empleado[1]}, DEPARTAMENTO : {empleado[2]}, SALARIO : S/.{empleado[3]} ")
            elif opcion == 3:
                break
    else:
        print("ERROR! LISTA DE EMPLEADOS VACÍA.")



def mainEmpleados():

    global empleados
    global idEmpleado

    while True:
        menuEmpleados()
        opcionUsuario = int(input("OPCION : "))
        
        if opcionUsuario == 1:
            agregarEmpleados()
        elif opcionUsuario == 2:
            eliminarEmpleado()
        elif opcionUsuario == 3:
            mostarEmpleados()
        elif opcionUsuario == 4:
            buscarEmpleado()
        elif opcionUsuario == 5:
            print(f"EL PROMEDIO DEL SALARIO DEL DEPARTAMENTO ES : S/{calcularSalarioPromDepartamento()}")
        elif opcionUsuario == 6:
            print(f"EL PROMEDIO DEL SALARIO GENERAL ES : S/{salarioGeneral()}")
        elif opcionUsuario == 7:
            break
        else:
            print("ERROR! OPCIÓN INVÁLIDA. INGRESE LA OPCIÓN NUEVAMENTE.")
            opcionUsuario = int(input("OPCION : "))

mainEmpleados()