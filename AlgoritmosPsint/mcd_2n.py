""" 
Algoritmo MCD_2_numeros
Hacer un algoritmo en Pseint para conseguir el M.C.D
de dos números por medio del algoritmo de Euclides.
Entrada: 2 números
Salidas: MCD 
Restriccion: números positivos enteros 
datos prueba: 1254, 14445

"""

# Entradas
n1 = int(input("Escribir el primer número :"))
n2 = int(input("Escribir el segundo número :"))
resto = 6
# saber quien es el más grande
if n1 > n2:
	dividendo = n1
	divisor = n2
else:
	dividendo = n2
	divisor = n1

# do while en python usando break
while True:
	# recuperar el resto
	resto = dividendo % divisor
	if (resto==0):
		break
	dividendo = divisor
	divisor = resto 

""" while resto != 0:
	# recuperar el resto    
	resto = dividendo % divisor
	if (resto != 0):
		dividendo = divisor
		divisor = resto """ 

# El ultimo divisor
print("El máximo comun divisor es el ", divisor)