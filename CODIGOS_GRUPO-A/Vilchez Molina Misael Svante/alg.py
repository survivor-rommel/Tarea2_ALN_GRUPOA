import numpy as np
from scipy.linalg import *

def cofactor(m, r, c):
	matriz = []
	for i in range(len(m) - 1):
		matriz.append([0] * (len(m) - 1))

	for i in range(r):
		for j in range(c):
			matriz[i][j] = m[i][j]
		for j in range(c + 1, len(m)):
			matriz[i][j - 1] = m[i][j]
	for i in range(r + 1, len(m)):
		for j in range(c):
			matriz[i - 1][j] = m[i][j]
		for j in range(c + 1, len(m)):
			matriz[i - 1][j - 1] = m[i][j]
	return(matriz)

def determin(m):
	if (len(m) <= 8):
		if (len(m) == 1):
			return m[0][0]
		determinant = 0
		for i in range(len(m)):
			determinant += (((-1) ** i) * m[0][i] * det(cofactor(m, 0, i)))
		return determinant
	return det(m)

def trans(m):
	matriz = []
	for i in range(len(m[0])):
		matriz.append([0] * len(m))

	for i in range(len(m)):
		for j in range(len(m[0])):
			matriz[j][i] = m[i][j]
	return(matriz)

def adj(m):
	matriz = []
	for i in range(len(m)):
		matriz.append([0] * len(m))

	for i in range(len(m)):
		for j in range(len(m)):
			matriz[i][j] = ((-1) ** (i + j)) * det(cofactor(m, i, j))
	return(matriz)


def inverse(m):
	if (len(m) <= 8):
		determinant = determin(m)
		matriz = adj(trans(m))
		for i in range(len(m)):
			for j in range(len(m)):
				matriz[i][j] /= determinant
		return(matriz)

	I = inv(m)
	inv_matriz = []
	for i in range(len(I)):
		inv_matriz.append([0] * len(I))

	for i in range(len(I)):
		for j in range(len(I)):
			inv_matriz[i][j] = I[i][j]
	return(inv_matriz)


def hilb(n):
	matriz = []
	for i in range(n):
		matriz.append([0] * n)

	for i in range(n):
		for j in range(n):
			matriz[i][j] = 1 / (i + j + 1)
	return(matriz)

def printMatrix(m, f, c):
	for i in range(f):
		for j in range(c):
			print(m[i][j], end = "\t")
		print()
	print()

def vander(c, n):
	matriz = []
	for i in range(len(c)):
		matriz.append([0] * n)

	for i in range(len(c)):
		for j in range(n):
			matriz[i][j] = c[i] ** (n - j - 1)
	return(matriz)

def norm(a, p):
	isMatrix = isinstance(a[0], list)
	if not isMatrix:
		if p == 'inf':
			return max(a)
		else:
			num = 0
			for i in range(len(a)):
				num += (a[i] ** p)
			return(num ** (1 / p))
	else:
		A = []
		if p == 1:
			for j in range(len(a[0])):
				num = 0
				for i in range(len(a)):
					num += abs(a[i][j])
				A.append(num)
			return max(A)
		elif p == 2:
			U, s, VT = np.linalg.svd(a)
			return max(s)
		elif p == 'inf':
			for i in range(len(a)):
				num = 0
				for j in range(len(a[0])):
					num += abs(a[i][j])
				A.append(num)
			return max(A)

def cond(a, p):
	return (norm(a, p) * norm(inverse(a), p))

print("Numero de condicionamiento de la matriz n x n con p-norm:")
n = int(input("Ingrese el valor de n: "))
p = int(input("Ingrese el valor de p: "))

M = []
for i in range(n):
	M.append(i + 1)

H = hilb(n)
V = vander(M, n)
print()
print("Matriz de Hilbert generada: ")
print()
printMatrix(H, n, n)
print()
print("Matriz de Vandermonde generada: ")
print()
printMatrix(V, n, n)
print()
print("Condicionamiento de matriz de Hilbert con ", p, "- norm: ")
print(cond(H, p))
print()
print("Condicionamiento de matriz de Vandermonde con ", p, "- norm: ")
print(cond(V, p))