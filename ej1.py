#Búsqueda recursiva por dicotomía en una tabla ordenada
tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = len(tabla)
def busqueda(tabla,l, valor, i):
    if i == valor:
        return "la posicion es el",i
    else:
        pass
def busqueda_recursiva(tabla, l):
    valor = int(input("Introduce el valor a buscar: "))
    i= -1
    print(busqueda(tabla, l, valor, i+1))


print(busqueda_recursiva(tabla, l))