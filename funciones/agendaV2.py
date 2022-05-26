"""
crear una agenda: que contenga nombre, telefono, colonia, mascota favoria, signo zodiacal
se tiene que consultar ingresar borrar modificar
"""
import os

def menu(titulo,*opt,**mensajes):
    # imprime titulo
    if mensajes["primera_vez"]:
        print("**********************************************")
        print(f"        BIENVENIDO a {titulo}       ")
        print("**********************************************")
    else:
        print("**********************************************")
        print(f"                {titulo}       ")
        print("**********************************************")
    # imprime opciones
    for i in range(len(opt)):
        print(f"{i+1}) {opt[i]}")
    opc = int(input("Selecciona una opción:  "))
    if opc>=1 and opc <=len(opt):
        return opc
    else:
        print(mensajes["error"])
        return -1

def mostrar_contactos(agenda):
    cont = 1
    for k,v in agenda.items():
        telefono,colonia,mascota_fav,sZ = v
        print(f"*********{cont}***********")
        print(f"Nombre: {k}")
        print(f"Teléfono: {telefono}")
        print(f"Colonia: {colonia}")
        print(f"Mascota_fav: {mascota_fav}")
        print(f"Signo Zodiacal: {sZ}")
        print()
        cont+=1

def agregar_contacto(agenda):
    print("Agregar contacto")
    # capturar datos
    nombre = input("ingresa nombre: ")
    telefono = input("ingresa teléfono: ")
    colonia = input("ingresa colonia: ")
    mascota_fav = input("ingresa mascota favorita: ")
    sZ = input("ingresa signo zodiacal: ")
    # guardar datos en una lista
    atr = [telefono,colonia,mascota_fav,sZ]
    # gurdar llave y valores en agenda
    agenda[nombre] = atr
    print(f" {nombre} fue agregado correctamente")
    return agenda

def buscar_contacto(agenda):
    print("buscar contacto")
    # guarda lo que hay que buscar
    buscar = input("Escribir nombre del contacto: ")
    # busca en el la agenda, sino existe regresar "No existe"
    resultado = agenda.get(buscar,"No existe el contacto ingresado: XD")
    # Verifica que el resultado sea str
    if isinstance(resultado,str):
        print(resultado)
    else:
        nombre = buscar
        telefono,colonia,mascota_fav,sZ = resultado
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Colonia: {colonia}")
        print(f"Mascota favorita: {mascota_fav}")
        print(f"Signo zodiacal: {sZ}")

def editar_contacto(agenda):
    # guardar el nombre que voy a buscar
    editar = input("Ingresa el usuario que quieres editar: ")
    # si el nombre existe retorna una lista
    resultado = agenda.get(editar,"No existe el contacto ingresado: XD")
    # Verifica que el resultado sea str
    if isinstance(resultado,str):
        # el mensaje cuando no existe
        print(resultado)
    else:
        # modificar
        print("El contacto que quieres editar es: ", editar)
        # desempaquetado
        telefono,colonia,mascota_fav,sZ = resultado
        print(f"1. Teléfono: {telefono}")
        print(f"2. Colonia: {colonia}")
        print(f"3. Mascota favorita: {mascota_fav}")
        print(f"4. Signo zodiacal: {sZ}")
        # guardar la opción
        opt = int(input("Ingresa una opción: "))
        # guardar el nuevo valor
        nuevo_valor = input("Ingresa el nuevo valor: ")
        # cambiar el valor en la lista resultado
        resultado[opt-1] = nuevo_valor # opt-1 // 0,1,2,3
        # acutaliza agenda, con llave
        agenda[editar] = resultado
        print(f"El contacto \"{editar}\" se actualizó correctamente")
        print(f"nuevo valor \\ {nuevo_valor}")
    return agenda

def borrar_contacto(agenda):
    # guardar el nombre que voy a buscar
    borrar = input("Ingresa el usuario que quieres borrar: ")
    # si el nombre existe retorna una lista
    resultado = agenda.pop(borrar,"No existe el contacto ingresado: XD")
    # Verifica que el resultado sea str
    if isinstance(resultado,str):
        # el mensaje cuando no existe
        print(resultado)
    else:
        # modificar
        print("El contacto que se eliminó es: ")
        # desempaquetado
        telefono,colonia,mascota_fav,sZ = resultado
        print(f"Nombre: {borrar}")
        print(f"Teléfono: {telefono}")
        print(f"Colonia: {colonia}")
        print(f"Mascota favorita: {mascota_fav}")
        print(f"Signo zodiacal: {sZ}")
    return agenda

def agenda(agenda):
    # bandera - bool
    continuar = True
    # primera vez
    p = True
    #while del programa Agenda
    while(continuar): # not salir = True
        os.system("cls")
        # menu while del menu
        while(True):
            opt = menu(
                "Agenda Chida",
                "Mostar Contactos",
                "Agregar",
                "Buscar",
                "Editar",
                "Borrar",
                "Salir",
                error="Elegiste una opción incorreta XD",
                primera_vez=p)
            p=False
            # validar la opción
            if opt!=-1:
                break
        # switchaer en las opciones - estructura multicondicional
        os.system("cls")
        if opt==1:
            mostrar_contactos(agenda)
        if opt==2:
            agenda = agregar_contacto(agenda)
        elif opt==3:
            buscar_contacto(agenda)
        elif opt==4:
            agenda = editar_contacto(agenda)
        elif opt==5:
            agenda = borrar_contacto(agenda)
        elif opt==6:
            continuar = False
        if opt!=6:
            input("Enter para continuar ...")
    print("Adiós ...")

# Función principal main
def main():
    contactos = {  'Jannet': ['54-456-456', 'Ampliación', 'Conejos', 'Aries'],
            'Romina': ['45-465-489', 'Tepepan', 'Los perritos', 'Aries'],
            'Monse' : ['48-864-132', 'Santa Úrsula', 'Perritos', 'Tauro'],
            'Ivan'  : ['55-465-789', 'Santa Úrsula', 'Gatos', 'Tauro'],
            'Hector': ['45-898-697', 'Tepepan', 'Lomitos', 'Tauro'],
            'Fer'   : ['85-213-789', 'Ampliacion', 'Gatos', 'Geminis']}
    agenda(contactos)

if __name__ == "__main__":
    main()