colores = ["a","v","r","a","a","v","r","r","r"]
azul = []
rojo = []
verde = []
ordenada = []
def ordenado():
    for i in colores:
        if i == "a":
            azul.append(i)
        elif i == "v":
            verde.append(i)
        elif i == "r":
            rojo.append(i)
    ordenada = azul + verde + rojo
    return ordenada
print(ordenado())
