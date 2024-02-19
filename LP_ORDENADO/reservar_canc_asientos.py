import os
import time

asientosGeneral = []

for i in range(100):
    asientosGeneral.append([i + 1, 'D'])


def verAsientos():
    global asientosGeneral

    print("ASIENTO DISPONIBLE [D]; ASIENTO RESERVADO [R]\n")

    for j in range(len(asientosGeneral)):
        if asientosGeneral[j][0] < 10:
            print(f"[00{asientosGeneral[j][0]}][{asientosGeneral[j][1]}]", end=',')
        elif 10 <= asientosGeneral[j][0] < 100:
            print(f"[0{asientosGeneral[j][0]}][{asientosGeneral[j][1]}]", end=',')
        else:
            print(f"[{asientosGeneral[j][0]}][{asientosGeneral[j][1]}]", end=',')

        if asientosGeneral[j][0] % 10 == 0:
            print("\n")

    print("---------------------------------------PANTALLA------------------------------------------")


def reservarAsiento():
    global asientosGeneral

    verAsientos()

    asientoReservar = int(input("INGRESE EL NUMERO DE ASIENTO A RESERVAR : "))
    while asientoReservar <= 0 or asientoReservar > 100:
        print("ERROR! ASIENTO INVÁLIDO. INGRESE EL NÚMERO DE ASIENTO NUEVAMENTE.")
        asientoReservar = int(input("INGRESE EL NUMERO DE ASIENTO A RESERVAR : "))

    for k in range(len(asientosGeneral)):
        if asientosGeneral[k][0] == asientoReservar and asientosGeneral[k][1] == 'D':
            estado = 'R'
            asientosGeneral[k][1] = estado
            print("ASIENTO RESERVADO CORRECTAMENTE!")
        elif asientosGeneral[k][0] == asientoReservar and asientosGeneral[k][1] == 'R':
            print("NO SE PUEDE RESERVAR UN ASIENTO QUE YA ESTA RESERVADO")


def cancelarAsiento():
    global asientosGeneral

    verAsientos()

    asientoCancelar = int(input("INGRESE EL NUMERO DE ASIENTO A CANCELAR : "))
    while asientoCancelar <= 0 or asientoCancelar > 100:
        print("ERROR! ASIENTO INVÁLIDO. INGRESE EL NÚMERO DEL ASIENTO NUEVAMENTE.")
        asientoCancelar = int(input("INGRESE EL NUMERO DE ASIENTO A CANCELAR : "))

    for k in range(len(asientosGeneral)):
        if asientosGeneral[k][0] == asientoCancelar and asientosGeneral[k][1] == 'R':
            estado = "D"
            asientosGeneral[k][1] = estado
            print("ASIENTO CANCELADO CORRECTAMENTE!")
        elif asientosGeneral[k][0] == asientoCancelar and asientosGeneral[k][1] == 'D':
            print("NO SE PUEDE CANCELAR UN ASIENTO QUE NO ESTA RESERVADO.")




def mostrarEstadisticasOcupacion():
    global asientosGeneral
    porcentaje = 0

    asientosReservados = [asiento for asiento in asientosGeneral if asiento[1] == 'R']

    if len(asientosReservados) != 0:
        porcentaje = (len(asientosReservados) / 100) * 100

    return porcentaje


def menu():
    print("1. Visualizar asientos")
    print("2. Realizar reserva de asiento")
    print("3. Cancelar reserva de asiento")
    print("4. Mostrar estadísticas de ocupación (porcentaje de asientos ocupados, asientos  disponibles)")
    print("5. Salir.")


def main():
    global asientosGeneral

    while True:
        menu()
        opcUsuario = int(input("OPCIÓN : "))       
        if opcUsuario == 1:
            verAsientos()
            time.sleep(5)
            os.system('cls')
        elif opcUsuario == 2:
            reservarAsiento()
            time.sleep(5)
            os.system('cls')
        elif opcUsuario == 3:
            cancelarAsiento()
            time.sleep(5)
            os.system('cls')
        elif opcUsuario == 4:
            print(f"PROCENTAJE DE ASIENTOS RESERVADOS : {mostrarEstadisticasOcupacion()}%")
            print(f"PROCENTAJE DE ASIENTOS DISPONIBLES : {100 - mostrarEstadisticasOcupacion()}%")
            time.sleep(3)
            os.system('cls')
        elif opcUsuario == 5:
            break
        else:
            print("ERROR! OPCIÓN INVÁLIDA. INGRESE LA OPCIÓN NUEVAMENTE.")
            opcUsuario = int(input("OPCIÓN : "))


if __name__ == '__main__':
    main()