# Ejercicio 8: Ingresar dos números y mostrar el menor de ellos

n1 = int(input("Ingresar el primer número: "))
n2 = int(input("Ingresar el segundo número: "))

if n1 < n2:
    print(f"El {n1} es menor que el {n2}")
elif n1 == n2:
    print("Son iguales")
else:
    print(f"El {n2} es menor que el {n1}")