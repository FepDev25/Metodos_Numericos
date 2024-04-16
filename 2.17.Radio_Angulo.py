import math

def calcular_radio_angulo(x, y):
    pi = math.pi
    print(f"({x},{y})")

    radio = math.sqrt(x**2 + y**2)
    angulo = 0

    if x<0 and y>0:
        angulo = arctangente(y, x) + pi
    elif x<0 and y<0:
        angulo = arctangente(y, x) - pi
    elif x<0 and y==0:
        angulo = pi
    elif x==0 and y>0:
        angulo = pi/2
    elif x==0 and y<0:
        angulo = -pi/2
    elif x==0 and y==0:
        angulo = 0
    else:
        angulo = arctangente(y, x)

    print(f"El radio es {radio}")
    print(f"El angulo es {angulo}")
    print()

def arctangente(p1, p2):
    return math.degrees(math.atan(p1 / p2))


calcular_radio_angulo(1, 0)
calcular_radio_angulo(1, 1)
calcular_radio_angulo(0, 1)
calcular_radio_angulo(-1, 1)
calcular_radio_angulo(-1, 0)
calcular_radio_angulo(-1, -1)
calcular_radio_angulo(0, -1)
calcular_radio_angulo(1, -1)
calcular_radio_angulo(0, 0)

