import os,time

def menu(titulo,*opt,**mensajes):
    # repetir el menú si la opción es incorrecta
    while True:
        # limpiar la consola
        os.system("cls")
        # calcular el tamaño del letrero
        if mensajes["pv"]:
            print("        B I E N V E N I D O")
        cantidad = 22 + len(titulo)
        if mensajes["principal"]:
            print("*"*cantidad)
            print(f"********** {titulo} **********")
            print("*"*cantidad)
        else:
            print(f"********** {titulo} **********")
        # desplegar las opciones, desde opt:list
        for i in range(len(opt)):
            print(f"{i+1}.- {opt[i]}")
        # controla el erro
        try:
            # guardamos la opción
            opcion = int(input())
            # validamos el rango de las opciones
            if 1 <= opcion <= len(opt):
                # retorna la opción
                return opcion
            else:
                print(mensajes['error'])
        # si no es un número contra el error
        except:
            print("Ingresa un número")
        input("Enter para continuar ...")

def buscarEnAgenda(contactos):
    nombre = input("Ingresa el nombre: ")
    return nombre,contactos.get(nombre,f"El contacto {nombre} no existe")

def agregarContacto(contactos):
    os.system("cls")
    print("********** Agregar contacto **********")
    nombre,respuesta = buscarEnAgenda(contactos)
    # verificar su existencia
    if isinstance(respuesta, list):
        print(f"El contacto \"{nombre}\" ya existe")
    else:
        telefono = input("Ingresa el número telefonico: ")
        colonia= input("Ingresa la colonia: ")
        mascota_fav = input("Ingresa la mascota favorita: ")
        signo_z = input("Ingresa el signo zodiacal: ")
        datos=[telefono,colonia,mascota_fav,signo_z]
        contactos[nombre] = datos
        print(f"El contacto {nombre} fue agregado correctamente ...")
    input("Enter para continuar ...")

def modificarContacto(contactos):
     # limpiar la consola
    os.system("cls")
    print("********** Modificar contacto **********")
    nombre,respuesta = buscarEnAgenda(contactos) # retornar list si existe, sino str
    # verificar su existencia
    if isinstance(respuesta, list):
        telefono,colonia,mascota_fav,signo_z = respuesta
        opt = menu(f"Modificar: {nombre}",
                   f"telefono: {telefono}",
                   f"colonia: {colonia}",
                   f"mascota favorita: {mascota_fav}",
                   f"signo zodiacal: {signo_z}",
                   error="Elige una opción valida XD",
                   pv=False,
                   principal=False)
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
        contactos[nombre] = respuesta
        print(f"El contacto {nombre} fue modificado correctamente")
    else:
        print(respuesta)
    input("Enter para continuar ...")

def eliminarContacto(contactos):
    os.system("cls")
    print("********** Eliminar un contacto **********")
    nombre,respuesta = buscarEnAgenda(contactos)
    # verificar su existencia
    if isinstance(respuesta, list):
        contactos.pop(nombre)
        print(f"El contacto {nombre} fue eliminado")
    else:
        print(respuesta)
    input("Enter para continuar ...")

def buscarContacto(contactos):
    os.system("cls")
    print("********** Buscar contacto **********")
    nombre,respuesta = buscarEnAgenda(contactos)
    # verificar su existencia
    if isinstance(respuesta, list):
        telefono,colonia,mascota_fav,signo_z = respuesta
        os.system("cls")
        print(f"******* {nombre} *******")
        print(f"telefono: {telefono}")
        print(f"colonia: {colonia}")
        print(f"mascota favorita: {mascota_fav}")
        print(f"signo zodiacal: {signo_z}")
    else:
        print(respuesta)
    input("Enter para continuar ...")

def mostrarContactos(contactos):
    os.system("cls")
    print("********** Mostrar contactos **********")
    i = 1
    for contacto,datos in contactos.items():
        telefono,colonia,mascota_fav,signo_z = datos
        print(f"****** {i} ******")
        print(f"nombre: {contacto}")
        print(f"telefono: {telefono}")
        print(f"colonia: {colonia}")
        print(f"mascota favorita: {mascota_fav}")
        print(f"signo zodiacal: {signo_z}\n")
        i+=1
    input("Enter para continuar ...")

def agenda(contactos):
    p_v = True
    while True: # controlar el programa
        opt = menu("Agenda Telefonica",
         "Agreagar Contacto",
         "Modificar Contacto",
         "Eliminar Contacto",
         "Buscar",
         "Mostrar Agenda",
         "Salir",
         error="Elige una opción valida XD",
         pv=p_v,
         principal=True)
        # realizar la opción elegida
        if opt == 1:
            agregarContacto(contactos)
        elif opt == 2:
            modificarContacto(contactos)
        elif opt == 3:
            eliminarContacto(contactos)
        elif opt == 4:
            buscarContacto(contactos)
        elif opt == 5:
            mostrarContactos(contactos)
        else:
            os.system('cls')
            print("Adios!")
            time.sleep(2)
            os.system('cls')
            break
        p_v= False

def main():
    contactos = {'Alfonso': ['5556488984', 'Arboledas', 'Perritos', 'Cancer'], 'Miguel': ['6485867899', 'Portales', 'Michis', 'Aries']}
    agenda(contactos)
if __name__ == "__main__":
    main()