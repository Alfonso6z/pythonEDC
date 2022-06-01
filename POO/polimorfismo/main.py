from bateria import Bateria
from guitarra import Guitarra
from teclado import Teclado
from bajo import Bajo
from instrumento import Instrumento

def main():
    print("Hola mundo")
    drums = Bateria("percución", "Perl", "Rock")
    bass = Bajo("cuerda", "tobyas", "Jazz")
    guitar = Guitarra("cuerda", "Fernder", "Blues")
    keyboard = Teclado("tecla", "Yamaha", "80's")
    intrumento = Instrumento(None,None, None)
    print(intrumento == guitar)
    
    print(bass.getTipo())
    bass.setTipo("Cuerdas gruesas")
    print(bass.getTipo())
    bass.genero = "lo que sea"
    print(bass.genero)
    
if __name__ == "__main__":
    main()