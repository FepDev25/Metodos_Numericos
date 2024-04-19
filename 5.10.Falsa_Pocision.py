import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

""" Encuentre la raíz positiva de f(x) = x4 – 8x3 – 35x2 + 450x –1001, utilizando el método de 
la falsa posición. Tome como valores iniciales a xl = 4.5 y xu = 6, y ejecute cinco iteraciones.
Calcule los errores tanto aproximado como verdadero, con base en el hecho de que la raíz es 5.60979. 
Emplee una gráfica para explicar sus resultados y hacer el cálculo dentro de un es = 1.0%. """

def falsa_pocision(xi, xu, mi_funcion, max_pasadas, porcentaje_error, mi_valor_verdadero):
    xr_ant = 0
    xr = 0
    x = sp.Symbol('x')
    funcion = mi_funcion
    valor_verdadero = mi_valor_verdadero

    pasadas = 1;
    while pasadas <= max_pasadas:
        # xr_ant guarda el antiguo valor de xr para calcular los errores
        xr_ant = xr

        print(f"Pasada N {pasadas}")
        print(f"Xi: {xi}")
        print(f"Xu: {xu}")

        # Calcula f(xi) y f(xu) evaluados en la funcion
        fxi = funcion.subs(x, xi)
        fxu = funcion.subs(x, xu)
        
        print(f"f(xi): {fxi}")
        print(f"f(xu): {fxu}")

        # Calcula el valor de xr
        xr = xu - ( (fxu * (xi - xu)) / (fxi - fxu) )
        print(f"Xr: {xr}")

        # Calculos los errores
        error_aprox = xr - xr_ant
        error_aproximado_porcentual = (error_aprox / xr) * 100
        print(f"Error aproximado porcentual: {abs(error_aproximado_porcentual)}%")

        error_verdadero = valor_verdadero - xr
        error_verdadero_porcentual = (error_verdadero / valor_verdadero) * 100
        print(f"Error verdadero porcentual: {abs(error_verdadero_porcentual)}%")

        # Si el error aproximado es igual o menor al error estalecido, termina
        if (abs(error_aproximado_porcentual) <= porcentaje_error):
            print(f"Error de {porcentaje_error} alcanzado")
            print(f"Raiz aproximada: {xr}")
            return xr

        # Calcula el valor de f(xr) evaluado en la funcion 
        fxr = funcion.subs(x, xr)
        print(f"f(xr): {fxr}")

        # Calcular el valor de f(xi)*f(xr)
        fxi_x_fxr = fxi * fxr
        print(f"f(xi) * f(xr): {fxi_x_fxr}")

        # Si fxi_x_fxr es menor a cero, xu pasa a ser xr
        if fxi_x_fxr < 0:
            xu = xr
        # Si fxi_x_fxr es mayor a cero, xi pasa a ser xr
        elif fxi_x_fxr > 0:
            xi = xr
        else:
        # Si fxi_x_fxr cero, xr es la raiz
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
xi = 4.5
xu = 6
# Manejando error del 1%
porcentaje_error = 1
# Numerode iteraciones, mientras mas iteraciones, mas cercana sera la raiz al valor verdadero.
iteraciones = 5
x = sp.Symbol('x')
funcion = x**4 - 8*x**3 -35*x**2 + 450*x - 1001 
# Declarando el valor verdadero de la raiz
valor_verdadero = 5.60979
# Los parametros corresponden a: xi, xu, la funcion, numero maximo de iteraciones y el 
# pocentaje de error relativo aproximado minimo que se desea manejar
raiz = falsa_pocision(xi , xu, funcion, iteraciones, porcentaje_error, valor_verdadero)
print(f"Raiz aproximada: {raiz}")
# Graficar el punto de la raiz obtenida.
graficar('x', funcion, 4.5, 6, raiz)
