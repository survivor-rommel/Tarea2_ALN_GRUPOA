import numpy as np
from numpy import *
import math

#Funcion que imprime la matriz
def printer(M):
    for row in M:
         print([format(elem, "f") for elem in row])

#Funcion que crea la matriz de Hilbert
def hilbert(n):
    hilbert= [[0 for i in range(n)]for j in range(n)] # Inicializamos una matriz n*n de ceros
    for i in range(0,n):
        for j in range(0,n):
            hilbert[i][j] = 1/(i+j+1)
    return hilbert
    
#Funcion que crea la matriz de Vandermonde
def vandermonde(ipvector, increasing=False):
    if not increasing:
        op_matx = np.array([x**(ipvector.size-1-i) for x in ipvector for i in range(ipvector.size)]).reshape(ipvector.size,ipvector.size)
    elif increasing:
        op_matx = np.array([x**i for x in ipvector for i in range(ipvector.size)]).reshape(ipvector.size,ipvector.size)

    return op_matx

#Inversa de una matriz
def inversa(x):
    return linalg.inv(x)

 #Norma 1
def norma1(x): #Norma 1
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
def norma2(x): #Norma 2 o euclidia
    s = 0
    m = len(x)
    for j in range(m):
        for k in range(m):
           s = s + abs(np.trace(x))

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

#Funcion que genera norma de una matriz 
def norma(x,opt): 
    if opt== 1: #Norma 1
        return norma1(x)
    elif opt==2: #Norma 2
        return norma2(x)
    elif opt== 'inf': #Norma Infinita
        return normaInfinita(x)

#Menu
print("Escoja opcion:\n")
print("1. Matriz de Hilbert\n")
print("2. Matriz de Vandermonde\n")
print("=========================")
opcion = int(input("Su opcion es: "))

#Hallando normas de la matriz Hilbert
if(opcion==1):
    n = int(input("Ingrese el orden de la matriz de Hilbert: "))
    Hilbert = hilbert(n)
    HilbertInversa = inversa(Hilbert)
    print("La matriz de Hilbert es:\n")
    printer(Hilbert)
    condi = (norma(Hilbert,1))*(norma(HilbertInversa,1))
    print("Norma 1 es: ",condi,"\n")
    condi = (norma(Hilbert,2))*(norma(HilbertInversa,2))
    print("Norma 2 es: ",condi,"\n")
    condi = (norma(Hilbert,'inf'))*(norma(HilbertInversa,'inf'))
    print("Norma infinita es: ",condi,"\n") 
    
#Hallando normas de la matriz Vandermonde               
elif(opcion==2): 
    n = int(input("Ingrese la cantidad de elementos del vector de entrada: "))
    list = [i for i in range(n)]
    inputvector = np.array(list)
    print("Desea la matriz de Vandermonde del vector de entrada:\n")
    print("1. En orden decreciente de potencias\n")
    print("2. En orden creciente de potencias\n")
    decinc = int(input("Su decisión es: "))
    if decinc == 1:
        VandermondeDec = vandermonde(inputvector,False)
        VandermondeDecInversa = inversa(VandermondeDec)
        print("El vector de entrada es:",inputvector,"\n")
        print("Vector de entrada en orden decreciente de potencias es:\n\n",VandermondeDec,"\n")
        condi = (norma(VandermondeDec,1))*(norma(VandermondeDecInversa,1))
        print("Norma 1 es: ",condi,"\n") 
        condi = (norma(VandermondeDec,2))*(norma(VandermondeDecInversa,2))
        print("Norma 2 es: ",condi,"\n") 
        condi = (norma(VandermondeDec,'inf'))*(norma(VandermondeDecInversa,'inf'))
        print("Norma infinita es: ",condi,"\n") 
            
    else:
        VandermondeInc= vandermonde(inputvector,True)
        VandermondeIncInversa = inversa(VandermondeInc)
        print("El vector de entrada es:",inputvector,"\n")
        print("Vector de entrada en orden creciente de potencias es:\n\n", VandermondeInc,"\n")
        condi = (norma(VandermondeInc,1))*(norma(VandermondeIncInversa,1))
        print("Norma 1 es: ",condi,"\n") 
        condi = (norma(VandermondeInc,2))*(norma(VandermondeIncInversa,2))
        print("Norma 2 es: ",condi,"\n") 
        condi = (norma(VandermondeInc,'inf'))*(norma(VandermondeIncInversa,'inf'))
        print("Norma infinita es: ",condi,"\n") 
        

else: #Error
    print("Opcion no es valida\n")
        

