
import numpy as np 
matrix = np.array([[4, 2], [3, 1]]) 
print("Original matrix:") 
print(matrix) 
result =  np.linalg.cond(matrix) 
print("Condition number of the matrix:") 
print(result) 