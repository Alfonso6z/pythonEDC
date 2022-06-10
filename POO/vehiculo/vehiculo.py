class Vehiculo:
    def __init__(self,tipo_motor,velocidad):
        self.__tipo_motor = tipo_motor
        self.__velocidad = velocidad
        self.__numero_llantas = None
        self.__energia = 0
        self.__tipo_combustible = None
        self.__cantidad_p = None
    
    # getters y setters de tipo motor
    @property # equivale a un get
    def tipo_motor(self):
        return self.__tipo_motor
    
    @tipo_motor.setter # equivale set
    def tipo_motor(self,tipo_motor):
        self.__tipo_motor = tipo_motor
    
    @tipo_motor.deleter # eliina un atributo    
    def tipo_motor(self):
        del self.__tipo_motor
    
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self,velocidad):
        self.__velocidad = velocidad
    
    
    
    @property
    def numero_llantas(self):
        return self.__numero_llantas
    
    @numero_llantas.setter
    def numero_llantas(self,numero_llantas):
        self.__numero_llantas = numero_llantas
    
    
    
    @property
    def energia(self):
        return self.__energia
    @energia.setter
    def energia(self,energia):
        self.__energia = energia


    @property
    def tipo_combustible(self):
        return self.__tipo_combustible
    @tipo_combustible.setter
    def tipo_combustible(self,tipo_combustible):
        self.__tipo_combustible = tipo_combustible


    @property
    def cantidad_p(self):
        return self.__cantidad_p
    @cantidad_p.setter
    def cantidad_p(self,cantidad_p):
        self.__cantidad_p = cantidad_p
    
    def __vaciar_combustible(self,cantidad):
        self.__energia = self.__energia - cantidad
    
    def andar(self):
        if self.__energia>0:
            self.__vaciar_combustible(1)
        else:
            print("No arranca... ")
    
    def llenar_combustible(self,cantidad):
        self.__energia + cantidad
    
    
    def transportar_persona(self,personas):
        if self.__cantidad_p >= personas:
            self.__cantidad_p = self.__cantidad_p - personas
            print(f"Asientos disponibles: {self.__cantidad_p}")
        else:
            print("Esta lleno")

    def __str__(self):
        return f'''
tipo_motor = {self.__tipo_motor}
velocidad = {self.__velocidad}
numero_llantas = {self.__numero_llantas}
energia = {self.__energia}
tipo_combustible = {self.__tipo_combustible}
cantidad_p = {self.__cantidad_p}
'''