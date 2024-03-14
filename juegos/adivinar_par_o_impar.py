import random

def adivinar_par_o_impar():

    numero = random.randint(0,2)
    print("Elije par o impar")
    acierto = input()

    if numero == 1:
        correcto = "impar"
    else:
        correcto = "par"

    while True:
        if acierto == correcto:
            print("Acertaste!")
            break
        else:
            print("Te equivocaste")
            break
    pass