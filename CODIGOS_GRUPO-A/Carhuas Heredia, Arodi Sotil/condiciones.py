import numpy as np
def show_matriz(A):
	for i in A:
		for j in i:
			print(j,end=" ")
		print(" ")


def matVander(x):
	v=[]
	for i in range(x):
		print("Ingrese numero de la fila ",i,end=" ")
		a = int(input())
		au = []
		for j in range(x):
			au.append(pow(a,j))

			pass
		v.append(au)
		pass
	v=np.fliplr(v)
	show_matriz(v)
	return v
	

def matHilbert(n):
    Hilb= [[0 for i in range(n)]for j in range(n)] 
    for i in range(0,n):
        for j in range(0,n):
            Hilb[i][j] = 1/(i+j+1)
    return Hilb




def normaCondicion(A,opc):
	if opc==1:
		print("Con la norma 1 es ",np.linalg.cond(A, 1),"\n")
	elif opc==2:
		print("Con la norma 2 es ",np.linalg.cond(A),"\n")
	else:
		if opc==3:
			print("Con la norma infinita es ",np.linalg.cond(A,np.inf),"\n")

		


print("Numero de Condiciones de una matriz.")
print("1.- Matriz de Hilbert\n")
print("2.- Matriz de Vandermonde\n")
op1=int(input("Ingrese la opcion: "))
if op1 == 1:
	n=int(input("Ingrese el orden de la matriz de Hilbert: "))
	A = matHilbert(n)
	print("Con la norma 1 es ",np.linalg.cond(A, 1),"\n")
	print("Con la norma 2 es ",np.linalg.cond(A),"\n")
	print("Con la norma infinita es ",np.linalg.cond(A,np.inf),"\n")
	pass
else:
	if op1 == 2:
		n=int(input("Ingrese el numero de elementos del vector de entrada: "))
		A =matVander(n)
		
		print("Con la norma 1 es ",np.linalg.cond(A, 1),"\n")
		print("Con la norma 2 es ",np.linalg.cond(A),"\n")
		print("Con la norma infinita es ",np.linalg.cond(A,np.inf),"\n")