"""
crear una agenda: que contenga nombre, telefono, colonia, mascota favoria, signo zodiacal
se tiene que consultar ingresar borrar modificar
"""
#
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
    elif opt==3:
        print("editar contacto")
    elif opt==4:
        print("borrar contacto")
    elif opt==5:
        print("salir")
        continuar = False
print(agenda)
print("Adios")

