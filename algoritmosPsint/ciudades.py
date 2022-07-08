''' 
Se quiere saber cuál es la ciudad con la población de más personas, son tres estados
con once ciudades, hacer un algoritmo en Pseint que nos permita saber eso.
    Entrada: 33 poblaciones, 11 por cada estado(3)
    Salida: la ciudad con mayor población
'''
estado_max =""
ciudad_max = 0
p_max = 0
estados = ["A","B","C"]
for estado in estados:
    for ciudad in range(1,12):
        p = int(input(f"Ingresa la población del estado {estado} ciudad {ciudad}: "))
        if p > p_max:
            estado_max = estado
            ciudad_max = ciudad
            p_max = p
print(f"El estado {estado_max} con ciudad {ciudad_max} tienen la mayor poblacion = {p_max}")