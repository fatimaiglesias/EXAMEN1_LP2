#hacer un cajero igual a la practica 3, pero este te tiene que pedir la 
# cantidad a retira o deporitar con el numero de billetes

saldo = 0
while True:
    print("""Bienvenido al menu del cajero:
            1) Consultar saldo
            2) Hacer Deposito
            3) Hacer Retiro
            4) Salir.""")
    decision = int(input("Que accion desearealizar: "))

    if decision == 1:
        print(f"Usted tiene {saldo} soles")
    elif decision == 2:
        billetes = ['10', '20', '50', '100', '200']
        lista = []

        for i in range(len(billetes)):
            lista.append(int(input(f'Cuantos billetes de {str(billetes[i])} va a ingresar: ')))

        print("Gracias por su transaccion")


        for i in range(len(billetes)):
            saldo += lista[i]*int(billetes[i])
            
    elif decision == 3:
        retiro = int(input("Cuanto va a retirar"))
        saldo += -(retiro)

        print("Que tenga un buen dia")

    elif decision == 4:
        print("Gracias por su preferencia")
        break
    else:
        print("Por favor elija una decision valida")



