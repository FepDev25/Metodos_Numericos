import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

""" Suponga el lector que está diseñando un tanque esférico (véase la figura P5.16) para almacenar 
agua para un poblado pequeño en un país en desarrollo. El volumen de líquido que puede contener se calcula 
con
V = πh2 [3R−h] 3 
donde V = volumen [m3], h = profundidad del agua en el tanque [m], y R = radio del tanque [m].
Si R = 3m, ¿a qué profundidad debe llenarse el tanque de modo que contenga 30 m3? Haga tres iteraciones 
con el método de la falsa posición a fin de obtener la respuesta. Determine el error relativo aproximado 
después de cada iteración."""

def falsa_pocision(hi, hu, mi_funcion, max_pasadas, porcentaje_error):
    # Inicialización de variables
    hr_ant = 0
    hr = 0
    h = sp.Symbol('h')
    funcion = mi_funcion

    pasadas = 1
    while pasadas <= max_pasadas:
        # Guarda el valor anterior de hr para calcular el error
        hr_ant = hr

        print(f"Pasada N {pasadas}")
        print(f"Hi: {hi}")
        print(f"Hu: {hu}")

        # Calcula f(hi) y f(hu) evaluados en la función
        fhi = funcion.subs(h, hi)
        fhu = funcion.subs(h, hu)
        
        print(f"f(hi): {fhi}")
        print(f"f(hu): {fhu}")

        # Calcula el valor de hr
        hr = hu - ((fhu * (hi - hu)) / (fhi - fhu))
        print(f"Hr: {hr}")

        # Calcula el error aproximado
        error_aprox = hr - hr_ant
        error_porcentual = (error_aprox / hr) * 100
        print(f"Error aproximado porcentual: {abs(error_porcentual)}%")

        # Si el error aproximado es menor o igual al porcentaje de error, termina
        if abs(error_porcentual) <= porcentaje_error:
            print(f"Error de {porcentaje_error}% alcanzado")
            return hr

        # Calcula f(hr) evaluado en la función 
        fhr = funcion.subs(h, hr)
        print(f"f(hr): {fhr}")

        # Calcula f(hi)*f(hr)
        fhi_x_fhr = fhi * fhr
        print(f"f(hi) * f(hr): {fhi_x_fhr}")

        # Actualiza los valores de hi y hu para la siguiente iteración
        if fhi_x_fhr < 0:
            hu = hr
        elif fhi_x_fhr > 0:
            hi = hr
        else:
            # Si f(hi)*f(hr) es cero, hr es la raíz
            print(f"Raíz encontrada: {hr}")
            return hr
        
        pasadas += 1
        print()
    return hr

def graficar(simbolo, mi_funcion, rango_h1, rango_h2, raiz):
    h = sp.Symbol(simbolo)
    funcion = mi_funcion

    # Convierte la función simbólica en una función numérica
    funcion_numpy = sp.lambdify(h, funcion, 'numpy')

    # Genera valores de h para graficar la función
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


# Valores iniciales para el método de la falsa posición
hi = 1
hu = 3
porcentaje_error = 0
iteraciones = 3
h = sp.Symbol('h')

# Ecuación en función de la profundidad (h)
funcion = (math.pi * h ** 2) * ((9 - h) / 3) - 30

# Aplicación del método de la falsa posición para encontrar la raíz
raiz = falsa_pocision(hi, hu, funcion, iteraciones, porcentaje_error)
print(f"La profundidad del tanque es: {raiz} m")

# Comprobar resultado:
comprobacion(raiz)

# Graficar el punto de la raíz obtenida
graficar('h', funcion, hi, hu, raiz)
