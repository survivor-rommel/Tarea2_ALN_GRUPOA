import math as mt
import numpy as np
import sys

# This is a local module for
# Additional methods

def print_matrix(M):
    """
        param M: Matrix to be printed
    """
    for row in M:
        print("[", end="")
        for col in row:
            print(round(col,3), end="\t")
        print("]")


def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
        :returns: list of lists that form the matrix.
    """
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)
    return A

def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied
        :return: The copy of the given matrix
    """
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def matrix_multiply(A,B):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix
        :return: The product of the two matrices
    """
    rowsA, rowsB = len(A), len(B)
    colsA, colsB = len(A[0]), len(B[0])

    if colsA != rowsB:
        print('Number of columns of A must equal number of B rows.')
    
    C = zeros_matrix(rowsA, colsB)
    
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total
    return C


def hilbert(n):
    """
        Return the Hilbert matrix of n columns and rows
    """
    f,c = n,n
    H = [[0 for columnas in range(c)] for filas in range(f)]
    cont = 1
    for i in range(f):
        for j in range(c):
            H[i][j] = 1/(i+j+1)
            cont += 1
    return H
def hilmat(a, b):
    return [[1 / (i + j + 1) for j in range(b)] for i in range(a)]

def vandermonde(v):
    rows = cols = n = len(v)
    V = zeros_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            V[i][j] = pow(v[i], n-j-1)
    return V

def check_squareness(A):
    """
    Makes sure that a matrix is square
        :param A: The matrix to be checked.
    """
    if len(A) != len(A[0]):
        raise ArithmeticError("Matrix must be square to inverse.")

def determinant(A, total=0):
    indices = list(range(len(A)))
    
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)
        builder = 0

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc+1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant(As)
        total += A[0][fc] * sign * sub_det

    return total

def check_non_singular(A):
    det = determinant(A)
    if det != 0:
        return det
    else:
        raise ArithmeticError("Singular Matrix!")

def check_matrix_equality(A,B, tol=None):
    """
    Checks the equality of two matrices.
        :param A: The first matrix
        :param B: The second matrix
        :param tol: The decimal place tolerance of the check
        :return: The boolean result of the equality check
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol == None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j],tol) != round(B[i][j],tol):
                    return False

    return True

def identity_matrix(n):
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix
        :returns: a square identity matrix
    """
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1.0

    return I

def invert_matrix(A, tol=2):
    """
    Returns the inverse of the passed in matrix.
        :param A: The matrix to be inversed
        :return: The inverse of the matrix A
    """
    # Section 1: Make sure A can be inverted.
    return np.linalg.inv(A)
    check_squareness(A)
    check_non_singular(A)

    # Section 2: Make copies of A & I, AM & IM, to use for row operations
    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)

    # Section 3: Perform row operations
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]: # *** skip row with fd in it.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    # Section 4: Make sure that IM is an inverse of A within the specified tolerance
    if check_matrix_equality(I,matrix_multiply(A,IM),tol):
        return IM
    else:
        raise ArithmeticError("Matrix inverse out of tolerance.")


def matrix_norm(M, p):
    """
    Returns the norm of a Matrix
        Input: M, a square matrix; p, the type of norm what we want to solve
        Output: n, the p-norm of the matrix M

    """
    rows = len(M)
    cols = len(M[0])
    
    if p == 1:
        L = []
        for i in range(cols):
            sum = 0
            for j in range(rows):
                sum += abs(M[i][j])
            L.append(sum)
        return max(L)
    elif p == 2:
        return np.linalg.norm(M)

    elif p == "fro":
        norm = 0
        for i in range(rows):
            for j in range(cols):
                norm += mt.pow(M[i][j],2)
        return mt.sqrt(norm)
        
    elif p == "inf":
        L = []
        for i in range(rows):
            sum = 0
            for j in range(cols):
                sum += abs(M[i][j])
            L.append(sum)
        return max(L)
    else:
        print("Sorry. We don't have the solution... yet :v")
        return

def matrix_cond(M,p=2):
    return matrix_norm(M,p) * matrix_norm(invert_matrix(M),p)