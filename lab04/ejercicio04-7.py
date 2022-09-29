def imprimircalificacion (calificacion):
    if(grade>= 0.9 and grade <=1.0):
        calificacion = "sobresaliente"
    elif (grade>= 0.8 and grade <0.9):
        calificacion = "notable"
    elif (grade>= 0.7 and grade <0.8):
        calificacion = "buena"
    elif (grade>=0.6 and grade <0.7):
        calificacion = "suficiente"
    elif (grade>= 0.6):
        calificacion = "insuficiente"
    else:
        calificacion = "no definido"
    return calificacion

    try: grade = float(input("ingrese la puntacion (0.01 - 1.00:"))
    print("La calificacion de su puntuacion es: ", grade)
    except:
    print("Error, puntuacion solamente acepta numeros"):