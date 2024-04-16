import math

def calcular_volumen(R_valor, d_valor, radio):
    R = R_valor
    d = d_valor
    print(f"R={R}")
    print(f"d={d}")
    print(f"radio={radio}")

    if d <= R:
        volumen_cono = (1/3) * math.pi * (radio**2) * d
        print(f"Volumen del cono: {volumen_cono}")
    elif d >= R and d <= 3*R:  
        volumen_cono = (1/3) * math.pi * (radio**2) * R
        volumen_cilindro = math.pi * (radio**2) * (d-R)
        print(f"Volumen del cono: {volumen_cono}")
        print(f"Volumen del cilindro: {volumen_cilindro}")

        print(f"Volumen total: {volumen_cono + volumen_cilindro}")
    else:
        print("Sobrepasado")
    print()

calcular_volumen(1, 0.5, 1)
calcular_volumen(1, 1.2, 1)
calcular_volumen(1, 3, 1)
calcular_volumen(1, 3.1, 1)
