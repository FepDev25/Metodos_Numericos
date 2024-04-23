import math

def calcular_volumen(R_valor, d_valor, radio):
    # El raido no se especifica en el ejercicio pero es necesario para sacar el volumen.
    R = R_valor
    d = d_valor
    print(f"R={R}")
    print(f"d={d}")
    print(f"radio={radio}")

    if d <= R:
        volumen_cono = (1/3) * math.pi * (radio**2) * d # d es la altura
        print(f"Volumen del cono: {volumen_cono}")
    elif d >= R and d <= 3*R:  
        volumen_cono = (1/3) * math.pi * (radio**2) * R # R es la altura porque el cono esta lleno
        # (d-h) es la altura, porque 'R' es la altura del cono, y al restarlo de 'd', se obtiene la altura en el cilindro
        volumen_cilindro = math.pi * (radio**2) * (d-R) 
        print(f"Volumen del cono: {volumen_cono}")
        print(f"Volumen del cilindro: {volumen_cilindro}")

        print(f"Volumen total: {volumen_cono + volumen_cilindro}")
    else:
        print("Sobrepasado")
    print()

#Los parametros son: R, d y el radio. 
R  = 1  

d1 = 0.5
d2 = 1.2
d3 = 3.0
d4 = 3.1

radio = 1.3

calcular_volumen(R, d1, radio)
calcular_volumen(R, d2, radio)
calcular_volumen(R, d3, radio)
calcular_volumen(R, d4, radio)
