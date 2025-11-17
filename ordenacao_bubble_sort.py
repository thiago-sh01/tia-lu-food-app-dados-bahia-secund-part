def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j]["codigo"] > lista[j+1]["codigo"]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista