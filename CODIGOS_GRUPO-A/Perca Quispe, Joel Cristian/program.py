from linearalgebra import *

h = int(input("Ingrese la numero para la matriz de hilbert: "))
A = hilbert(15)

print('La matrix de Hilbert de ', h, 'x', h);
print_matrix(A)

print('k(M) = ',matrix_cond(A))

v = list(range(1,16))

B = vandermonde(v)
print('\n\nLa matrix de Vandermonde en base a v', v)
print_matrix(B)
print('k(M) = ', matrix_cond(B))