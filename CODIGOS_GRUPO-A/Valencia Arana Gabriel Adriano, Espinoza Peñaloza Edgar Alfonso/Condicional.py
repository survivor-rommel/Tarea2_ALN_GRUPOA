import copy
import math

from numpy import linalg as al
import numpy as np

"""
HALLAR CONDICIONAMIENTO DE LAS MATRICES DE HILBERT Y VANDERMONDE
EJEMPLO POR CONSOLA

>>> show_matriz(hilbert(3))
1.0 0.5 0.33333
0.5 0.33333 0.25
0.33333 0.25 0.2
>>> show_matriz(vandermonde(4))
ingrese numero de la fila  0 6
ingrese numero de la fila  1 3
ingrese numero de la fila  2 6
ingrese numero de la fila  3 2
1 6 36 216
1 3 9 27
1 6 36 216
1 2 4 8
>>> cond(hilbert(3),1)
748.6462207148505
>>> cond(hilbert(3),2)
524.5016824671295
>>> cond(hilbert(3),"fro")
526.6053418003786
>>> cond(hilbert(3),"inf")
748.6462207148505
>>>
>>> cond(vandermonde(4))
ingrese numero de la fila  0 3
ingrese numero de la fila  1 5
ingrese numero de la fila  2 1
ingrese numero de la fila  3 8
1 3 9 27
1 5 25 125
1 1 1 1
1 8 64 512
2439.5931188907307
>>>
"""

def hilbert(x):
	a = []
	for i in range (x):
		b = []
		for j in range (x):
			b.append(round(1/(j+i+1),5))
		a.append(b)
	return a

def vandermonde(x):
	v = []
	for i in range(x):
		print("ingrese numero de la fila ", i, end= " ")
		a = int(input())
		au = []
		for j in range(x):
			au.append(pow(a,j))
		v.append(au)
	show_matriz(v)
	return v

def vector_columna(A, p):
	if(p < len(A[0]) and p >= 0):
		x = []
		for i in range(len(A)):
			x.append(A[i][p])
		return x
	return False

def vector_fila(A, p):
	if(p < len(A) and p >= 0):
		x = []
		for i in range(len(A[p])):
			x.append(A[p][i])
		return x
	return False

def transpuesta(A):
	x = []
	for i in range(len(A[0])):
		au = []
		for j in range(len(A)):
			au.append(A[j][i])
		x.append(au)
	return x

def mult_matriz(A, B):
	x = []
	if(len(A[0]) == len(B)):
		for i in range(len(A)):
			au = []
			for j in range(len(B[0])):
				au2 = 0
				for k in range(len(B)):
					au2 += A[i][k]*B[k][j]
				au.append(au2)
			x.append(au)
	return x

