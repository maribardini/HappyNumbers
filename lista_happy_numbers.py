print('Bienvenidos!\nIngrese un número para indicarle al sistema\nhasta qué dígito chequear si es o no un Happy Number\ny que arroje los resultados.')
cant = int(input('Ingrese un número: '))

def CantidadHappyNumbers():
	print("Éstos son los números felices solicitados:")
	digit = 0
	while digit <= cant:
		new = str(digit)
		HappyNumbers(new)
		digit += 1

def HappyNumbers(new):
	num = new
	check = set()
	while 1:
		if num == 1:
			print (new, "Happy Number!")
			break
		num = sum(int(c)**2 for c in str(num))
		if num in check:
			break
		check.add(num)
		
CantidadHappyNumbers()