
import numpy as np 
matriz = np.array([[10, 14], [12, 15]])
print("La matriz original es :")
print(matriz)
resultado =  np.linalg.cond(matriz)


print("El numero de condicion de la matriz es el siguiente  :")
print(resultado)