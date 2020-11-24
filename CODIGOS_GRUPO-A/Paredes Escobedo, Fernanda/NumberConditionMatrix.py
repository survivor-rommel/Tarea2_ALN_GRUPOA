
import numpy as np
from numpy import *
import math

#Generar matriz de Hilbert
def makeHilbert(n):
    Hilb= [[0 for i in range(n)]for j in range(n)] # Inicializamos una matriz n*n de ceros
    for i in range(0,n):
        for j in range(0,n):
            Hilb[i][j] = 1/(i+j+1)
    return Hilb
#Mostrar matriz de Hilbert 
def showMatrix(matrix):
    for row in matrix:
        print([format(elem, "f") for elem in row])

#Gemerar matriz de Vandermonde
def makeVander(ipvector, increasing=False):
    if not increasing:
        op_matx = np.array([x**(ipvector.size-1-i) for x in ipvector for i in range(ipvector.size)]).reshape(ipvector.size,ipvector.size)
    elif increasing:
        op_matx = np.array([x**i for x in ipvector for i in range(ipvector.size)]).reshape(ipvector.size,ipvector.size)

    return op_matx

#Inversa de una matriz
def inversa(x):
    return linalg.inv(x)

 #Norma 1
def normaUno(x): #Norma 1
    max=0
    m=len(x)
    for j in range(m):
        sum=0
        for k in range(m):
            sum = sum + abs(x[k][j])
        if sum > max:
            max = sum
        
    return max

#Norma 2 o euclidia
def normaEuclidia(x): #Norma 2 o euclidia
    s = 0
    m = len(x)
    for j in range(m):
        for k in range(m):
           s = s + abs(np.trace(x))

    return sqrt(s)
    
#Norma de Frobenius 
def normaFrobenius(x): #Norma de Frobenius
    s = 0
    m = len(x) #numero de filas y columnas, en este caso son iguales porque este programa se aplicará a matrices cuadradas
    for j in range(m):
        for k in range(m):
            s = s + abs(pow(x[j][k],2))

    return sqrt(s)

#Norma infinita
def normaInfinita(x): #Norma infinita
    max=0
    m=len(x)
    for j in range(m):
        sum=0
        for k in range(m):
            sum = sum + abs(x[j][k])
        if sum > max:
            max=sum
        
    return max

#Generar norma de una matriz 
def norma(x,p): #x es la matriz y p el párametro (norma1, norma2, frobenius o infinita)
    if p == 1: #Norma 1
        return normaUno(x)
    elif p ==2: #Norma 2
        return normaEuclidia(x)
    elif p == 'fro': #Norma Frobenius
        return normaFrobenius(x)
    elif p == 'inf': #Norma Infinita
        return normaInfinita(x)

#Mostrar el condicional de una matriz x
print("****************************")
print("Condicional de una matriz")
print("****************************\n")
print("Escoja entre:\n")
print("1. Matriz de Hilbert\n")
print("2. Matriz de Vandermonde\n")
print("****************************")
eleccion = int(input("Su elección es: "))
print("****************************\n")
print("Ahora seleccione una de estas opciones:\n ")
print("1. Condicional por la norma 1\n")
print("2. Condicional por la norma 2\n")
print("3. Condicional por la norma de Frobenius\n")
print("4. Condicional por la norma infinita\n")
print("****************************")
opcion = int(input("Su opción es: "))
print("****************************\n")

