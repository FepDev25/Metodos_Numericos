import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def biseccion(xi, xu, mi_funcion, max_pasadas, porcentaje_error):
    # Definir variables y crear la funcion
    xr = 0
    xr_ant = 0
    x = sp.Symbol('x')
    funcion = mi_funcion

    pasadas = 1;
    while pasadas < max_pasadas:
        # xr_ant guarda el antiguo valor de xr para calcular los errores
        xr_ant = xr

        print(f"Pasada N {pasadas}")
        print(f"Xi: {xi}")
        print(f"Xu: {xu}")

        # Calcular l valor de xr
        xr = (xi + xu) / 2
        print(f"Xr: {xr}")

        # Calcular l valor de fxi, fxu, y fxr evaluados en la funcion
        fxi = funcion.subs(x, xi)
        fxu = funcion.subs(x, xu)
        fxr = funcion.subs(x, xr)

        print(f"f(xi): {fxi}")
        print(f"f(xu): {fxu}")
        print(f"f(xr): {fxr}")

        # Calcular el valor de f(xi)*f(xr)
        fxi_x_fxr = fxi * fxr
        print(f"f(xi) * f(xr): {fxi_x_fxr}")

        # Calcular el error aproximado y el error aproximado porcentual
        error_aprox = xr - xr_ant
        error_porcentual = (error_aprox / xr) * 100
        print(f"Error aproximado porcentual: {abs(error_porcentual)}%")

        # Si el error porcentual es menor al error establecido, termina
        if (abs(error_porcentual) <= porcentaje_error):
            print(f"Error de {porcentaje_error} alcanzado")
            print(f"Raiz aproximada: {xr}")
            return xr

        # Si fxi_x_fxr es menor a cero, xu pasa a ser xr
        if fxi_x_fxr < 0:
            xu = xr
        # Si fxi_x_fxr es mayor a cero, xi pasa a ser xr
        elif fxi_x_fxr > 0:
            xi = xr
        else:
        # Si fxi_x_fxr es cero, xr es la raiz y termina
            print(f"Raiz encontrada: {xr}")
            return xr
        
        pasadas += 1
        print()
    return xr

def graficar (simbolo, mi_funcion, rango_x1, rango_x2, raiz):
    # Sirve para graficar la funcion, junto con el valor obtenido como raiz.
    x = sp.Symbol(simbolo)
    funcion = mi_funcion

    funcion_numpy = sp.lambdify(x, funcion, 'numpy')

    x_vals = np.linspace(rango_x1, rango_x2, 100)
    y_vals = funcion_numpy(x_vals)

    plt.plot(x_vals, y_vals, label=f'$f(x) = {str(funcion)}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de $f(x)$')
    plt.scatter(raiz, 0, color='red')
    plt.grid(True)
    plt.legend()
    plt.show()

# Valores de xi y xu de referencia
xi = 15
xu = 18
# Manejando error del 0.5%. (Mientras el error este mas cercano o igual a 0%, mas exacta sera la riaz.)
porcentaje_error = 0.5
x = sp.Symbol('x')
funcion = -25182*x - 90*x**2 + 44*x**3 - 8*x**4 + 0.7*x**5
# Los parametros corresponden a: xi, xu, la funcion, numero maximo de iteraciones y el 
# pocentaje de error relativo aproximado minimo que se desea manejar
raiz = biseccion(xi , xu, funcion, 100, porcentaje_error)
# Graficar el punto de la raiz obtenida.
graficar('x', funcion, 15, 18, raiz)
