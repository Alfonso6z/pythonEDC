Algoritmo MCD_2_numeros
	//Hacer un algoritmo en Pseint para conseguir el M.C.D
	// de dos números por medio del algoritmo de Euclides.
	// Entrada: 2 números
	// Salidas: MCD 
	// Restriccion: números positivos enteros
	
	// Entradas
	Escribir "Escribir el primer número"
	Leer n1
	Escribir "Escribir el segundo número"
	Leer n2
	
	// saber quien es el más grande
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
	Escribir "El máximo comun divisor es el ", divisor
	
FinAlgoritmo
