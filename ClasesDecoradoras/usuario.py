def usuario_decorador():
    def super_usuario(cls):
        
        class SuperUsuario(cls):
            
            def getNombreCompleto(self):
                return f"{self.getNombre()} {self.getApellido()}"
            
            def __str__(self):
                return f"Hola, mi nombre completo es: {self.getNombreCompleto()}"
            
        return SuperUsuario
    return super_usuario


@usuario_decorador()
class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido


def main():
    u1 = Usuario("Juan","Hernandez")
    print(u1.getNombreCompleto())
    print(u1)
if __name__ == "__main__":
    main()