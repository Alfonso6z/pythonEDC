from animal import Animal
from gato import Gato
from perro import Perro
from cocodrilo import Cocodrilo
def main():
    # crear objetos
    animal1 = Animal()
    animal2 = Gato("Sir Lancelot")
    animal3 = Perro("Solovino")
    animal4 = Cocodrilo()
    
    
    animal2.hablar("raul")
    animal2.ronronea()
    animal2.setClasificacion("Mamifero")
    print(animal2.clasificacion)
    
    animal3.hablar("ahuuuuuuuu")
    animal3.ladra()
    animal3.setClasificacion("Mamifero")
    print(animal3.clasificacion)
    
    animal4.setAlimentacion("Personas")
    animal4.setClasificacion("Oviparo")
    animal4.setEcosistema("Pantano")
    print(animal4.alimentacion)
    print(animal4.ecosistema)
    print(animal4.clasificacion)

if __name__ == "__main__":
    main()