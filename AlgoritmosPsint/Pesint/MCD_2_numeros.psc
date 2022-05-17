Algoritmo MCD_2_numeros
	//Hacer un algoritmo en Pseint para conseguir el M.C.D
	// de dos n�meros por medio del algoritmo de Euclides.
	// Entrada: 2 n�meros
	// Salidas: MCD 
	// Restriccion: n�meros positivos enteros
	
	// Entradas
	Escribir "Escribir el primer n�mero"
	Leer n1
	Escribir "Escribir el segundo n�mero"
	Leer n2
	
	// saber quien es el m�s grande
	si n1 > n2 Entonces
		dividendo = n1
		divisor = n2
	sino
		dividendo = n2
		divisor = n1
	FinSi
	
	Repetir
		// recuperar el resto
		resto = dividendo mod divisor
		si resto <> 0 Entonces // iteramos
			dividendo = divisor
			divisor = resto
		FinSi
	Hasta Que resto = 0 // cuando es resto es 0
	
	// El ultimo divisor
	Escribir "El m�ximo comun divisor es el ", divisor
	
FinAlgoritmo
