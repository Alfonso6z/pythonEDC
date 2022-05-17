'''
Algoritmo: mediaParesImpares
Hacer un algoritmo en Pseint para calcular la media de los números pares e impares,
sólo se ingresarán diez números.
Entradas: 10 números
Salidas: promedioPares y promedioImpares
restricción: 
	tienen que ser números positivo
	no se puede dividir entre cero ( contar 0 pares o 0 impares)'''
contP = 0 # contador de pares
contI = 0 # contador de impares
sumaP = 0 # acumula pares
sumaI = 0 # acumula impares

for i in range(10):
	# Entrada
	dato = int(input(f"Ingresa el número {i+1} :  "))
	if dato % 2 == 0: # Es par
		contP+=1 # contar pares
		sumaP = sumaP + dato # sumar pares
	else: # Es impar
		contI = contI + 1 # contar impares cont+=1 cont=+1
		sumaI = sumaI + dato # suma los impares
  
# Sacar los promedios
# Verificar que hay número pares
if contP != 0:
	promP = sumaP/contP
	print("#", contP,"  El promedio de los números pares es = ",promP)
else:
	print( "NO SE INGRESARON NÚMERO PARES")
# Verificar que hay número impares
if contI != 0:
	promI = sumaI/contI
	print( "#", contI,"   El promedio de los números impares es = ",promI)
else:
	print( "NO SE INGRESARON NÚMERO IMPARES")