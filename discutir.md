# discutir(A,S) #

Discute sistemas de ecuaciones atendiendo al teorema de Rouché-Frobenius.

## Ejemplo ##
Discusión del siguiente sistema:
  * x+y=3
  * y+z=5
  * x+z=4

De el extraemos la matriz de coeficientes (A) y la matriz columna de soluciones (S).

```
>>> import matrices
>>> A=[[1,1,0,
        0,1,1,
        1,0,1],[3,3]]

>>> S=[[3,
        5,
        4],[3,1]]

>>> print matrices.dicutir(A,S)
Sistema compatible determidado (solución unica)
1

```
La función imprime el tipo de sistema y devuelve un valor numérico en función de el tipo de sistema:
  * 0 --> S.I
  * 1 --> S.C.D
  * 2 --> S.C.I

Lo que puede resultar útil para comprobar los sistemas antes de usar la función cramer(A,S).