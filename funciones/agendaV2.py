"""
crear una agenda: que contenga nombre, telefono, colonia, mascota favoria, signo zodiacal
se tiene que consultar ingresar borrar modificar
"""
def menu(titulo,*opt,**mensajes):
    # imprime titulo
    if mensajes["primera_vez"]:
        print("**********************************************")
        print(f"        BIENVENIDO a {titulo}       ")
        print("**********************************************")
    # imprime opciones
    for i in range(len(opt)):
        print(f"{i+1}) {opt[i]}")
    opc = int(input("Seleciona una opción:  "))
    if opc>=1 and opc <=len(opt):
        return opc
    else:
        print(mensajes["error"])
        return -1

# TODO: Crear función para agregar un contacto a la agenda chida
def agregar_contacto():
    print("Agregar contacto desde la función agregar_contacto()")

def agenda(agenda_old):
    # bandera - bool
    continuar = True
    # primera vez
    p = True
    #while del programa Agenda
    while(continuar): # not salir = True
        # menu while del menu
        while(True):
            opt = menu(
                "Agenda chida",
                "Agregar",
                "Buscar",
                "Editar",
                "Borrar",
                "Salir",
                error="Elejiste una opción incorreta XD",
                primera_vez=p)
            p=False
            # validar la opción
            if opt!=-1:
                break
        # switchaer en las opciones - estructura multicondicional
        if opt==1:
            agregar_contacto()
            # print("Agregar contacto")
            # # capturar datos
            # nombre = input("ingresa nombre: ")
            # telefono = input("ingresa telefono: ")
            # colonia = input("ingresa colonia: ")
            # mascota_fav = input("ingresa mascota favorita: ")
            # sZ = input("ingresa signo zodiacal: ")
            # # guardar datos en una lista
            # atr = [telefono,colonia,mascota_fav,sZ]
            # # gurdar llave y valores en agenda_old
            # agenda_old[nombre] = atr
            # print(f" {nombre} fue agregado correctamente")
        elif opt==2:
            print("buscar contacto")
            # guarda lo que hay que buscar
            buscar = input("Escribir nombre del contacto: ")
            # busca en el la agenda_old, sino existe regresar "No existe"
            resultado = agenda_old.get(buscar,"No existe el contacto ingresado: XD")
            # Verifica que el resultado sea str
            if isinstance(resultado,str):
                print(resultado)
            else:
                nombre = buscar
                telefono,colonia,mascota_fav,sZ = resultado
                print(f"Nombre: {nombre}")
                print(f"Telefono: {telefono}")
                print(f"Colonia: {colonia}")
                print(f"Mascota favorita: {mascota_fav}")
                print(f"Signo zodiacal: {sZ}")
        elif opt==3:
            print("editar contacto")
            # guardar el nombre que voy a buscar
            editar = input("¿Ingresa el usuario que quieres editar: ")
            # si el nombre existe retorna una lista
            resultado = agenda_old.get(editar,"No existe el contacto ingresado: XD")
            # Verifica que el resultado sea str
            if isinstance(resultado,str):
                # el mensaje cuando no existe
                print(resultado)
            else:
                # modificar
                print("El contacto que quieres editar es: ", editar)
                # desempaquetado
                telefono,colonia,mascota_fav,sZ = resultado
                print(f"1. Telefono: {telefono}")
                print(f"2. Colonia: {colonia}")
                print(f"3. Mascota favorita: {mascota_fav}")
                print(f"4. Signo zodiacal: {sZ}")
                # guardar la opción
                opt = int(input("Ingresa una opción: "))
                # guardar el nuevo valor
                nuevo_valor = input("ingresa el nuevo valor: ")
                # cambiar el valor en la lista resultado
                resultado[opt-1] = nuevo_valor # opt-1 // 0,1,2,3
                # acutaliza agenda_old, con llave
                agenda_old[editar] = resultado
                print(f"El contacto \"{editar}\" se actualizo correctamente")
                print(f"nuevo valor \\ {nuevo_valor}")
        elif opt==4:
            print("borrar contacto")
        elif opt==5:
            print("salir")
            continuar = False
    print(agenda_old)
    print("Adios")
# Función principal main
def main():
    contactos = {  'Jannet': ['54-456-456', 'Ampliación', 'Conejos', 'Aries'],
            'Romina': ['45-465-489', 'Tepepan', 'Los perritos', 'Aries'],
            'Monse' : ['48-864-132', 'Santa Úrsula', 'Perritos', 'Tauro'],
            'Ivan'  : ['55-465-789', 'Santa Úrsula', 'Gatos', 'Tauro'],
            'Hector': ['45-898-697', 'Tepepan', 'Lomitos', 'Tauro'],
            'Fer'   : ['85-213-789', 'Ampliacion', 'Gatos', 'Geminis']}
    contactos1 = {  'Jannet': ['54-456-456', 'Ampliación', 'Conejos', 'Aries']}
    print("holaMundo")
    agenda(contactos1)

if __name__ == "__main__":
    main()