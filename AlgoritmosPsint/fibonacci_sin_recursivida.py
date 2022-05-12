""" 
Hacer un algoritmo en Pseint para calcular la serie de Fibonacci

Entrada:
    número -> es la posición en la sucesion de fibonacci
    ejemplo:
        0,1,1,2,3,5,8,13,21,34
Salida:
    posición en la sucesión de fibo
Algoritmo:
    1. pedir número n
    2. Si n = 0, entonces regresar 0 sino paso 3
    3. si n = 1, entonces regresar 1 sino paso 4
    4. si n>1, entonces sumar
    5. mostra
fin     
"""
# pedir un número y pasarlo a int
n = int(input("ingrsa un número: "))

# casos base
x0 = 0
x1 = 1

#  posicióm 0
if n == 0:
    print("[0]")
# posición 1
elif n == 1:
    print("[0,1]")
# posición mayor a 1
else:
    fib = "[0,1"
    for i in range(2,n+1):
        x2 = x0 + x1
        fib = f"{fib},{x2}"
        x0 = x1
        x1 = x2
    print(f"{fib}]")