from random import randint

def pedir_numero():
    lista = []
    for i in range (0,20):
        lista.append(randint(1, 100))
    return lista

def ordenamiento_burbuja(lista):
    tamanio = len(lista)
    for i in range(tamanio):
        for j in range(i + 1, tamanio): 
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista = pedir_numero()
print("Lista Desordenada: ")
print(lista)
lista_ordenada = ordenamiento_burbuja(lista)
print("Lista Ordenada: ")
print(lista_ordenada)