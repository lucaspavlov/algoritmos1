def mergesort(lista):
    if len(lista) == 1:
        return lista
    medio = len(lista) // 2
    return merge(mergesort(lista[:medio], mergesort(lista[medio:]))

def merge(lista1, lista2):
    '''Dadas dos listas ordenadas, las une preservando el orden'''
    lista_ordenada = []
    L1 = len(lista1)
    L2 = len(lista2)
    ind_1 = 0
    ind_2 = 0
    while ind1 < L1 - 1 and ind2 < L2 - 1:
        if lista1[ind_1] <= lista2[ind_2]:
            lista_ordenada.append(lista1[ind_1])
            ind_1 += 1
        elif lista2[ind_2] < lista1[ind_1]:
            lista_ordenada.append(lista2[ind_2])
            ind_2 += 1
    if ind1 == L1 - 1:
        for i in range(ind2, L2):
            lista_ordenada.append(lista2[i])
    else:
        for i in range(ind1, L1):
            lista_ordenada.append(lista1[i])
