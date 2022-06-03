class Banda:
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__integrantes = []
        self.__genero = None
        self.__spotify = True
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setIntegrantes(self,integrantes):
        self.__integrantes = integrantes
    def getIntegrantes(self):
        return self.__integrantes
    def setGenero(self,genero):
        self.__genero = genero
    def getGenero(self):
        return self.__genero