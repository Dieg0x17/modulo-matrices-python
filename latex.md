Devuelve una cadena de texto con la matriz M en formato LaTeX

## Ejemplo ##
```
>>> import matrices
>>> A = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 3]
>>> print(matrices.latex(A))

\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \\ \end{pmatrix}
```