""" 
Ejercicio 15: Escribir un programa que muestre por pantalla la tabla de 
multiplicar del 1 al 10. 
"""
# for {variabla inicial} in range(valorInicial,valorFinal,paso)
for i in range(1,11):
    print(f"TABLA DEL {i}")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
