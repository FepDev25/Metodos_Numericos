import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math


"""
Suponga el lector que está diseñando un tanque esférico (véase la figura P6.26) de almacenamiento de agua 
para un po- blado pequeño de un país en desarrollo. El volumen del líquido que puede contener se calcula 
con
V =πh2 [3R−h] 3
donde V = volumen [pie3], h = profundidad del agua en el tanque [pies], y R = radio del tanque [pies].
Si R = 3 m, ¿a qué profundidad debe llenarse el tanque de modo que contenga 30 m3? Haga tres iteraciones 
del método de Newton- Raphson para determinar la respuesta. Encuentre el error relati- vo aproximado 
después de cada iteración. Observe que el valor inicial de R convergerá siempre.
"""

def newton_raphson(funcion_h, limite_iteraciones, h_inicial):
    h_n_1 = 0
    h_n = h_inicial
    h = sp.Symbol('h')
    funcion = funcion_h
    f_prima = sp.diff(funcion, h)
    funcion_derivada = f_prima
    iteracion = 0
    print(f"h{iteracion}: {h_n}")
    print()

    while iteracion < limite_iteraciones:
        iteracion += 1
        h_n_1 = h_n

        f_hn = funcion.subs(h, h_n)
        f_dhn = funcion_derivada.subs(h, h_n)

        h_n = (h_n - (f_hn/f_dhn)).evalf()

        error_aproximado = h_n - h_n_1
        error_aproximado_porcentual = (error_aproximado / h_n) * 100
        print(f"h{iteracion}: {h_n}")
        print(f"Error aproximado porcentual: {abs(error_aproximado_porcentual)}")
        print()
    return h_n

def graficar(simbolo, mi_funcion, rango_h1, rango_h2, raiz):
    h = sp.Symbol(simbolo)
    funcion = mi_funcion

    funcion_numpy = sp.lambdify(h, funcion, 'numpy')

    h_vals = np.linspace(rango_h1, rango_h2, 100)
    f_vals = funcion_numpy(h_vals)

    # Grafica la función
    plt.plot(h_vals, f_vals, label=f'$f(h) = {str(funcion)}')
    plt.xlabel('h')
    plt.ylabel('f(h)')
    plt.title('Gráfico de $f(h)$')
    plt.scatter(raiz, 0, color='red')  # Punto de la raíz en el gráfico
    plt.grid(True)
    plt.legend()
    plt.show()

def comprobacion(valor_raiz):
    h = sp.Symbol('h')
    volumen_esperado = 30
    funcion_inicial = (math.pi * h ** 2) * ((9 - h) / 3)
    f_v = funcion_inicial.subs(h, valor_raiz)
    print(f"Volumen esperado: {volumen_esperado}")
    print(f"Volumen obtenido: {f_v}")


h = sp.Symbol('h')
funcion = (math.pi * h ** 2) * ((9 - h) / 3) - 30
profundidad = newton_raphson(funcion, 3, 1)
print(f"Profundidad: {profundidad} pies")

# Comprobar resultado:
comprobacion(profundidad)

# Graficar el punto de la raíz obtenida
graficar('h', funcion, -10, 10, profundidad)