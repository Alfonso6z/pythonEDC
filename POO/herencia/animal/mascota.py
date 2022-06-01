class Mascota:

    def __init__(self,nombre):
        self.nombre = nombre
        self.vacuna = None
        print(f"Hola {nombre} bienvenido XB")

    def hablar(self,sonido):
        print(f"{self.nombre}: {sonido}!")

    def vacunas(self, vacuna:bool):
        self.vacuna = vacuna