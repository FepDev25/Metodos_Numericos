from raiz.biseccion import *
from raiz.falsa_pocision import *
import sympy as sp

"""Encuentre la raíz positiva de f(x) = x4 – 8x3 – 35x2 + 450x –1001, utilizando el método de la 
falsa posición. Tome como valores iniciales a xl = 4.5 y xu = 6, y ejecute cinco iteraciones. 
Calcule los errores tanto aproximado como verdadero, con base en el hecho de que la raíz es 5.60979. 
Emplee una gráfica para explicar sus resultados y hacer el cálculo dentro de un es = 1.0%. """

xi = 4.5
xu = 6
x = sp.Symbol('x')
funcion = x**4 - 8*x**3 -35*x**2 + 450*x - 1001 
#raiz = biseccion(xi , xu, 'x', funcion, 100, 10)
#graficar('x', funcion, 14, 18, raiz)

raiz = falsa_pocision(xi, xu, 'x', funcion, 5, 0)
graficar('x', funcion, 1, 10, raiz)