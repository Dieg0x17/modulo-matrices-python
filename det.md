# det (M) #

Calcula el determinante de una matriz cuadrada. Devuelve `None` si la matriz no es cuadrada.

## Ejemplo ##
```
>>> import matrices
>>> M = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 3]]
>>> print matrices.det(M)

0

>>> M = [[1, 0, 0, 0, 1, 0, 0, 0, 1], [3, 3]]
>>> print matrices.det(M)

1
```