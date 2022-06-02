"""
crear una agenda: que contenga nombre, telefono, colonia, mascota favoria, signo zodiacal
se tiene que consultar ingresar borrar modificar
"""
import os

def imprime_contacto(nombre,atributos):
    telefono,colonia,mascota_fav,sZ = atributos
    print(f"Nombre: {nombre}")
    print(f"Teléfono: {telefono}")
    print(f"Colonia: {colonia}")
    print(f"Mascota_fav: {mascota_fav}")
    print(f"Signo Zodiacal: {sZ}")

def menu(titulo,*opt,**mensajes):
    # imprime titulo con bienvenida si primera_vez = Verdadero
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
        print(f"{i+1}.- {opt[i]}")
    opc = int(input("Selecciona una opción:  "))
    if opc>=1 and opc <=len(opt):
        return opc
    else:
        print(mensajes["error"])
        return -1
    
def mostrar_contactos(agenda:dict):
    # contar contactos
    cont = 1
    # agenda.items() es iterable
    # k = llave, v = valores[]
    for k,v in agenda.items():
        print(f"************** {cont} ***************")
        imprime_contacto(k, v)
        print()
        cont+=1

def agregar_contacto(agenda:dict):
    atr = []
    print("Agregar contacto")
    # capturar datos
    nombre = input("ingresa nombre: ")
    telefono = input("ingresa teléfono: ")
    atr.append(telefono)
    colonia = input("ingresa colonia: ")
    atr.append(colonia)
    mascota_fav = input("ingresa mascota favorita: ")
    atr.append(mascota_fav)
    sZ = input("ingresa signo zodiacal: ")
    atr.append(sZ)
    # guardar datos en una lista
    # atr = [telefono,colonia,mascota_fav,sZ]
    # gurdar llave y valores en agenda
    agenda[nombre] = atr
    print(f" {nombre} fue agregado correctamente")

def buscar_contacto(agenda:dict):
    print("buscar contacto")
    # guarda lo que hay que buscar
    buscar = input("Escribir nombre del contacto: ")
    # busca en el la agenda, sino existe regresar "No existe"
    resultado = agenda.get(buscar,"No existe el contacto ingresado: XD")
    # Verifica que el resultado sea str
    if isinstance(resultado,str):
        print(resultado)
    else:
        imprime_contacto(buscar, resultado)

def editar_contacto(agenda:dict):
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
        titulo = "Contacto a editar : " + editar
        # desempaquetado
        telefono,colonia,mascota_fav,sZ = resultado
        opt = menu(titulo,
                    "Teléfono: " + telefono,
                    "Colonia: " + colonia,
                    "Mascota favorita: " + mascota_fav,
                    "Signo Zodiacal: " + sZ,
                    error='No existe el atributo',primera_vez=False)
        # guardar el nuevo valor
        nuevo_valor = input("Ingresa el nuevo valor: ")
        # cambiar el valor en la lista resultado
        resultado[opt-1] = nuevo_valor # opt-1 // 0,1,2,3
        # acutaliza agenda, con llave
        agenda[editar] = resultado
        print(f"El contacto \"{editar}\" se actualizó correctamente")
        print(f"nuevo valor \\ {nuevo_valor}")

def borrar_contacto(agenda:dict):
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
        imprime_contacto(borrar, resultado)

def agenda(agenda):
    # bandera - bool
    continuar = True
    # primera vez
    primera_vez = True
    #while del programa Agenda
    while(continuar): # not salir = True
        # menu while del menu
        while(True):
            # Limpia pantalla
            os.system("cls")
            opt = menu(
                "Agenda Chida",
                "Mostar Contactos",
                "Agregar",
                "Buscar",
                "Editar",
                "Borrar",
                "Salir",
                error="Elegiste una opción incorreta XD",
                primera_vez=primera_vez)
            primera_vez=False
            # validar la opción
            if opt!=-1:
                break
        # switchaer en las opciones - estructura multicondicional
        os.system("cls")
        if opt==1:
            mostrar_contactos(agenda)
        elif opt==2:
            agregar_contacto(agenda)
        elif opt==3:
            buscar_contacto(agenda)
        elif opt==4:
            editar_contacto(agenda)
        elif opt==5:
            borrar_contacto(agenda)
        elif opt==6:
            continuar = False
        # no muestres Enter... si opt es salir
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