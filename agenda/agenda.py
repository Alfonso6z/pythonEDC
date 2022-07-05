import os

agenda = {'Alfonso': ['5556488984', 'Arboledas', 'Perritos', 'Cancer'], 'Miguel': ['6485867899', 'Portales', 'Michis', 'Aries']}
while True: # controlar el programa
    while True: # controla el menú
        # limpiar la consola
        os.system("cls")
        print("1.- Agregar contacto")
        print("2.- Modificar")
        print("3.- Eliminar")
        print("4.- Buscar")
        print("5.- Mostrar agenda")
        print("6.- Salir")
        try: 
            opt = int(input())
            if 1 <= opt <= 6:
                break
            else: 
                print("Ingresa una opción del 1 al 6")
                input("Enter para continuar ...")
        except:
            print(" ingresa el tipo de dato correcto")
    # realizar la opción elegida
    if opt == 1:
        nombre = input("Ingresa el nombre: ")
        respuesta = agenda.get(nombre) # retornar list si existe, sino None
        # verificar su existencia
        if isinstance(respuesta, list):
            print(f"El contacto \"{nombre}\" ya existe")
        else:
            telefono = input("Ingresa el número telefonico: ")
            colonia= input("Ingresa la colonia: ")
            mascota_fav = input("Ingresa la mascota favorita: ")
            signo_z = input("Ingresa el signo zodiacal: ")
            datos=[telefono,colonia,mascota_fav,signo_z]
            agenda[nombre] = datos
    elif opt == 2:
        # TODO:Modificar contacto
        pass
    elif opt == 3:
        # TODO:Eliminar datos[0]  = "telefono"
        pass
    elif opt == 4:
        # TODO: Buscar
        nombre = input("Ingresa el nombre a buscar: ")
        respuesta = agenda.get(nombre,f"El contacto {nombre} no existe") # retornar list si existe, sino str
        # verificar su existencia
        if isinstance(respuesta, list):
            telefono,colonia,mascota_fav,signo_z = respuesta
            print(f"******* {nombre} *******")
            print(f"telefono: {telefono}")
            print(f"colonia: {colonia}")
            print(f"mascota favorita: {mascota_fav}")
            print(f"signo zodiacal: {signo_z}")
        else:
            print(respuesta)
        
    elif opt == 5:
        i = 1
        for contacto,datos in agenda.items():
            telefono,colonia,mascota_fav,signo_z = datos
            print(f"****** {i} ******")
            print(f"nombre: {contacto}")
            print(f"telefono: {telefono}")
            print(f"colonia: {colonia}")
            print(f"mascota favorita: {mascota_fav}")
            print(f"signo zodiacal: {signo_z}\n")
            i+=1
        input("Enter para continuar ...")
    else:
        print(agenda)
        print("Adios!")
        break