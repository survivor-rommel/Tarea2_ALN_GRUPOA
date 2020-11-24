#Alumna: Evelyn Lizbeth Cusi Hancco

import numpy as np
from math import *
from numpy.linalg import det, inv
def mostrarMatriz(M,n):
    print("\nMatriz")
    for i in range(n):
        for j in range(n):
            print(round(M[i][j],4),end="\t\t")
        print()

def mostrarMatriz2(M,n):
    print("\nMatriz")
    for i in range(n):
        for j in range(n):
            print(M[i][j],end="\t\t")
        print()


def matrizVandermonde(M,n):
    for i in range(n):
        for j in range(1):
            M[i][j]=i+1
    M2=[]
    for i in range(n):
        M2.append([0]*n)
    for i in range(n):
        for j in range(n):
            M2[i][j]=M[i][0]**j

    return M2


def matrizHilbert(n):
    M3=[]
    for i in range(n):
        M3.append([0]*n)
    for i in range(n):
        for j in range(n):
            a=j+i+1
            M3[i][j]=(1/a)
    return M3

def maximoDeSumaColumna(M,n):
    L=[]
    for j in range(n):
        suma=0
        for i in range(n):
            suma=suma+abs(M[i][j])

        L.append(suma)

    maximo=L[0]
    for i in range(n):
        if L[i]>maximo:
            maximo=L[i]
    return maximo
    
def maximoDeMatrizInversa(M,n):

    MxInversa=[]
    for i in range(n):
        MxInversa.append([0]*n)
    MxInversa=np.linalg.inv(M)

    MxInversaAbs=[]
    for i in range(n):
        MxInversaAbs.append([0]*n)
    for i in range(n):
        for j in range(n):
            MxInversaAbs[i][j]=abs(MxInversa[i][j])
    L2=[]
    for j in range(n):
        suma=0
        for i in range(n):
            suma=round(suma+MxInversaAbs[i][j],7)

        L2.append(suma)

    maximo2=L2[0]
    for i in range(n):
        if L2[i]>=maximo2:
            maximo2=L2[i]
    return maximo2

def NumCondicion_Norma_Uno(M):
    normaUno=maximoDeSumaColumna(M,n)*maximoDeMatrizInversa(M,n)
    return normaUno

def Norma_Infinita(M,n):

    L3=[]
    for i in range(n):
        suma=0
        for j in range(n):
            suma=suma+M[i][j]

        L3.append(suma)

    maximo3=L3[0]
    for i in range(n):
        if L3[i]>maximo3:
            maximo3=L3[i]
    return maximo3


def NumCondicion_Norma_Infinita(M):
    return np.linalg.cond(M,inf)


def Norma_Dos(M):
    resultado=Norma_Infinita(M,n)*maximoDeSumaColumna(M,n)
    normaDos=sqrt(resultado)
    return normaDos

    
def NumCondicion_Norma_Dos(M):
    return np.linalg.cond(M,2)



print()
print("Menu:")
print("1) Numero de condiciones con Matriz de Hilbert")
print("2) Numero de condiciones con Matriz de Vandermonde")
print("3) Salir")
opcion=int(input("Ingrese la opción: "))
while opcion!=3:
    if opcion==1:
        n=int(input("Ingresar el orden de la matriz de Hilbert: "))
        M=[]
        for i in range(n):
            M.append([0]*n)


        Hilbert=[]
        for i in range(n):
            Hilbert.append([0]*n)


        print()
        print()

        print("Matriz de Hilbert")
        Hilbert=matrizHilbert(n)
        mostrarMatriz(Hilbert,n)
        print()
        print("________________________________________________________________________________________________________")
        print("NUMERO DE CONDICIONES: ")
        print("Numero de condicion con Norma Uno:     ",NumCondicion_Norma_Uno(Hilbert))

        print("Numero de condicon con Norma Infinita: ",NumCondicion_Norma_Infinita(Hilbert))

        print("Numero de condicio con Norma Dos:      ",NumCondicion_Norma_Dos(Hilbert))
        print("________________________________________________________________________________________________________")

    elif opcion==2:
        n=int(input("Ingresar el orden de la matriz de Vandermonde: "))
        M=[]
        for i in range(n):
            M.append([0]*n)

                
        Vandermonde=[]
        for i in range(n):
            M.append([0]*n)

        print()
        print("Matriz de Vandermonde")
        Vandermonde=matrizVandermonde(M,n)
        mostrarMatriz2(Vandermonde,n)
        print()
        print()
        print("________________________________________________________________________________________________________")
        print("NUMERO DE CONDICIONES: ")
        print("Numero de condicion con Norma Uno:     ",NumCondicion_Norma_Uno(Vandermonde))

        print("Numero de condicon con Norma Infinita: ",NumCondicion_Norma_Infinita(Vandermonde))

        print("Numero de condicio con Norma Dos:      ",NumCondicion_Norma_Dos(Vandermonde))
        print("________________________________________________________________________________________________________")

    print()
    print("Menu:")
    print("1) Numero de condiciones con Matriz de Hilbert")
    print("2) Numero de condiciones con Matriz de Vandermonde")
    print("3) Salir")
    opcion=int(input("Ingrese la opción: "))


