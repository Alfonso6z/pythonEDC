class Primo:

    def __init__(self):
        print("Has creado un objeto de la clase Primo")
        
    def esPrimo(self,p):
        # Es mi programa para verificar que un número es primo
        cont = 0 # contar entre cuantos números es divisible
        for i in range(2,p+1):
            if p % i == 0:# verifica que es divisible
                cont+=1
        if cont == 1:
            return (True)
        else:
            return (False)

    def primoRango(self,n):
        lista_primos = []
        for i in range(2,n+1):
            if self.esPrimo(i):
                lista_primos.append(i)
        return lista_primos

# def primo(p):
    #     # Es mi programa para verificar que un número es primo
    #     cont = 0 # contar entre cuantos números es divisible
    #     for i in range(p,2,-1):
    #         print(f" p = {p} mod {i} = {p%i}")
    #         if p % i == 0:# verifica que es divisible
    #             cont+=1
    #             print(f" p = {p} es divisible entre = {i}")
    #     print(f"el contador es = ",cont)
    #     if cont == 1:
    #         print(f" el número {p} es primo")
