'''
Hacer un algoritmo en Pseint para calcular la suma de los n primeros números
    Entrada: n números
    Salida: suma de los n números
'''
cont = 0
suma = 0
while True:
    n = float(input(f"Ingresa el número {cont+1}: "))
    if n<0:
        break
    suma+=n
    cont+=1
print(f"la suma de los {cont} es = {suma}")
