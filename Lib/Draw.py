

def drawSquare(dimension):
    # Parte Superior
    for varAux in range(dimension+1):
        print('* ', end='')
    print ()
    # Parte Central
    filaActual = 1
    while filaActual <= dimension-2:
        for varAux in range(dimension):
            if varAux == 0:
                print('* ', end='')
            elif varAux == dimension -1:
                print('  *', end='')
            else:
                print('  ', end='')
        print()
        filaActual +=1

    # Parte Inferior
    for varAux in range(dimension + 1):
        print('* ', end='')




