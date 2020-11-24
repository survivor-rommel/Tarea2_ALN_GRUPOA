def makeHilbert(n):
    Hilb= [[0 for i in range(n)]for j in range(n)] # Inicializamos una matriz n*n de ceros
    for i in range(0,n):
        for j in range(0,n):
            Hilb[i][j] = 1/(i+j+1)
    return Hilb

def showMatrix(matrix):
    for row in matrix:
        print([format(elem, "f") for elem in row])

n = int(input(" Ingrese el orden de la matriz de Hilbert: ")) # Ingresamos el orden de la matriz de Hilbert
showMatrix((makeHilbert(n))) # Mostramos la matriz Hilbert de orden: n*n

