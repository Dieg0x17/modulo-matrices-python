# potencia (M, n) #
Eleva una matirz M a un exponente entero positivo n. La matriz M debe ser cuadrada.

## Ejemplo ##
```
>>> import matrices
>>> M = [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 3] ]
>>> P = matrices.potencia(M, 2)
>>> matrices.imprime(P)

  30  36  42
  66  81  96
 102 126 150
```