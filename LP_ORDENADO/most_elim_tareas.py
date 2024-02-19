tareas = []
numTarea = 1

def menu():
    print("1. AÑADIR TAREA.")
    print("2. ELIMINAR TAREA.")
    print("3. MOSTRAR TODAS LAS TAREAS.")
    print("4. MARCAR TAREA COMO COMPLETADA.")
    print("5. SALIR.")


def comprobarTarea():

    global tareas

    if len(tareas) == 0:
        return False
    else:
        return True

def agregarTarea():

    global tareas
    global numTarea

    print("----------DATOS TAREA----------")
    nombreTarea = input("NOMBRE : ")
    descipcionTarea = input("DESCRIPCIÓN : ")
    estadoTarea = 'PENDIENTE'

    tareas.append([numTarea,nombreTarea,descipcionTarea,estadoTarea])

    return 1

def mostrarTareas():

    global tareas
    global numTarea

    if comprobarTarea():
        for tarea in tareas:
            print(f"TAREA NUMERO-{tarea[0]}")
            print(f"NOMBRE      : {tarea[1]}")
            print(f"DESCRIPCIÓN : {tarea[2]}")
            print(f"ESTADO      : {tarea[3]}")
            print("\n")
    else:
        print("NO HAY TAREAS POR MOSTAR")

def eliminarTarea():

    global tareas
    global numTarea

    if comprobarTarea():
        mostrarTareas()
        opcionTarea = int(input("INGRESE EL NUMERO DE LA TAREA A ELIMINAR : "))

        while opcionTarea < 0:
            print("ERROR! OPCIÓN INVÁLIDA. INGRESE EL NÚMERO NUEVAMENTE.")
            opcionTarea = int(input("INGRESE EL NUMERO DE LA TAREA A ELIMINAR : "))

        for tarea in tareas:
            if tarea[0] == opcionTarea:
                tareas = [tarea for tarea in tareas if tarea[0] != opcionTarea]
            else:
                print("NO SE ENCONTRÓ LA TAREA A ELIMINAR.")
    else:
        print("NO HAY TAREAS POR ELIMINAR")

def marcarTarea():

    global tareas
    global numTarea

    if comprobarTarea():
        mostrarTareas()
        opcionTarea = int(input("INGRESE EL NUMERO DE LA TAREA A MARCAR : "))

        while opcionTarea < 0:
            print("ERROR! OPCIÓN INVÁLIDA. INGRESE EL NÚMERO NUEVAMENTE.")
            opcionTarea = int(input("INGRESE EL NUMERO DE LA TAREA A MARCAR : "))

        for i in range(len(tareas)):
            if tareas[i][0] == opcionTarea:
                print("TAREA COMPLETADA? (SÍ (1) O NO (0) )")
                respuesta = int(input("RESPUESTA : "))

                while respuesta < 0 or respuesta > 1:
                    print("ERROR! RESPUESTA INVÁLIDA. INGRESE NUEVAMENTE SU RESPUESTA.")
                    print("TAREA COMPLETADA? (SÍ (1) O NO (0) )")
                    respuesta = int(input("RESPUESTA : "))

                if respuesta == 1:
                    tareas[i][3] = 'COMPLEATADA'
                    print("TAREA MODIFICADA CORRECTAMENTE.")
                    print(f"TAREA NUMERO-{tareas[i][0]}")
                    print(f"NOMBRE      : {tareas[i][1]}")
                    print(f"DESCRIPCIÓN : {tareas[i][2]}")
                    print(f"ESTADO      : {tareas[i][3]}")
                    print("\n")
                elif respuesta == 2:
                    tareas[i][3] = 'PENDIENTE'
                    print("TAREA MODIFICADA CORRECTAMENTE.")
                    print(f"TAREA NUMERO-{tareas[i][0]}")
                    print(f"NOMBRE      : {tareas[i][1]}")
                    print(f"DESCRIPCIÓN : {tareas[i][2]}")
                    print(f"ESTADO      : {tareas[i][3]}")
                    print("\n")
    else:
        print("NO SE ENCONTRÓ LA TAREA A ELIMINAR.")




def main():

    global tareas
    global numTarea

    while True:
        menu()
        opcion = int(input("OPCIÓN : "))
                    
        if opcion == 1:
            numTarea += agregarTarea()
        elif opcion == 2:
            eliminarTarea()
        elif opcion == 3:
            mostrarTareas()
        elif opcion == 4:
            marcarTarea()
        elif opcion == 5:
            break
        else:
            print("ERROR! OPCIÓN INVÁLIDA. INGRESE LA OPCIÓN NUEVAMENTE.")
            opcion = int(input("OPCIÓN : "))


if __name__ == '__main__':
    main()