if eleccion == 1: #Hilbert y norma 1
    if opcion == 1:
        n = int(input("Ingrese el orden de la matriz de Hilbert: "))
        Hilbert = makeHilbert(n)
        HilbertInversa = inversa(Hilbert)
        print("*****************************************************\n")
        print("La matriz de Hilbert es:\n")
        showMatrix(Hilbert)
        print("*****************************************************\n")
        condi = (norma(Hilbert,1))*(norma(HilbertInversa,1))
        print("El condicional de la matriz con la nomra 1 es: ",condi,"\n")
    elif opcion == 2: #Hilbert y norma 2
        n = int(input("Ingrese el orden de la matriz de Hilbert: "))
        Hilbert = makeHilbert(n)
        HilbertInversa = inversa(Hilbert)
        print("*****************************************************\n")
        print("La matriz de Hilbert es:\n")
        showMatrix(Hilbert)
        print("*****************************************************\n")
        condi = (norma(Hilbert,2))*(norma(HilbertInversa,2))
        print("El condicional de la matriz con la norma euclidia es: ",condi,"\n")
    elif opcion == 3: #Hilbert y norma Frobenius
        n = int(input("Ingrese el orden de la matriz de Hilbert: "))
        Hilbert = makeHilbert(n)
        HilbertInversa = inversa(Hilbert)
        print("*****************************************************\n")
        print("La matriz de Hilbert es:\n")
        showMatrix(Hilbert)
        print("*****************************************************\n")
        condi = (norma(Hilbert,'fro'))*(norma(HilbertInversa,'fro'))
        print("El condicional de la matriz con la norma de Frobenius es: ",condi,"\n")
    else: #Hilbert y norma infinita
        n = int(input("Ingrese el orden de la matriz de Hilbert: "))
        Hilbert = makeHilbert(n)
        HilbertInversa = inversa(Hilbert)
        print("*****************************************************\n")
        print("La matriz de Hilbert es:\n")
        showMatrix(Hilbert)
        print("*****************************************************\n")
        condi = (norma(Hilbert,'inf'))*(norma(HilbertInversa,'inf'))
        print("El condicional de la matriz es con la norma infinita es: ",condi,"\n") 
    
