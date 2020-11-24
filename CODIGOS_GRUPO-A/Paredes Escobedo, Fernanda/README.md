### Numero de Condición :
##### Hilbert Matrix y Vandermode Matrix
-------------------------------------------------------------------------
######Realizado por
> Fernanda Anthoanette Paredes Escobedo
> CUI: 20182906
> Grupo: A

--------------------------------------------------------------------
#### Explicación del programa

El archivo principal "NumberConditionMatrix.py", genera una aplicación de consola, para interactuar con el usuario. En tal caso, se generan salidas para que el usuario ingrese los datos necesarios para calcular el número de condición de la matriz de Hilbert o Vandermonde, según las opciones elegidas, así como porque norma calcular la condicional de la matriz.

--------------------------------------------------
>>Nota: Para ejecutar solo corra NumberConditionMatrix.py

>A continuación se muestra un ejemplo de la salida del programa para la matriz de Hilbert de orden 3 con la norma 1:

		****************************
		Condicional de una matriz
		****************************
		Escoja entre:
		1. Matriz de Hilbert
		2. Matriz de Vandermonde
		****************************
		Su elección es: 1
		****************************
		Ahora seleccione una de estas opciones:
		1. Condicional por la norma 1
		2. Condicional por la norma 2
		3. Condicional por la norma de Frobenius
		4. Condicional por la norma infinita
		****************************
		Su opción es: 1
		****************************
		Ingrese el orden de la matriz de Hilbert: 3
		*****************************************************
		La matriz de Hilbert es:
		['1.000000', '0.500000', '0.333333']
		['0.500000', '0.333333', '0.250000']
		['0.333333', '0.250000', '0.200000']
		*****************************************************
		El condicional de la matriz con la nomra 1 es:  748.0000000000027 

>Ahora con la matriz de Vandermonde de un vector de entrada  de 5 elementos ordenados por orden decreciente de potencias, con la norma de Frobenius:
		****************************
		Condicional de una matriz
		****************************
		Escoja entre:
		1. Matriz de Hilbert
		2. Matriz de Vandermonde
		****************************
		Su elección es: 2
		****************************
		Ahora seleccione una de estas opciones:
 		1. Condicional por la norma 1
		2. Condicional por la norma 2
		3. Condicional por la norma de Frobenius
		4. Condicional por la norma infinita
		****************************
		Su opción es: 3
		****************************
		Ingrese la cantidad de elementos del vector de entrada: 5
		*****************************************************
		Desea la matriz de Vandermonde del vector de entrada:
		1. En orden decreciente de potencias:n
		2. En orden creciente de potencias:
		Su decisión es: 1
		*****************************************************
		El vector de entrada es: [0 1 2 3 4] 
		*****************************************************
		La matriz de Vandermonde del vector de entrada en orden decreciente de potencias es:
		 [[  0   0   0   0   1]
		 [  1   1   1   1   1]
		[ 16   8   4   2   1]
		[ 81  27   9   3   1]
		 [256  64  16   4   1]] 
		*****************************************************
		El condicional de la matriz con la norma de Frobenius es:  2632.5581862831923 

#####Programas adicionales

El archivo "HilbertMatrix.py" permite generar una matriz de Hilbert de orden n, el orden lo dedice el usuario.
>El resultado de ejecutarlo sería:

		 Ingrese el orden de la matriz de Hilbert: 4
		['1.000000', '0.500000', '0.333333', '0.250000']
		['0.500000', '0.333333', '0.250000', '0.200000']
		['0.333333', '0.250000', '0.200000', '0.166667']
		['0.250000', '0.200000', '0.166667', '0.142857']

El archivo "Vandermonde Matrix.py", permite generar una matriz de Vandermonde a partir de un vector de n elementos, los cuales son generados por el programa en orden.

>El resultado de ejecutarlo sería:

		Ingrese la cantidad de elementos del vector de entrada: 6
		El vector de entrada es: [0 1 2 3 4 5] 
		La matriz de Vandermonde del vector de entrada en orden decreciente de potencias es:
 		[[   0    0    0    0    0    1]
		[   1    1    1    1    1    1]
		 [  32   16    8    4    2    1]
		 [ 243   81   27    9    3    1]
		 [1024  256   64   16    4    1]
		 [3125  625  125   25    5    1]] 
		La matriz de Vandermonde del vector de entrada en orden creciente de potencias es:
		 [[   1    0    0    0    0    0]
		 [   1    1    1    1    1    1]
		 [   1    2    4    8   16   32]
		 [   1    3    9   27   81  243]
		 [   1    4   16   64  256 1024]
		 [   1    5   25  125  625 3125]] 
