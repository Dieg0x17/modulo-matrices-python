Evalúa una expresión matricial, devolviendo el resultado. También es posible hacer asignaciones directamente en la expreión.

  * expresión debe ser una cadena literal.


(ver ejemplos)

## Sintaxis ##

  * Los nombres de las matrices deben ser letras mayúsculas, exceptuando la I y la X que quedan reservadas.

  * **Suma**: se utiliza el signo '+'. Ejemplo: `expresion = 'A+B'`

  * **Resta**: se utiliza el signo '-'. Ejemplo: `expresion = 'A-B'`

  * **Producto**: se utiliza el punto '.'. Ejemplo: `expresion = 'A.B'`

  * **Traspuesta**: se utiliza la 't' minúscula tras la expresión a trasponer. Ejemplos; `expresion = 'At'`, `expresion = '(A+B)t`

  * **Inversa**: se utiliza una comilla simple tras la expresión. Ejemplos: `expresion = "A'"`, `expresion = "(A+B.C)'"`

  * **Adjunta**: se utiliza el asterisco posterior a la matriz o a la expresión. Ejemplos: `expresion = 'A*'`, `expresion = '(A+B)*'`

  * **Asignación**: Puede asignarse directamente el resultado de una expresión a una variable. Ejemplo: `expresion = 'C=A+B'`