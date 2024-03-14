import random

def ganador(player1,player2):
    
    if player1 == player2:
        return False
    
    if player1 == "piedra":
        if player2 == "papel":
            return False
        elif player2 == "tijeras":
            return True
    if player1 == "papel":
        if player2 == "piedra":
            return True
        elif player2 == "tijeras":
            return False
    if player1 == "tijeras":
        if player2 == "papel":
            return True
        elif player2 == "piedra":
            return False

def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    win = False
    
    while win == False:
        cpu = random.randint(1,3)
        opciones = ["piedra", "papel", "tijeras"]

        opcion_cpu = opciones[(cpu - 1)]

        user = (input()).lower()

        print(f"{opcion_cpu} vs {user}")

        if ganador(user, opcion_cpu):
            win = True
        else:
            print("No ganaste")
    
    print("Ganaste!!")

