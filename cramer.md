# cramer(A,S) #

Resuelve Sistemas compatibles determinados aplicando la regla de Cramer.

## Ejemplo ##
Resolución del siguiente sistema:
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

>>> print(matrices.cramer(A,S))
[1, 2, 3]

```
La salida es una lista con las soluciones, en este caso x=1 y=2 z=3.