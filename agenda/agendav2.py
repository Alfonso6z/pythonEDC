import os,time

def menu(titulo,*opt,**mensajes):
    print(titulo)
    for i in range(len(opt)):
        print(f"{i+1}.- {opt[i]}")
    opt = int(input())
    if 'error' in mensajes:
        print(mensajes['error'])
    return opt

def agenda():
    agenda = {'Alfonso': ['5556488984', 'Arboledas', 'Perritos', 'Cancer'], 'Miguel': ['6485867899', 'Portales', 'Michis', 'Aries']}
    while True: # controlar el programa
        while True: # controla el menú
            # limpiar la consola
            os.system("cls")
            print("**************************************")
            print("******** Agenda en python ************")
            print("**************************************")
            print("1.- Agregar contacto")
            print("2.- Modificar contacto")
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
            # limpiar la consola
            os.system("cls")
            print("********** Agregar contacto **********")
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
                print(f"El contacto {nombre} fue agregado correctamente ...")
                input("Enter para continuar ...")
        elif opt == 2:
            # limpiar la consola
            os.system("cls")
            print("********** Modificar contacto **********")
            nombre = input("Ingresa el nombre a modificar: ")
            respuesta = agenda.get(nombre,f"El contacto {nombre} no existe") # retornar list si existe, sino str
            # verificar su existencia
            if isinstance(respuesta, list):
                telefono,colonia,mascota_fav,signo_z = respuesta
                while True:
                    os.system("cls")
                    print(f"******* Modificar: {nombre} *******")
                    print(f"Elige una opción")
                    print(f"1.- telefono: {telefono}")
                    print(f"2.- colonia: {colonia}")
                    print(f"3.- mascota favorita: {mascota_fav}")
                    print(f"4.- signo zodiacal: {signo_z}")
                    opt = int(input())
                    if 1<=opt<=4:
                        break
                    else:
                        input("Opción incorrecta. Enter para continuar ...")
                os.system("cls")
                if opt == 1:
                    print(f"*** contacto {nombre} - telefono actual: {telefono} ***")
                    telefono_n = input("Ingresa el nuevo número de telefono: ")
                    respuesta[opt-1] = telefono_n
                elif opt == 2:
                    print(f"*** contacto {nombre} - colonia actual: {colonia} ***")
                    colonia_n = input("Ingresa la nueva colonia: ")
                    respuesta[opt-1] = colonia_n
                elif opt == 3:
                    print(f"*** contacto {nombre} - macota favorita actual: {mascota_fav} ***")
                    mascota_fav_n = input("Ingresa la nueva mascota: ")
                    respuesta[opt-1] = mascota_fav_n
                elif opt == 4:
                    print(f"*** contacto {nombre} - signo zodiacal actual: {signo_z} ***")
                    signo_z_n = input("Ingresa el nuevo signo: ")
                    respuesta[opt-1] = signo_z_n
                agenda[nombre] = respuesta
                print(f"El contacto {nombre} fue modificado correctamente")
            else:
                print(respuesta)
            input("Enter para continuar ...")
        elif opt == 3:
            os.system("cls")
            print("********** Eliminar un contacto **********")
            nombre = input("Ingresa el nombre a eliminar: ")
            respuesta = agenda.get(nombre,f"El contacto {nombre} no existe")
            # verificar su existencia
            if isinstance(respuesta, list):
                agenda.pop(nombre)
                print(f"El contacto {nombre} fue eliminado")
            else:
                print(respuesta)
            input("Enter para continuar ...")
        elif opt == 4:
            # limpiar la consola
            os.system("cls")
            print("********** Buscar contacto **********")
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
            input("Enter para continuar ...")
        elif opt == 5:
            os.system("cls")
            print("********** Mostrar agenda **********")
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
            os.system('cls')
            print("Adios!")
            time.sleep(2)
            os.system('cls')
            break

def main():
    print("Hola mundo")
    opcion = menu('Agenda',
                  "Agregar contacto",
                  "Modificar contacto",
                  "Eliminar",
                  "Buscar",
                  "Mostrar agenda",
                  "Salir",
                  error='Esto es un error de prueba')# kwargs {'error':'Esto es un erro de prueba'}
    print(f" la opción del menú es {opcion}")
if __name__ == "__main__":
    main()