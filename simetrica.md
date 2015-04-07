# simetrica (M) #

Devuelve True si la matriz M dada es simétrica y False en caso contrario.

## Ejemplos ##
```
>>> import matrices
>>> M = [[1, 0, 0, 0, 1, 0, 0, 0, 1], [3, 3]]
>>> matrices.simetrica(M)

True

>>> M = [[1, 2, 3, 2, 1, 4, 3, 4, 1], [3, 3]]
>>> matrices.simetrica(M)

True

>>> M = [[1, 2, 3, 4, 5, 6], [2, 3]]
>>> matrices.simetrica(M)

False

>>> M = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 3]]
>>> matrices.simetrica(M)

False
```