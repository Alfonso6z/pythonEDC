from vehiculo import Vehiculo
from motocicleta import Motocicleta
from cuatrimoto import Cuatrimoto
def main():
    # crear objeto
    moto = Motocicleta("Gasolina","120 Km/h")
    # moto.set_tipo_motor("De Gasolina")
    moto.tipo_motor = "De Gasolina"
    # print(moto.tipo_motor()) 
    print(moto.tipo_motor)
    
    # moto propiedades o atributos
    moto.numero_llantas = 2
    moto.energia = 101
    moto.tipo_combustible = "de la verde"
    moto.cantidad_p = 2
    for i in range(101):
        moto.andar()
    moto.andar()
    print(moto)
    
    cuatri = Cuatrimoto("Gasolina", "80 Km/h")
    
if __name__ == "__main__":
    main()