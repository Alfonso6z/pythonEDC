'''
Hacer un algoritmo en Pseint para calcular la media de los números pares e impares, 
sólo se ingresará diez números.

    Entrada: 10 números enteros.
    Salida: promedio_pares y promedio_impares
Algoritmo:
    1.- Pedir los 10 números
    2.- contar y sumar los pares y los impares
    3.- calcular el promedio de los pares e impares
FinAlgoritmo
'''
def promedio(suma,cantidad):
    if cantidad!=0:
        return suma/cantidad
    else:
        return "no aplica"

def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def promedio_par_e_impar(numeros:list):
    cont_p = 0
    cont_i = 0
    suma_p = 0
    suma_i = 0
    for n in numeros:
        if es_par(n):
            cont_p+=1
            suma_p+=n
        else:
            cont_i+=1
            suma_i+=n
    return promedio(suma_p, cont_p),promedio(suma_i, cont_i)

def pide_n_numeros(n):
    lista = []
    for i in range(n):
        dato = int(input(f"Ingresa el número {i+1}:  "))
        lista.append(dato)
    return lista

def main():
    n = int(input("Ingresa la cantidad de números: "))
    lista_n = pide_n_numeros(n)
    prom_p,prom_i = promedio_par_e_impar(lista_n)
    print(f'''
    El promedio de los números pares = {prom_p}
    El promedio de los números impares es = {prom_i}''')
if __name__ == "__main__":
    main()
