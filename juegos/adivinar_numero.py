import random

def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    win = False
    while win == False:
        numero = random.randint(1,10)
        respuesta = int(input("Adivina el numero: "))

        if respuesta == numero:
            win = True
        else:
            print("Incorrecto")
    
    print("Adivinaste el numero")

    