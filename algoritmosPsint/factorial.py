''' 
Hacer un algoritmo en Pseint que permita calcular el factorial de un número.
    Entrada: un número n
    salida: n! = 1*2*3*4* ... *n
            n! = n*(n-1)*(n-2)* ... * 1
            5! =  5*4!
            4! = 1*2*3*4
'''
def factorial(n):
    if n == 0:
        return 1
    # recursividad
    return n * factorial(n-1)

def fac(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f

def main():
    n = int(input("Ingresa un número: "))
    print(f"{n}! = {fac(n)}")
    print(f"{n}! = {factorial(n)}")
if __name__ == "__main__":
    main()