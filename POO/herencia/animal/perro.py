from animal import Animal
from mascota import Mascota
class Perro(Mascota,Animal):
    
    def ladra(self):
        print(f"{self.nombre}: guau guau!")