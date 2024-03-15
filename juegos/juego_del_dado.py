import random

def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    ptos_usuario = 0
    ptos_cpu = 0
    win = False
    while win == False:
        print("Presiona enter para tirar el dado")
        enter = input()
        
        dado_usuario = random.randint(1,6)
        print(f"Sacaste: {dado_usuario}")
        ptos_usuario += dado_usuario

        if ptos_usuario >= 30:
            print("Ganaste!")
            win = True
            break

        dado_cpu = random.randint(1,6)
        print(f"Cpu saco: {dado_cpu}")
        ptos_cpu += dado_cpu

        if ptos_cpu >= 30:
            print("Perdiste :(")
            win = True