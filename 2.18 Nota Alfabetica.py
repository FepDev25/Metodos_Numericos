def Nota_Alfabetica():
    
    calificacion = float(input("Ingrese la calificación numérica (entre 0 y 100): "))
    
    if calificacion >= 90 and calificacion <= 100:
        return "A"
    elif calificacion >= 80 and calificacion < 90:
        return "B"
    elif calificacion >= 70 and calificacion < 80:
        return "C"
    elif calificacion >= 60 and calificacion < 70:
        return "D"
    else:
        return "F"

# Llamar a la función e imprimir el resultado
letra = Nota_Alfabetica()
print("La calificación es:", letra)