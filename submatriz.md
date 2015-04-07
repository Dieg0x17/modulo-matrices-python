# submatriz (M, f, c) #

Devuelve la submatriz resultante de eliminar la fila f y la columna c de la matriz M dada

## Ejemplo ##
```
>>> import matrices
>>> M = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 3]]
>>> matrices.imprime(matrices.submatriz(M, 1, 1))

  5  6
  8  9
```