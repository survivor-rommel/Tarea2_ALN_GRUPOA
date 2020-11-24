import numpy as np

x = np.array([1, 2, 3, 5])
N = 3
vector1 = np.vander(x)

print('El Vector x :\n', x)
print('La matriz de VanderMonde del vector x', vector1)

y = np.array([11,5,16,12,7,1])
N = 5

vector2 = np.vander(y, N)
vector3 = np.vander(y)

print('\n\nVector y :\n', y)
print('La matriz de Vandermonde en el vector y (N = 5): ', vector2)
print('\n\nEntonces la de  Matriz Vandermonde cuadrada en  vector y : ', vector3)