## Itera sobre cada número en el vector de entrada n veces, siendo n el número de columnas en la matriz op y la salida
## un vector intermedio. Utilice una fórmula de orden diferencial basada en la condición creciente y decreciente.
## Reforma el vector intermedio usando el tamaño del vector de entrada (filas) yn (columnas) para generar la matriz op.

import numpy as np

def makeVander(ipvector, increasing=False):
    if not increasing:
        op_matx = np.array([x**(ipvector.size-1-i) for x in ipvector for i in range(ipvector.size)]).reshape(ipvector.size,ipvector.size)
    elif increasing:
        op_matx = np.array([x**i for x in ipvector for i in range(ipvector.size)]).reshape(ipvector.size,ipvector.size)

    return op_matx

n = int(input("Ingrese la cantidad de elementos del vector de entrada: "))
list = [i for i in range(n)]
inputvector=np.array(list)
op_matx_dec_order = makeVander(inputvector,False)
op_matx_inc_order = makeVander(inputvector,True)

print("El vector de entrada es:",inputvector,"\n")
print("La matriz de Vandermonde del vector de entrada en orden decreciente de potencias es:\n\n",op_matx_dec_order,"\n")
print("La matriz de Vandermonde del vector de entrada en orden creciente de potencias es:\n\n", op_matx_inc_order,"\n")
