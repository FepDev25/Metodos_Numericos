from random import randint
import math

def llenar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(randint(-100, 100)) 
        matriz.append(fila)
    return matriz

def raiz_de_cuadrados(matriz):
    suma = 0
    resultado = 0
    for fila in matriz:
        for numero in fila:
            suma += numero**2
    resultado = math.sqrt(suma)
    return resultado

def imprimir_matriz(matriz, mensaje):
    print(mensaje)
    for fila in matriz:
        print(fila)

matriz = llenar_matriz(3,3)
imprimir_matriz(matriz, "Matriz:")
resultado = raiz_de_cuadrados(matriz)
print(f"Raíz cuadrada de la suma de los cuadrados de los elementos: {resultado}")

def normalizar_matriz(matriz):
    for fila in matriz:
        mayor = fila[0]
        for numero in fila[1:]:
            if abs(numero) > abs(mayor):
                mayor = numero

        print(f"Fila: {fila}, mayor: {abs(mayor)}")

        for i in range(len(fila)):
            fila[i] = round(fila[i] / mayor, 2)
            
normalizar_matriz(matriz)
imprimir_matriz(matriz, "Matriz Normalizada:")