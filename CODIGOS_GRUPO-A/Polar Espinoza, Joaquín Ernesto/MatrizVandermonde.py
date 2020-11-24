import numpy as np

x = np.array([1, 2, 3, 5])
N = 3
v1 = np.vander(x)

print('Vector x :\n', x)
print('Matriz de Vandermonde de vector x', v1)

y = np.array([4,5,6,7,8,9])
N = 4
v2 = np.vander(y, N)
v3 = np.vander(y)

print('\n\nVector y :\n', y)
print('Matriz de Vandermonde de vector y (N = 4): ', v2)
print('\n\n Matriz Vandermonde (Square) de vector y : ', v3)