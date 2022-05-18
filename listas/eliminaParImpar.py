'''
LLenar una lista con números pseudoaleatorios y eliminar todos los numeros
pares o impares
'''

# Libreria para usar números aleatorios
import random

# pedir el tamaño de la lista
n = int(input("Ingresa el tamaño de la lista: "))
# llenar la lista con números aleatorias del 1 al 100
lista = [random.randint(1,100) for i in range(n)]
# mostrar lista inicial
print(lista)
# pregunatar si quieren eliminar pares o impares, p es para verificar el modulo
p = int(input("Eliminar impares(1) o pares(2) ? "))
# contador para recorrer la lista
cont = 0
# elimina los pares
if p == 2:
    # mientras no llegue al final de la lista
    while(cont<len(lista)):
        # verificar si es par
        if lista[cont] % 2 == 0:
            # eliminar el elemento
            lista.pop(cont)
        else:
            # aumentar contador si no se elimina el elemento
            cont=cont+1
else: # elimina impares
    while(cont<len(lista)):
        # verificar si es par o impar 
        if lista[cont] % 2 != 0:
            # eliminar el elemento
            lista.pop(cont)
        else:
            # aumentar contador si no se elimina el elemento
            cont+=1
# imprimir lista final
print(lista)