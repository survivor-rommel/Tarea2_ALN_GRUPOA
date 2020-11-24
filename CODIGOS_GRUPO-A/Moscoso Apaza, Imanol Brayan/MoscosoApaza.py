import numpy as np
def Hilbert(n): #n = norma
    H = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            H[i][j] = 1/(i+j+1)
    
    print(H)
    
	#numero de condicionamiento
    cond = np.linalg.cond(H)
    print("numero de condicionamiento=", cond)
    

def Vandermode(a):
    n = len(a)
    D = np.zeros((n,n),dtype=float)
    ultimo = n-1
    i = 0
    for i in range(0,n,1):
        for j in range(0,n,1):
            potencia = ultimo - j
            D[i,j] = a[i]**potencia
	
    print(D)
    
    #numero de condicionamiento
    cond = np.linalg.cond(D)
    print("numero de condicionamiento=", cond)
	
	
n = int(input("ingrese norma para la matriz de hilbert: "))
Hilbert(n)

#agregar el vector
a =[]
tam = int(input("tamano del arreglo: "))
for i in range(tam):
	val=int(input("ingrese numero: "))
	a.append(val)
Vandermode(a)