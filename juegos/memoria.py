import random

def memoria():
    
	cant_num = random.randint(10,20)
	final = ""
	for i in range(cant_num):
		nuevo = random.randint(1,1000)
		print(nuevo)
		final = final + str(nuevo) + " "
	
	final = final[:-1]
	print("Ahora escribe los numeros dictados separados por un espacio")
	intento = input(str())

	if intento == final:
		print("CORRECTO!!")
	else:
		print("TE EQUIVOCASTE")
	
	pass