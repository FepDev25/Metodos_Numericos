import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

def falsa_pocision(mi, mu, mi_funcion, max_pasadas, porcentaje_error):
    # Inicialización de variables
    mr_ant = 0
    mr = 0
    m = sp.Symbol('m')
    funcion = mi_funcion

    pasadas = 1;
    while pasadas <= max_pasadas:
        # Guarda el valor anterior de la raíz para calcular el error
        mr_ant = mr

        print(f"Pasada N {pasadas}")
        print(f"Mi: {mi}")
        print(f"Mu: {mu}")

        # Calcula f(mi) y f(mu) evaluadas en la función
        fmi = funcion.subs(m, mi)
        fmu = funcion.subs(m, mu)
        
        print(f"f(mi): {fmi}")
        print(f"f(mu): {fmu}")

        # Calcula el valor de la raíz (mr)
        mr = mu - ((fmu * (mi - mu)) / (fmi - fmu))
        print(f"Mr: {mr}")

        # Calcula el error aproximado
        error_aprox = mr - mr_ant
        error_porcentual = (error_aprox / mr) * 100
        print(f"Error aproximado porcentual: {abs(error_porcentual)}%")

        # Si el error aproximado es menor o igual al porcentaje de error, termina
        if (abs(error_porcentual) <= porcentaje_error):
            print(f"Error de {porcentaje_error}% alcanzado")
            return mr

        # Calcula f(mr) evaluada en la función
        fmr = funcion.subs(m, mr)
        print(f"f(mr): {fmr}")

        # Calcula f(mi)*f(mr)
        fmi_x_fmr = fmi * fmr
        print(f"f(mi) * f(mr): {fmi_x_fmr}")

        # Actualiza los valores de mi y mu para la siguiente iteración
        if fmi_x_fmr < 0:
            mu = mr
        elif fmi_x_fmr > 0:
            mi = mr
        else:
            # Si f(mi)*f(mr) es cero, mr es la raíz
            print(f"Raíz encontrada: {mr}")
            return mr
        
        pasadas += 1
        print()
    return mr

def graficar(simbolo, mi_funcion, rango_m1, rango_m2, raiz):
    m = sp.Symbol(simbolo)
    funcion = mi_funcion

    # Convierte la función simbólica en una función numérica
    funcion_numpy = sp.lambdify(m, funcion, 'numpy')

    # Genera valores de m para graficar la función
    m_vals = np.linspace(rango_m1, rango_m2, 100)
    f_vals = funcion_numpy(m_vals)

    # Grafica la función
    plt.plot(m_vals, f_vals, label=f'$f(m) = {str(funcion)}')
    plt.xlabel('m')
    plt.ylabel('f(m)')
    plt.title('Gráfico de $f(m)$')
    plt.scatter(raiz, 0, color='red')  # Punto de la raíz en el gráfico
    plt.grid(True)
    plt.legend()
    plt.show()

# Valores iniciales vistos graficamente.
mi = 55
mu = 60
# En el ejercicio se especifica un error de 0.1%
porcentaje_error = 0.1
m = sp.Symbol('m')

# Ecuación en función de la masa (m)
funcion = (9.8 * m / 15) * (1 - math.e ** (-135 / m)) - 35

# Aplicación del método de la falsa posición para encontrar la raíz
raiz = falsa_pocision(mi, mu, funcion, 100, porcentaje_error)
print(f"La masa aproximada del paracaidista es: {raiz}")

# Graficar el punto de la raíz obtenida
graficar('m', funcion, 1, 100, raiz)
