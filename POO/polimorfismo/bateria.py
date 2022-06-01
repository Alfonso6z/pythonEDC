class Bateria:
    def __init__(self,tipo,marca,clasificacion):
        # privados
        self.__tipo = tipo
        self.__marca = marca
        self.__clasificacion = clasificacion
        # publico
        self.genero = None
    
    def setTipo(self,tipo):
        self.__tipo = tipo
    def getTipo(self):
        return self.__tipo