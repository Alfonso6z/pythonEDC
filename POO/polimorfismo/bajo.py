class Bajo:
    def __init__(self,tipo,marca,clasificacion):
        # privados
        self.__tipo = tipo
        self.__marca = marca
        self.__clasificacion = clasificacion
        # publico
        self.genero = None
    # modifica atributo privado
    def setTipo(self,tipo):
        self.__tipo = tipo
    # retorna atributo privado
    def getTipo(self):
        return self.__tipo
    def hola(self):
        print("Privado")