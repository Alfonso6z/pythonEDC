from typing import Any
class Persona():
    
    # constructor o instanciador
    def __init__(self,nombre,edad,estatura):
        print(f"Nacio {nombre}")
        self._nombre = nombre
        self._edad = edad
        self._estatura = estatura
        self._conyuge:Persona = None
    
    # comportamiento hablar
    def hablar(self,mensaje):
        print(f"{self._nombre}: {mensaje}")
    
    def pedirMatrimonio(self,conyuge):
        self._conyuge = conyuge
        print(f"{self._nombre} se caso con {conyuge._nombre}")
    
    def quienEsTuEsposo(self):
        if self._conyuge:
            print(f"{self._nombre}: Mi conyuge es {self._conyuge._nombre}")
        else:
            print("Estoy solter@")