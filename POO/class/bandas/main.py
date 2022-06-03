from banda import Banda
def main():
    
    banda1 = Banda("Van Halen")
    print(banda1.getNombre())
    banda1.setIntegrantes(["Eddie","Alex","David","Michael"])
    print(banda1.getIntegrantes())
    banda1.setGenero("Hard Rock")
    print(banda1.getGenero())
    
if __name__ == "__main__":
    main()