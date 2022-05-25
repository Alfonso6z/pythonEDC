d={
    "alfoso":[1,2,3,4,5],
    "marisol":[1],
    "juan":[3,2,1]
}
for k,v in d.items():
    calf=""
    for i in range(len(v)):
        if i == len(v)-1:
            calf+=str(v[i])
        else:
            calf+=str(v[i])+", "
    print(f"Nombre:{k}\n\tcalificaciones:{calf}")