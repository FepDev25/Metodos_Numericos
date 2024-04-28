import sympy as sp
import math
import numpy as np
import matplotlib.pyplot as plt

def newton_raphson(funcion_x, limite_iteraciones, x_inicial, porcentaje_error):
    # Esta funcion encuentra la raiz aproximada de una funcion, segun el limite de iteraciones o el error aproximado minimo.
    
    x_n_1 = 0 # Se define X n-1
    x_n = x_inicial # X_n se refiere al valor de x inicial que le damos al ejercicio
    # Crear la funcion
    x = sp.Symbol('x')
    funcion = funcion_x
    # Saca la derivada de la funcion
    f_prima = sp.diff(funcion, x)
    funcion_derivada = f_prima
    # Variable para controlar las iteraciones
    iteracion = 1
    # Imprimir primera iteracion
    print(f"x{iteracion}: {x_n}")
    print()

    while iteracion <= limite_iteraciones:
        print(f"Iteracion N{iteracion}")
        iteracion += 1
        # Almacenar Xn-1 para poder calcular el error aproximado porcentual.
        x_n_1 = x_n

        # Evaluar x_n en la funcion y en la derivada para luego encontrar el nuevo X_n
        f_xn = funcion.subs(x, x_n)
        f_dxn = funcion_derivada.subs(x, x_n)
        # Imprimir valores
        print(f"{x_n} evaluado en la funcion: {f_xn.evalf()}")
        print(f"{x_n} evaluado en la derivada: {f_dxn.evalf()}")

        # Calcular X_n
        x_n = (x_n - (f_xn/f_dxn)).evalf()

        # Calcular el error aproximado porcentual.
        error_aproximado = x_n - x_n_1
        error_aproximado_porcentual = (error_aproximado / x_n) * 100
        print(f"x{iteracion}: {x_n}")
        print(f"Error aproximado porcentual: {abs(error_aproximado_porcentual)}")

        # Si el error aproximado porcentual ya alcanza al error minimo que se paso por parametro, se sale de la funcion. 
        if (abs(error_aproximado_porcentual) <= porcentaje_error):
            print(F"Error de {porcentaje_error}% alcanzado.")
            # Retorna x_n
            return x_n
        
        print()
    # Retorna x_n, la raiz de la ultima iteracion.
    return x_n

def graficar(simbolo, mi_funcion, rango_x, rango_y, raiz):
    # Metodo para graficar la funcion junto con la raiz encontrada.
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

# Especificar el valor inicial que sera x_1
valor_inicial = -1
# Crear la funcion
x = sp.Symbol('x')
funcion = 7 * sp.sin(x) * math.e**(-x) + 3
# Encontrar la raiz.
porcentaje_de_error = 0.0000000001 # S eindica el porcentaje de error
raiz = newton_raphson(funcion, 10, valor_inicial, porcentaje_de_error )
# Imprimir raiz obtenida
print(f"La raiz es {raiz}")
# Graficar la funcion con la riaz encontrada.
graficar('x', funcion, -1, 1, raiz)
