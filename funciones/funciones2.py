import os
import time
def bienvenidos():
    print("                             ")
    print("******************************")
    print("*       BIENVENIDO           *")
    print("******************************")
    print("Iniciando programa ...")
    time.sleep(2)    
    os.system ("cls")

def saludo():
    for i in range(10):
        print("Program iniciado")
        print(f"El progrmatermina en {10-i}s")
        time.sleep(1)
        os.system("cls")
# ejecutando funciones
bienvenidos()
saludo()
print("Adios ...")