elif eleccion == 2: 
    if opcion == 1: #Vandermonde y norma 1
        n = int(input("Ingrese la cantidad de elementos del vector de entrada: "))
        list = [i for i in range(n)]
        inputvector = np.array(list)
        print("*****************************************************\n")
        print("Desea la matriz de Vandermonde del vector de entrada:\n")
        print("1. En orden decreciente de potencias\n")
        print("2. En orden creciente de potencias\n")
        print("*****************************************************\n")
        decinc = int(input("Su decisión es: "))
        if decinc == 1:
            VandermondeDec = makeVander(inputvector,False)
            VandermondeDecInversa = inversa(VandermondeDec)
            print("*****************************************************\n")
            print("El vector de entrada es:",inputvector,"\n")
            print("*****************************************************\n")
            print("La matriz de Vandermonde del vector de entrada en orden decreciente de potencias es:\n\n",VandermondeDec,"\n")
            print("*****************************************************\n")
            condi = (norma(VandermondeDec,1))*(norma(VandermondeDecInversa,1))
            print("El condicional de la matriz es con la norma 1 es: ",condi,"\n") 
        else:
            VandermondeInc= makeVander(inputvector,True)
            VandermondeIncInversa = inversa(VandermondeInc)
            print("*****************************************************\n")
            print("El vector de entrada es:",inputvector,"\n")
            print("*****************************************************\n")
            print("La matriz de Vandermonde del vector de entrada en orden creciente de potencias es:\n\n", VandermondeInc,"\n")
            print("*****************************************************\n")
            condi = (norma(VandermondeInc,1))*(norma(VandermondeIncInversa,1))
            print("El condicional de la matriz con la norma 1 es: ",condi,"\n") 
    elif opcion == 2: #Vandermonde y norma euclidia
        n = int(input("Ingrese la cantidad de elementos del vector de entrada: "))
        print("*****************************************************\n")
        list = [i for i in range(n)]
        inputvector = np.array(list)
        print("Desea la matriz de Vandermonde del vector de entrada:\n")
        print("1. En orden decreciente de potencias:\n")
        print("2. En orden creciente de potencias:\n")
        decinc = int(input("Su decisión es: "))
        if decinc == 1:
            VandermondeDec = makeVander(inputvector,False)
            VandermondeDecInversa = inversa(VandermondeDec)
            print("*****************************************************\n")
            print("El vector de entrada es:",inputvector,"\n")
            print("*****************************************************\n")
            print("La matriz de Vandermonde del vector de entrada en orden decreciente de potencias es:\n\n",VandermondeDec,"\n")
            print("*****************************************************\n")
            condi = (norma(VandermondeDec,2))*(norma(VandermondeDecInversa,2))
            print("El condicional de la matriz con la norma euclidia es: ",condi,"\n") 
        else:
            VandermondeInc= makeVander(inputvector,True)
            VandermondeIncInversa = inversa(VandermondeInc)
            print("*****************************************************\n")
            print("El vector de entrada es:",inputvector,"\n")
            print("*****************************************************\n")
            print("La matriz de Vandermonde del vector de entrada en orden creciente de potencias es:\n\n", VandermondeInc,"\n")
            print("*****************************************************\n")
            condi = (norma(VandermondeInc,2))*(norma(VandermondeIncInversa,2))
            print("El condicional de la matriz con la norma euclidia es: ",condi,"\n") 
    elif opcion == 3: #Vandermonde y norma de frobenius
        n = int(input("Ingrese la cantidad de elementos del vector de entrada: "))
        print("*****************************************************\n")
        list = [i for i in range(n)]
        inputvector = np.array(list)
        print("Desea la matriz de Vandermonde del vector de entrada:\n")
        print("1. En orden decreciente de potencias:n")
        print("2. En orden creciente de potencias:\n")
        decinc = int(input("Su decisión es: "))
        if decinc == 1:
            VandermondeDec = makeVander(inputvector,False)
            VandermondeDecInversa = inversa(VandermondeDec)
            print("*****************************************************\n")
            print("El vector de entrada es:",inputvector,"\n")
            print("*****************************************************\n")
            print("La matriz de Vandermonde del vector de entrada en orden decreciente de potencias es:\n\n",VandermondeDec,"\n")
            print("*****************************************************\n")
            condi = (norma(VandermondeDec,'fro'))*(norma(VandermondeDecInversa,'fro'))
            print("El condicional de la matriz con la norma de Frobenius es: ",condi,"\n") 
        else:
            VandermondeInc= makeVander(inputvector,True)
            VandermondeIncInversa = inversa(VandermondeInc)
            print("*****************************************************\n")
            print("El vector de entrada es:",inputvector,"\n")
            print("*****************************************************\n")
            print("La matriz de Vandermonde del vector de entrada en orden creciente de potencias es:\n\n", VandermondeInc,"\n")
            print("*****************************************************\n")
            condi = (norma(VandermondeInc,'fro'))*(norma(VandermondeIncInversa,'fro'))
            print("El condicional de la matriz con la norma de Frobenius es: ",condi,"\n") 
    else: #Vandermonde y norma infinita
        n = int(input("Ingrese la cantidad de elementos del vector de entrada: "))
        print("*****************************************************\n")
        list = [i for i in range(n)]
        inputvector = np.array(list)
        print("Desea la matriz de Vandermonde del vector de entrada:\n")
        print("1. En orden decreciente de potencias:\n")
        print("2. En orden creciente de potencias:\n")
        decinc = int(input("Su decisión es: "))
        if decinc == 1:
            VandermondeDec = makeVander(inputvector,False)
            VandermondeDecInversa = inversa(VandermondeDec)
            print("*****************************************************\n")
            print("El vector de entrada es:",inputvector,"\n")
            print("*****************************************************\n")
            print("La matriz de Vandermonde del vector de entrada en orden decreciente de potencias es:\n\n",VandermondeDec,"\n")
            print("*****************************************************\n")
            condi = (norma(VandermondeDec,'inf'))*(norma(VandermondeDecInversa,'inf'))
            print("El condicional de la matriz con la norma infinita es: ",condi,"\n") 
        else:
            VandermondeInc= makeVander(inputvector,True)
            VandermondeIncInversa = inversa(VandermondeInc)
            print("*****************************************************\n")
            print("El vector de entrada es:",inputvector,"\n")
            print("*****************************************************\n")
            print("La matriz de Vandermonde del vector de entrada en orden creciente de potencias es:\n\n", VandermondeInc,"\n")
            print("*****************************************************\n")
            condi = (norma(VandermondeInc,'inf'))*(norma(VandermondeIncInversa,'inf'))
            print("El condicional de la matriz con la norma infinita es: ",condi,"\n") 
    
else: #Opciones inválidas
    print("***********************************************\n")
    print("Verifique sus opciones por favor. Ocurrió un error\n")
    print("***********************************************\n")