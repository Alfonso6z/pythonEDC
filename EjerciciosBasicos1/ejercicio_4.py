""" 
Ejercicio 4
Escribir un programa que pregunte el nombre del usuario en la consola 
y un número entero e imprima por pantalla en líneas distintas el nombre del usuario 
tantas veces como el número introducido. 
"""

nombre = input("Ingresa tu nombre: ")
numero = int(input("Ingresa un número: "))

# Concatenando un salto de línea
print((nombre + "\n") * numero)

# Ciclo while
print("--- Con ciclo while ---")
numero_aux = numero
while(numero_aux > 0):
    print(nombre)
    numero_aux -= 1

# Ciclo for
print("--- Con ciclo for ---")
for repeticion in range(numero):
    print(nombre)
    