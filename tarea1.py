import math

def factorial(n):
    if n < 0:
        return "Error, no existe el factorial para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact


def evaluacion_metodo_1(num):
    resultado = 1
    for i in range(1,21):
        if (i % 2 == 0):
            resultado = resultado + ((num**i)/factorial(i))
        else:
            resultado = resultado - ((num**i)/factorial(i))
        
        print(f"Pasada {i}, resultado: {resultado}")
    
    return resultado


def evaluacion_metodo_2(num):
    resultado = 1
    for i in range(1,21):
        resultado = resultado + ((num**i)/factorial(i))
        print(f"Pasada {i}, resultado: {1/resultado}")
    
    return 1/resultado

print("Solucion por primer metodo: ")
solucion1 = evaluacion_metodo_1(5)
print("Solucion por segundo metodo: ")
solucion2 = evaluacion_metodo_2(5)

def serieMcLaurin(num):
    resultado = 1
    negativo = True
    for i in range(2,101,2):
        if (negativo):
            resultado = resultado - ((num**i)/factorial(i))
            negativo = False
        else:
            resultado = resultado + ((num**i)/factorial(i))
            negativo = True
        
        print(f"Pasada {i}, resultado: {resultado}")
    
    return resultado

print("Solucion por serie de McLaurin: ")
numero = 0.3 * math.pi
print(numero)
solucion1 = serieMcLaurin(numero)