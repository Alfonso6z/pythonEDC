""" 
Ejercicio 6
Escribir un programa que pregunte al usuario por el número de horas
trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que 
le corresponde. """

horas = int(input("Ingresar horas trabajadas: "))
costo = float(input("Ingresar el costo por hora: "))

resultado = horas * costo

print(f"El pago que le corresponde es: ${resultado}")
