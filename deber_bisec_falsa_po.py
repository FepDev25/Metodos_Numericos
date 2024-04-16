from biseccion import *
from falsa_pocision import *
import sympy as sp

""" Determine las raíces reales de f(x) = −25182x − 90x2 + 44x3– 8x4 + 0.7x5:
a) Gráficamente
b) Usando el método de bisección para localizar la raíz más grande con es = 10%. Utilice como valores iniciales xl = 0.5 y xu = 1.0.
c) Realice el mismo cálculo que en b), pero con el método de la falsa posición y es = 0.2% """

xi = 0.5
xu = 1
x = sp.Symbol('x')
funcion = -25182*x - 90*x**2 + 44*x**3 - 8*x**4 + 0.7*x**5
raiz = biseccion(xi , xu, 'x', funcion, 100, 10)
graficar('x', funcion, -1, 2, raiz)

raiz = falsa_pocision(xi, xu, 'x', funcion, 100, 0.2)
graficar('x', funcion, -1, 2, raiz)