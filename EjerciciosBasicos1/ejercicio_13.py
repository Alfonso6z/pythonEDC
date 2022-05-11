
# *Ejercicio 13: Escribir un programa que pida al usuario un número entero positivo
# *y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Ingresar número: "))

if numero > 0:
    # Ciclo while
    c = numero
    while(c >= 0):
        print(c, end=", ")
        c -= 1
    print("-----")
    # Ciclo for 
    for c in range(numero, -1, -1):
        print(c, end =", ")
else:
    print("Error: ingresa un número positivo")