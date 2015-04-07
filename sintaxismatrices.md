# Sintaxis #

Hay dos formas de escribir las matrices.

> ## Forma que usan todas las funciones como entrada ##
Las matrices se representan en listas con dos sublistas en la primera va la matriz escrita en orden de filas y en la segunda las dimensiones de esta.

### Ejemplo ###
```
ex=[[ 1, 2, 3, 4,
      5, 6, 7, 8,
      9,10,11,12],[3,4]]

ex2=[[0, 1, 2,
      3, 4, 5,
      6, 7, 8],[3,3]]

ex3=[[ 0, 1, 2, 3, 4, 5, 
       6, 7, 8, 9,10,11,
      12,13,14,15,16,17,
      18,19,20,21,22,23,
      24,25,26,27,28,29,
      30,31,32,33,34,35],[6,6]]

ex4=[[1],[1,1]]

ex5=[[ 1, 2, 3, 4, 5,
       6, 7, 8, 9,10,
      11,12,13,14,15,
      16,17,18,19,20,
      21,22,23,24,25],[5,5]]
```


> ## Forma opcional ##
Se creó para facilitar la escritura de alguna función. Se representan las filas en sublistas dentro de la lista principal.

### Ejemplo ###
```
ex=[[ 1, 2, 3, 4 ],
    [ 5, 6, 7, 8 ],
    [ 9,10,11,12 ]]

ex2=[[ 0, 1, 2 ],
     [ 3, 4, 5 ],
     [ 6, 7, 8 ]]
```

## Cambio entre formas ##
Para cambiar entre ambos formatos de representación existen 2 funciones:
### Mlistasfilas ###
```
>>> ex=[[1,  2,  3,  4,
>>>      5,  6,  7,  8, 
>>>      9, 10, 11, 12],[3,4]]
>>> print Mlistasfilas(ex)
[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
```
### Mlistadoble ###
```
ex=[[1,  2,  3,  4],
    [5,  6,  7,  8], 
    [9, 10, 11, 12]]
print Mlistadoble(ex)
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],[3,4]]
```