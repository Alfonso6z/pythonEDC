""" 
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después 
de que el usuario lo introduzca muestre por pantalla la cadena  ¡Hola <nombre>!,
donde <nombre> es el nombre que el usuario haya introducido. 
"""
# Entrada
nombre = input("Ingresa tu nombre: ")

#Salida, concatenar con +
print("¡Hola " + nombre + "!")

#concatenar con ,
print("¡Hola", nombre + "!")

# inyectar una variable con format
print(f"¡Hola {nombre}!")