def svd(a):

    eps = 1.e-15  
    tol = 1.e-64/eps
    assert 1.0+eps > 1.0 
    assert tol > 0.0   
    itmax = 50
    u = copy.deepcopy(a)
    m = len(a)
    n = len(a[0])

    e = [0.0]*n  
    q = [0.0]*n
    v = []
    for k in range(n): v.append([0.0]*n)
    g = 0.0
    x = 0.0
    for i in range(n):
        e[i] = g
        s = 0.0
        l = i+1
        for j in range(i,m): s += (u[j][i]*u[j][i])
        if s <= tol:
            g = 0.0
        else:
            f = u[i][i]
            if f < 0.0:
                g = math.sqrt(s)
            else:
                g = -math.sqrt(s)
            h = f*g-s
            u[i][i] = f-g
            for j in range(l,n):
                s = 0.0
                for k in range(i,m): s += u[k][i]*u[k][j]
                f = s/h
                for k in range(i,m): u[k][j] = u[k][j] + f*u[k][i]
        q[i] = g
        s = 0.0
        for j in range(l,n): s = s + u[i][j]*u[i][j]
        if s <= tol:
            g = 0.0
        else:
            f = u[i][i+1]
            if f < 0.0:
                g = math.sqrt(s)
            else:
                g = -math.sqrt(s)
            h = f*g - s
            u[i][i+1] = f-g
            for j in range(l,n): e[j] = u[i][j]/h
            for j in range(l,m):
                s=0.0
                for k in range(l,n): s = s+(u[j][k]*u[i][k])
                for k in range(l,n): u[j][k] = u[j][k]+(s*e[k])
        y = abs(q[i])+abs(e[i])
        if y>x: x=y
    for i in range(n-1,-1,-1):
        if g != 0.0:
            h = g*u[i][i+1]
            for j in range(l,n): v[j][i] = u[i][j]/h
            for j in range(l,n):
                s=0.0
                for k in range(l,n): s += (u[i][k]*v[k][j])
                for k in range(l,n): v[k][j] += (s*v[k][i])
        for j in range(l,n):
            v[i][j] = 0.0
            v[j][i] = 0.0
        v[i][i] = 1.0
        g = e[i]
        l = i
    for i in range(n-1,-1,-1):
        l = i+1
        g = q[i]
        for j in range(l,n): u[i][j] = 0.0
        if g != 0.0:
            h = u[i][i]*g
            for j in range(l,n):
                s=0.0
                for k in range(l,m): s += (u[k][i]*u[k][j])
                f = s/h
                for k in range(i,m): u[k][j] += (f*u[k][i])
            for j in range(i,m): u[j][i] = u[j][i]/g
        else:
            for j in range(i,m): u[j][i] = 0.0
        u[i][i] += 1.0
    eps = eps*x
    for k in range(n-1,-1,-1):
        for iteration in range(itmax):
            for l in range(k,-1,-1):
                goto_test_f_convergence = False
                if abs(e[l]) <= eps:
                    goto_test_f_convergence = True
                    break 
                if abs(q[l-1]) <= eps:
                    break  
            if not goto_test_f_convergence:
                c = 0.0
                s = 1.0
                l1 = l-1
                for i in range(l,k+1):
                    f = s*e[i]
                    e[i] = c*e[i]
                    if abs(f) <= eps:
                        break
                    g = q[i]
                    h = pythag(f,g)
                    q[i] = h
                    c = g/h
                    s = -f/h
                    for j in range(m):
                        y = u[j][l1]
                        z = u[j][i]
                        u[j][l1] = y*c+z*s
                        u[j][i] = -y*s+z*c
            z = q[k]
            if l == k:

                if z<0.0:
                    q[k] = -z
                    for j in range(n):
                        v[j][k] = -v[j][k]
                break 
            if iteration >= itmax-1:
                if __debug__: print('Error: no convergence.')
                break 
            x = q[l]
            y = q[k-1]
            g = e[k-1]
            h = e[k]
            f = ((y-z)*(y+z)+(g-h)*(g+h))/(2.0*h*y)
            g = pythag(f,1.0)
            if f < 0:
                f = ((x-z)*(x+z)+h*(y/(f-g)-h))/x
            else:
                f = ((x-z)*(x+z)+h*(y/(f+g)-h))/x
            c = 1.0
            s = 1.0
            for i in range(l+1,k+1):
                g = e[i]
                y = q[i]
                h = s*g
                g = c*g
                z = pythag(f,h)
                e[i-1] = z
                c = f/z
                s = h/z
                f = x*c+g*s
                g = -x*s+g*c
                h = y*s
                y = y*c
                for j in range(n):
                    x = v[j][i-1]
                    z = v[j][i]
                    v[j][i-1] = x*c+z*s
                    v[j][i] = -x*s+z*c
                z = pythag(f,h)
                q[i-1] = z
                c = f/z
                s = h/z
                f = c*g+s*y
                x = -s*g+c*y
                for j in range(m):
                    y = u[j][i-1]
                    z = u[j][i]
                    u[j][i-1] = y*c+z*s
                    u[j][i] = -y*s+z*c
            e[l] = 0.0
            e[k] = f
            q[k] = x

    return q

def pythag(a,b):
    absa = abs(a)
    absb = abs(b)
    if absa > absb: return absa*math.sqrt(1.0+(absb/absa)**2)
    else:
        if absb == 0.0: return 0.0
        else: return absb*math.sqrt(1.0+(absa/absb)**2)

def transpose(a):
    m = len(a)
    n = len(a[0])
    at = []
    for i in range(n): at.append([0.0]*m)
    for i in range(m):
        for j in range(n):
            at[j][i]=a[i][j]
    return at

def show_matriz(A):
	for i in A:
		for j in i:
			print(j, end = " ")
		print(" ")
def determinante(A):
	if (len(A) == len(A[0])):
		x = 0

def norma_vector(A, p):
	x = 0
	for i in range(len(A)):
		x+= pow(abs(A[i]),p)
	return pow(x,1/p)

def sum_v(A):
	x = 0
	for i in range(len(A)):
		x += abs(A[i])
	return x

