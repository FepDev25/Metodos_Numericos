import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def falsa_pocision(xi, xu, simbolo, mi_funcion, max_pasadas, porcentaje_error):
    xr_ant = 0
    xr = 0
    x = sp.Symbol(simbolo)
    funcion = mi_funcion

    pasadas = 1;
    while pasadas < max_pasadas:
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
        
        # Calculos los errores
        error_aprox = xr - xr_ant
        error_porcentual = (error_aprox / xr) * 100
        print(f"Error aproximado porcentual: {abs(error_porcentual)}%")

        # Si el error aproximado es igual o menor al error estalecido, termina
        if (abs(error_porcentual) <= porcentaje_error):
            print(f"Error de {porcentaje_error}% alcanzado")
            print(f"Raiz aproximada: {xr}")
            return xr
        
        pasadas += 1
        print()
    return xr

def graficar(simbolo, mi_funcion, rango_x, rango_y, raiz):
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

# Se crea la funcion del ejercicio.
x = sp.Symbol('x')
funcion = 1 - (1225 / (9.81 * (4*x + (x**2/2.5))**3) ) * (4 + x)
# En este metodo se recomienda disminuir el porcentaje de error y aumentar las iteraciones para un mejor resultado
raiz = falsa_pocision(0.5 , 2.5, 'x', funcion, 10, 1)
print(raiz)
# Se grafican resultados.
graficar('x', funcion, 0.5, 2.5, raiz)