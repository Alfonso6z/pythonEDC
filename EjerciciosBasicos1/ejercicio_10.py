""" 
Ejercicio 10
Escribir un programa que pida al usuario una palabra y 
la muestre por pantalla 10 veces. """

palabra = input("Ingresa una palabra: ")

# Ciclo while
repetir = 0
while(repetir < 10):
    print(palabra)
    repetir += 1
    
print("---------")
# Ciclo for
for repeticion in range(10):
    print(palabra)
    