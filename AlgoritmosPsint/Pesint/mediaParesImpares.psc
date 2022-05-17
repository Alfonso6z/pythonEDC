Algoritmo mediaParesImpares
	// Hacer un algoritmo en Pseint para calcular
	//la media de los n�meros pares e impares,
	//s�lo se ingresar� diez n�meros.
	// Entradas: 10 n�meros
	// Salidas: promedioPares y promedioImpares
	// restricci�n: 
	//		tienen que ser n�meros positivo
	//		no se puede dividir entre cero ( contar 0 pares o 0 impares)
	contP = 0 // contador de pares
	contI = 0 // contador de impares
	sumaP = 0 // acumula pares
	sumaI = 0 // acumula impares
	Para n=1 hasta 10 Hacer
		// Entrada
		Escribir "Ingresa el n�mero: ",n
		Leer dato
		Si dato mod 2 = 0 Entonces // Es par
			contP = contP + 1 // contar pares
			sumaP = sumaP + dato // sumar pares
		SiNo // Es impar
			contI = contI + 1 // contar impares cont+=1 cont=+1
			sumaI = sumaI + dato // suma los impares
		FinSi
	FinPara
	// Sacar los promedios
	// Verificar que hay n�mero pares
	Si contP <> 0 Entonces
		promP = sumaP/contP
		Escribir "# ", contP,"El promedio de los n�meros pares es = ",promP
	Sino
		Escribir "NO SE INGRESAR�N N�MERO PARES"
	FinSi
	// Verificar que hay n�mero impares
	Si contI <> 0 Entonces
		promI = sumaI/contI
		Escribir "# ", contP,"El promedio de los n�meros impares es = ",promI
	SiNo
		Escribir "NO SE INGRESAR�N N�MERO IMPARES"
	FinSi
FinAlgoritmo
