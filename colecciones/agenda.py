"""
crear una agenda: que contenga nombre, telefono, colonia, mascota favoria, signo zodiacal
se tiene que consultar ingresar borrar modificar
"""
#
from secrets import randbits


agenda = {  'Jannet': ['54-456-456', 'Ampliación', 'Conejos', 'Aries'],
            'Romina': ['45-465-489', 'Tepepan', 'Los perritos', 'Aries'],
            'Monse' : ['48-864-132', 'Santa Úrsula', 'Perritos', 'Tauro'],
            'Ivan'  : ['55-465-789', 'Santa Úrsula', 'Gatos', 'Tauro'],
            'Hector': ['45-898-697', 'Tepepan', 'Lomitos', 'Tauro'],
            'Fer'   : ['85-213-789', 'Ampliacion', 'Gatos', 'Geminis']}
# bandera - bool
continuar = True
#while del programa Agenda
while(continuar): # not salir = True
    print("continuar =",continuar)
    # menu while del menu
    while(True):
        print("1. Agregar")
        print("2. Buscar")
        print("3. Editar ")
        print("4. Borrar")
        print("5. Salir")
        # guardar la opción
        opt = int(input())
        # validar la opción
        if opt<=5 and opt>=1:
            break
        else:
            print("opción no valida")

    # switchaer en las opciones - estructura multicondicional
    if opt==1:
        print("Agregar contacto")
        # capturar datos
        nombre = input("ingresa nombre: ")
        telefono = input("ingresa telefono: ")
        colonia = input("ingresa colonia: ")
        mascota_fav = input("ingresa mascota favorita: ")
        sZ = input("ingresa signo zodiacal: ")
        # guardar datos en una lista
        atr = [telefono,colonia,mascota_fav,sZ]
        # gurdar llave y valores en agenda
        agenda[nombre] = atr
        print(f" {nombre} fue agregado correctamente")
    elif opt==2:
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
            print(f"Telefono: {telefono}")
            print(f"Colonia: {colonia}")
            print(f"Mascota favorita: {mascota_fav}")
            print(f"Signo zodiacal: {sZ}")
            
    elif opt==3:
        print("editar contacto")
        # guardar el nombre que voy a buscar
        editar = input("¿Ingresa el usuario que quieres editar: ")
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
            # acutaliza agenda, con llave
            agenda[editar] = resultado
            print(f"El contacto \"{editar}\" se actualizo correctamente")
            print(f"nuevo valor \\ {nuevo_valor}")
    elif opt==4:
        print("borrar contacto")
    elif opt==5:
        print("salir")
        continuar = False
print(agenda)
print("Adios")

