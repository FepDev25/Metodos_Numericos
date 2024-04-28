import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

def secante(mi_funcion, x0, x1, maximo_iteraciones):
    # La funcion sirve para encontrar la raiz aproximada de una funcion segun las maximas iteraciones que se le indiquen.
    iteracion = 1
    x = sp.Symbol('x')
    funcion = mi_funcion
    x_i = 0 # Representa x_i en cada iteracion
    while(iteracion <= maximo_iteraciones): # Cuando las iteracines superen su maximo, el bucle termina.
        # Imprimir valores
        print(f"Iteracion N{iteracion}")
        print(f"x0: {x0}")
        print(f"x1: {x1}")

        fxi_1 = (funcion.subs(x, x1)).evalf() # Evaluar Xi - 1 en la funcion
        fxi_2 = (funcion.subs(x, x0)).evalf() # Evaluar Xi - 2 en la funcion
        # Imprimir valores
        print(f"f(Xi-1): {fxi_1}")
        print(f"f(Xi-2): {fxi_2}")
        
        x_i = (x1 - (fxi_1 * (x1 - x0)) / (fxi_1 - fxi_2)).evalf() # Calcular el valor de x_i
        # Imprimir xi calculada
        print(f"xi: {x_i}")
        x0 = x1 # Actualizar el valor de x_0
        x1 = x_i # Actualizar el valor de x_1

        fxi = (funcion.subs(x, x_i)).evalf() # Evaluar Xi en la funcion
        # Imprimir f(xi)
        print(f"f(Xi): {fxi}")

        # Incrementar las iteraciones
        iteracion += 1
        print()
    return x_i

def graficar(simbolo, mi_funcion, rango_x, rango_y, raiz):
    # Este metodo grafica la funcion junto con la raiz encontrada.
    x = sp.Symbol(simbolo)
    funcion = mi_funcion

    funcion_numpy = sp.lambdify(x, funcion, 'numpy')

    x_vals = np.linspace(rango_x, rango_y, 100)
    y_vals = funcion_numpy(x_vals)

    plt.plot(x_vals, y_vals, label=f'$f(x) = {str(funcion)}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de $f(x)$')
    plt.scatter(raiz, 0, color='red')
    plt.grid(True)
    plt.legend()
    plt.show()

# Crear la funcion en python
x = sp.Symbol('x')
funcion = 7 * sp.sin(x) * math.e**(-x) + 3
# Encontrar la raiz
raiz = secante(funcion, 1, 0, 10)
# Imprimir la raiz
print(f"La raiz es {raiz}")
# Graficar funcion con la raiz calculada.
graficar('x', funcion, -1, 1, raiz)    
