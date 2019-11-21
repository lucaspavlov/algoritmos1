def merge(lista1, lista2):
    '''Dadas dos listas ordenadas, las une preservando el orden'''
    lista_ordenada = []
    L1 = len(lista1)
    L2 = len(lista2)
    ind1 = 0
    ind2 = 0
    while ind1 < L1 and ind2 < L2:
        if lista1[ind1] <= lista2[ind2]:
            lista_ordenada.append(lista1[ind1])
            ind1 += 1
        else:
            lista_ordenada.append(lista2[ind2])
            ind2 += 1
    if ind1 == L1:
        for i in range(ind2, L2):
            lista_ordenada.append(lista2[i])
    else:
        for i in range(ind1, L1):
            lista_ordenada.append(lista1[i])
    return lista_ordenada

def mergesort(lista):
    if len(lista) == 1:
        return lista
    medio = len(lista) // 2
    return merge(mergesort(lista[:medio]), mergesort(lista[medio:]))