def max_v(A):
	x = A[0]
	for i in A:
		if(x < i):
			x = i
	return x  

def norm(A, p = None):
	x = 0
	#assert A != False, "matriz inversible"
	if(p == 1):
		au = 0
		x = sum_v(vector_columna(A,0))
		for i in range(len(A[0])):
			if(x < sum_v(vector_columna(A,i))):
				x = sum_v(vector_columna(A,i))
		return x

	if(p == "fro"):
			for i in range(len(A)):
				for j in range(len(A[i])):
					x+=pow(A[i][j], 2)
			return pow(x, 1/2)
	if(p == 2 or p is None):
			return max(svd(A))
	if(p == "inf"):
		au = 0
		x = sum_v(vector_fila(A,0))
		for i in range(len(A)):
			if(x < sum_v(vector_fila(A,i))):
				x = sum_v(vector_fila(A,i))

		return x

def delete_row_column(A, i, j):
    rows = len(A)
    columns = len(A[0])
    return [[A[row][col] for col in range(columns) if col != j] for row in range(rows) if row != i]


def minor(A, i, j):
    A = delete_row_column(A, i, j)
    return det(A)


def det(A):
    assert len(A) == len(A[0]), "Matriz debe ser cuadrada"
    order = len(A)

    if order == 2:
        determinant = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])  # ad - bc
        return determinant
    else:
        determinant = 0
        for i in range(order):
            coefficient = A[0][i]
            if i % 2 == 1:
                coefficient *= -1
            determinant += coefficient * minor(A, 0, i)
        return determinant

def inv2x2(A):
	Adj = []
	de = det(A)
	Adj = [ [A[1][1], -A[1][0]] , [-A[0][1] , A[0][0] ]]
	Adj = transpuesta(Adj)
	Adj[0][0] *= 1/de
	Adj[0][1] *= 1/de
	Adj[1][0] *= 1/de
	Adj[1][1] *= 1/de
	return Adj

def inv(A):
    assert len(A) == len(A[0]), "Matriz debe ser cuadrada"
    order = len(A)

    if(len(A) > 7):
    	return al.inv(A)

    if(len(A) == 2 and len(A[0]) == 2):
    	return inv2x2(A)

    determinant = det(A)
    if determinant == 0:
    	return False
    cofactors = []
    for i in range(order):
        cofactors_row = []
        for j in range(order):
            coefficient = -1 if (i % 2) ^ (j % 2) else 1  
            cofactors_row.append(coefficient * minor(A, i, j))
        cofactors.append(cofactors_row)

    adjugate = transpose(cofactors)
    inverse = [[element / determinant for element in row] for row in adjugate] 
    return inverse

def cond(A, p = None):
	if(len(A) == len(A[0])):
		x = 0;
		if(p == 1):
			return norm(A,1) * norm(inv(A), 1)
		if(p == "fro"):
			return norm(A,"fro") * norm(inv(A), "fro")
		if(p == 2 or p is None):
			return norm(A) * norm(inv(A))
		if(p == "inf"):
			return norm(A,"inf") * norm(inv(A),"inf")


while True:
	print("que matriz desea obtener su condicion", end = " ")
	print("(1) hilbert (2)vandermonde")
	au = int(input())
	if(au == 1):
		print("de que tamaño desea su matriz de hilbert? ")
		au2 = int(input())
		print("que condicion desea(1) 1 (2 o cualquiera) 2 (3) frobenius (4) infinita")
		au3 = int(input())
		if(au3 == 1):
			print(cond(hilbert(au2), 1))
		elif(au3 == 2):
			print(cond(hilbert(au2)))
		elif(au3 == 3):
			print(cond(hilbert(au2), "fro"))
		elif(au3 == 4):
			print(cond(hilbert(au2), "inf"))
		else:
			print(cond(hilbert(au2)))

	if(au == 2):
		print("de que tamaño desea su matriz de vandermonde? ")
		au2 = int(input())
		print("que condicion desea(1) 1 (2 o cualquiera) 2 (3) frobenius (4) infinita")
		au3 = int(input())
		if(au3 == 1):
			print(cond(vandermonde(au2), 1))
		elif(au3 == 2):
			print(cond(vandermonde(au2)))
		elif(au3 == 3):
			print(cond(vandermonde(au2), "fro"))
		elif(au3 == 4):
			print(cond(vandermonde(au2), "inf"))
		else:
			print(cond(vandermonde(au2)))
