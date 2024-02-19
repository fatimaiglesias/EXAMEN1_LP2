import random

def generar_numero_aleatorio():
    return random.randint(1, 100)

def pedir_adivinanza():
    while True:
        try:
            adivinar = int(input("Adivina el número (entre 1 y 100): "))
            return adivinar
        except ValueError:
            print("Por favor, ingresa un número válido.")

def comparar_numeros(num_generado, num_adivinado):
    if num_adivinado < num_generado:
        print("El número que has ingresado es menor.")
    elif num_adivinado > num_generado:
        print("El número que has ingresado es mayor.")
    else:
        print("¡Felicidades! Has adivinado el número.")
        return True
    return False

def jugar():

    print("------------------JUEGA A ADIVINAR EL NUMERO----------------")
    numero_aleatorio = generar_numero_aleatorio()
    intentos = 0
    max_intentos = int(input("digite max de intentos: "))

    while intentos < max_intentos:
        intentos += 1
        adivinar = pedir_adivinanza()
        if comparar_numeros(numero_aleatorio, adivinar):
            print("Número de intentos:", intentos)
            return
    print("Lo siento, has alcanzado el límite de intentos. El número era:", numero_aleatorio)

if __name__ == "__main__":
    jugar()