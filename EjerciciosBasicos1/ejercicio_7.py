""" 
Ejercicio 7
Pedir el precio de un producto y calcular su IVA (21%) y su valor 
original 
"""

# Concepto matemático
precio = int(input("Ingresar precio: "))

# iva = (precio * 21) / 100
iva = precio * 0.21
original = precio - iva

print("Y su valor original es:", original)
