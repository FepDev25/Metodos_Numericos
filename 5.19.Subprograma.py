import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def imprimir(iteracion, xi, xu, xr, fxi, fxr):
    print(f"Iteracion N{iteracion}")
    print(f"xi: {xi}")
    print(f"xu: {xu}")
    print(f"xr: {xr}")
    print(f"f(xi): {fxi}")
    print(f"f(xr): {fxr}")
    print()

def biseccion(xi, xu, mi_funcion, max_iteraciones):
    # Definir variables y crear la funcion
    xr = 0
    x = sp.Symbol('x')
    funcion = mi_funcion
    evaluacion = 0

    iteraciones = 1;
    # Evaluar f(xi) antes de entrar en el bucle
    fxi = funcion.subs(x, xi)
    evaluacion += 1
    while iteraciones <= max_iteraciones:
        xr = (xi + xu) / 2
        # Evaluar unicamente xr
        fxr = funcion.subs(x, xr)
        evaluacion += 1
        # Realizar el test de f(xi)*f(xr)
        test = fxi * fxr

        imprimir(iteraciones, xi, xu, xr, fxi, fxr)

        if test < 0:
            xu = xr
        elif test > 0:
            xi = xr
            # Si test es menor a cero, f(xi) sera f(xr) en la sigueinte pasada, evitando asi evaluaciones innecesarias
            fxi = fxr
            evaluacion -= 1
        else:
            print(f"Raiz encontrada: {xr}")
            return xr
        
        iteraciones += 1
    print(f"Numero de iteraciones: {iteraciones}")
    print(f"Numero de evaluaciones: {evaluacion}")
    return xr

xi = 0.5
xu = 2
iteraciones = 100
x = sp.Symbol('x')
funcion = sp.log(x**2) - 0.7
raiz = biseccion(xi , xu, funcion, iteraciones)
print(f"Raiz aproximada: {raiz}")