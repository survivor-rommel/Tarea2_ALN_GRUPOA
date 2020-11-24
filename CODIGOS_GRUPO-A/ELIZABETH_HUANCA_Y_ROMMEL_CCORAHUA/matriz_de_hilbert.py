import numpy as np
from math import factorial

# establecimiento de las 3 funciones necesarias binomio , hilb , invhilb






def binomio(a, b):
  

    if b < 0 or b > a:
        return 0
    if b == 0 or b == a:
        return 1
    return factorial(a) // (factorial(b) * factorial(a-b))

def hilb(a, b=0):

    if a < 1 or b < 0:
        raise ValueError("El tamaño de la matriz debe ser uno o incluso mas grande ")  #retorna en caso de error

    elif a == 1 and (b == 0 or b == 1):
        return np.array([[1]])

    elif b == 0:
        b = a

    v = np.arange(1, a + 1) + np.arange(0, b)[:, np.newaxis]
    return 1. / v   #     para el punto decimal...


def invhilb(n):
    
    A = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = ((-1)**(i + j)) * (i + j + 1) * binomio(n + i, n - j - 1) * \
             binomio(n + j, n - i - 1) * binomio(i + j, i) ** 2  # para el resultado esperado
    return A  # retornamos la matriz con respecto a las funciones anteriores