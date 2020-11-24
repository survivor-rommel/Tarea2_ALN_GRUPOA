# Condición de una Matriz con norma 2 en Python

## Descripción

Este proyecto corresponde al trabajo del curso Algebra Lineal Numérica de la carrera
de Ciencias de la Computación dictada en la Universidad Nacional de San Agustín de Arequipa.

**NOTA:** Adicionalmente se presenta implementacion de p-norma para p = 1,2,"fro", "inf"

### Contenido

1. El archivo `program.py`, contiene el programa principal con matrices de Hilbert y
vandermonde.

2. El archivo `linearalgebra.py` contiene la modularización de las funciones necesarias para determinar la inversa de una matriz, la norma, la determinante, etc.

## Instrucciones de Uso

Para ejecutar el el programa necesita ejecutar en consola:

`> python program.py`

seguir los pasos necesarios.

## Resultados parciales

Se hizo prueba con una matriz de hilbert de 15x15 el numero de condicionamiento es **4.684590819309408e+17**, el mismo caso en Octave resulta **3.6744e+17**.

Se hizo prueba tambien con la Matriz de Vandermonde con v = [1:15], el numero de condicionamiento resulta **2.58258833617361e+21**, el mismo caso en Octave da **2.5824e+21**.

En ambos casos el orden de magnitud se aproximan por lo que concluimos que el programa determina la condicion de una matriz.