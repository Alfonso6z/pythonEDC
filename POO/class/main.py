from persona import Persona
from figura import Figura
def main():
    persona1 = Persona("Monse", 26, 1.58)
    persona2 = Persona("Juan", 35, 1.80)
    
    persona1.hablar(f"Hola {persona2._nombre}!")
    persona2.hablar(f"Hey,Que tal como te llamas?")
    persona1.hablar(f"My name is {persona1._nombre}")
    persona2.hablar(f"Te quieres casar conmigo?")
    persona1.hablar(f"yes")
    persona1.pedirMatrimonio(persona2)
    persona1.quienEsTuEsposo()
    persona2.quienEsTuEsposo()
        
if __name__ == "__main__":
    main()