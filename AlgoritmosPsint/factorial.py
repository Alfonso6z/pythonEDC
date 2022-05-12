'''
Hacer un algoritmo en Pseint que permita calcular el factorial de un número.
Entradas:
    número
Salida:
    factorial(número)

Algoritmo:
    1. solicitar número
    2. guardarlo
    3. multiplicar (n*(n-1)*(n-2),..*(n-n-1))
        (1*2*3*...*n)
    4. mostrar el factorial
'''

# solicitar un número , casting a int
# NOTE: todo lo que se ingresa por consola es de tipo str
n = int(input("ingresa un número: "))

""" 
 si n = 5
 1*2*3*4*5
 si n = 10
 1*2*3*4*5*6*7*8*9*10
"""
f=1
for i in range(1,n+1):
    f=f*i
print(f"El factorial de {n} es = {f}")