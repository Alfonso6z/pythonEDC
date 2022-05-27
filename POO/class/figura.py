# crear clase figura
class Figura():
    # constructor o instanciador
    def __init__(self):
        self._lados = None

    @property # getter = Regresa el valor de _lados
    def lados(self):
        return self._lados # retrona lados

    @lados.setter # setter = Cambia valor de _lados
    def lados(self,valor):
        # mi regla de la clase
        if valor>2:
            self._lados = valor
        else:
            print("No pudes poner los lados menores a 3")
            self._lados = None

    @lados.deleter # Elimina el atributo lados
    def lados(self):
        del self._lados
        
def main():
    # instanciando o creando un objeto
    triangulo = Figura()
    # aqui nace el objeto
    cuadrado = Figura()

    # cambiando el valor de su atributo lados
    triangulo.lados = 3
    cuadrado.lados = 4
    
    # elimino su atributo lados
    # del cuadrado.lados
    
    print(f" soy triangulo y tengo {triangulo.lados} lados")
    print(f" soy cuadrado y tengo {cuadrado.lados} lados")
    
if __name__ == "__main__":
    main()