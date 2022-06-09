import random
class Telefono:
    def __init__(self,marca,capacidad,compania):
        print(f"Creaste un telefono {marca} ")
        self.__marca = marca
        self.__capacidad=capacidad
        self.__compania = compania
        self.__imai = random.randint(1111111111,9999999999)
    
    def setMarca(self,marca):
        self.__marca = marca
    def setCapacidad(self,capaciadad):
        self.__marca = capaciadad
    def setCompania(self,compania):
        self.__marca = compania
    def getMarca(self):
        return self.__marca
    def getCapacidad(self):
        return self.__capacidad
    def getCompania(self):
        return self.__compania
    def getIMAI(self):
        return self.__imai
    def llamaleA(self,telefono):
        print(f"Llamanado a ... {telefono.getMarca()}")
    
def main():
   
    t1 = Telefono("LG","128GB","Telcel")
    print(t1.getIMAI())
    t3 = Telefono("Nokia","256GB")
    print(t3.getIMAI())
    #t1.llamaleA(t3)
if __name__ == "__main__":
    main()