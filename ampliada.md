# ampliada (A, S) #

Devuelve la matriz resultante de añadir la matriz S a la derecha de la matriz A.

## Ejemplo ##
```
>>> import matrices
>>> A = [[1,2,3,4,5,6,7,8,9], [3,3]]
>>> S = [[1,1,1], [3, 1]]
>>> M = matrices.ampliada(A, S)
>>> matrices.imprime(M)

   1  2  3  1
   4  5  6  1
   7  8  9  1
```