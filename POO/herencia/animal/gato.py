from animal import Animal
from mascota import Mascota

class Gato(Mascota,Animal):
    def ronronea(self):
        print(f"{self.nombre}:rrrrrrrrrrrrrrrrrrrrrr ^=°=^ !")