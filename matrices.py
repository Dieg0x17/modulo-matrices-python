#!/usr/bin/env python
## coding: utf-8
# Modulo para operar con matrices (http://code.google.com/p/modulo-matrices-python/)
#
# Authors:
#    Diego Rasero
#    Felipe Hommen
# 
# This python module is distributed under the terms of GPLv3 license
#
# ChangeLog 0.02332-1:
#  [+] Operaciones basicas
#  [+] Obtención de información (diagonales, filas, columnas...)
#  [+] Funciones para cambios de formato
#  [+] Función de errores 
#  [+] Función determinantes 
#  [+] Función traspuestas 

"""Las matrices se representan en listas con dos sublistas en la primera va la matriz escrita en orden de filas y en la segunda las dimensiones de esta"""

#ex=[[ 1, 2, 3, 4,
#      5, 6, 7, 8,
#      9,10,11,12],[3,4]]

#ex2=[[0, 1, 2,
#      3, 4, 5,
#      6, 7, 8],[3,3]]

#ex3=[[ 0, 1, 2, 3, 4, 5, 
#       6, 7, 8, 9,10,11,
#      12,13,14,15,16,17,
#      18,19,20,21,22,23,
#      24,25,26,27,28,29,
#      30,31,32,33,34,35],[6,6]]

#ex4=[[1],[1,1]]

#ex5=[[ 1, 2, 3, 4, 5,
#       6, 7, 8, 9,10,
#      11,12,13,14,15,
#      16,17,18,19,20,
#      21,22,23,24,25],[5,5]]

############## Errores.

def error(n):
    if n==1: return "Fallo de formato, compruebe si es correcta la escritura de la matriz"
    elif n==2: return "Inserte una matriz cuadrada"
    elif n==3: return "La matriz no tiene inversa"
    elif n==4: return "No se puede aplicar Cramer al sistema"

############## Información.
def x(M):
    """Devuelve el número de filas"""
    return M[1][0] # devuelve m

#print x(ex)

def y(M):
    """Devuelve el número de columnas"""
    return M[1][1] # devuelve n

#print y(ex)

def fila(M,f):
    """Devuelve la fila f de la matriz M"""
    if f <= x(M) and f >= 1:
        return M[0][(f-1)*y(M):((f-1)*y(M))+y(M)]

#print fila(ex5,3)

def columna(M,c):
    """Devuelve la columna c de la matriz M"""
    if c <= y(M) and c >= 1:
        A=[]
        for i in range(1,x(M)+1):
            l=fila(M,i)
            A=A+[l[c-1]]
        return A

#print columna(ex5,3)

############## Comprobaciones.

def comprueba(M):
    """comprueba la validez de una matriz"""
    try:
        if len(M[0]) == x(M)*y(M) and len(M[1]) == 2:
            return M
        else:
            error(1)
    except:
        error(1)

#N=23
#print comprueba(N)
#print comprueba(ex)

def cuadrada(M):
    """Verifica que se trata de una matriz cuadrada"""
    if x(M) == y(M):
        return True
    else:
        return False

#print cuadrada(ex)
#print cuadrada(ex3)

def diagonalprincipal(M):
    """ Devuelve la diagonal principal de una matriz"""
    if cuadrada(M):
        D=[]
        for i in range(0,(x(M)*y(M)),(x(M)+1)):
            D.append(M[0][i])
        return D

#print diagonalprincipal(ex3) 

def diagonalsecundaria(M):
    """ Devuelve la diagonal secundaria de una matriz"""
    if cuadrada(M):
        D=[]
        if x(M) == 1:
            D=[[M[0][0]]]
        else:
            for i in range((y(M)-1),(y(M)*(y(M)-1))+1,(y(M)-1)):
                D.append(M[0][i])
        return D

#print diagonalsecundaria(ex3)

def simetrica(M):
    """comprueba la simetria de una matriz"""
    if cuadrada(M):
        num=0
        for i in range(y(M)):
            if fila(M,i)==columna(M,i):
                num=num+1
        if num == y(M):
            return True
        else:
            return False
    else:
        return False

#print simetrica(Midentidad(3))
#print simetrica(ex5)

############## Formato de las matrices.

def Mlistasfilas(M):
    """Cambia el formato de las matrices a una lista con sublistas del tamaño de las columnas"""
    A=[]
    for f in range(1,x(M)+1):
        A.append(fila(M,f))
    return A

#print Mlistasfilas(ex)

def Mlistadoble(M):
    """Cambia el formato de las matrices a una lista con dos sublistas una con todos los elementos y otra con las dimensiones"""
    A=[]
    for i in range(len(M)):
        A+=M[i]
    return [A,[len(M),len(M[0])]]

#ej=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#print Mlistadoble(ej)

def imprime(M):
    """Imprime la matriz de forma ordenada"""
    string=""
    print ""
    for f in range(1,x(M)+1): # rango numero de filas
        for n in fila(M,f):
            if n < 10:
                string=string+"   "+str(n)
            elif n < 100:
                string=string+"  "+str(n)
            else:
                string=string+" "+str(n)
        print string
        string =""
    print ""

#imprime(ex)

############## Creación de matrices.

def Mnula(x, y):
    """ Crea una matriz nula"""
    A = [0]*x*y
    return [A,[x,y]]

#print Mnula(3,6)
#print Mnula(2,2)

def Midentidad(x):
    """ Crea una matriz identidad"""
    A=Mnula(x,x)
    for i in range(0,(x*x),(x+1)):
        A[0][i]=1
    return A

#mi=Midentidad(7)

def Maleatoria():
    """Crea una matriz de dimensiones aleatorias con un numeros aleatorios"""
    pass

############## Operaciones con matrices.

def suma(M1,M2):
    """Suma de dos matrices de las mismas dimensiones"""
    if y(M1)==y(M2) and x(M1)==x(M2):
        A=[]
        for i in range(y(M1)*x(M1)):
            A=A+[M1[0][i]+M2[0][i]]
        return [A,[y(M1),x(M1)]]

#Sol=suma(ex2,Midentidad(3))

def resta(M1,M2):
    """Resta de dos matrices de las mismas dimensiones"""
    if y(M1)==y(M2) and x(M1)==x(M2):
        A=[]
        for i in range(y(M1)*x(M1)):
            A=A+[M1[0][i]-M2[0][i]]
        return [A,[y(M1),x(M1)]]

#Sol=resta(ex2,Midentidad(3))

def prodnr(M,k):
    """Producto de un número real por una matriz"""
    A=[]
    for i in range(y(M)*x(M)):
        A=A+[M[0][i]*k]
    return [A,[y(M),x(M)]]

#Sol=prodnr(ex,23)

def mys(l1,l2):
    """Multiplica dos listas iguales y suma el resultado"""
    if len(l1)==len(l2):
        n=0
        for i in range(len(l1)):
            n+=l1[i]*l2[i]
        return n

def producto(M1,M2):
    """Producto de dos matrices"""
    if y(M1) == x(M2):
        A=[[],[x(M1),y(M2)]]
        for f in range(1,x(M1)+1):
            for c in range(1,y(M2)+1):
                A[0].append(mys(fila(M1,f),columna(M2,c)))
        return A
    else:
        return "Error de formato"

#Sol=producto(ex2,ex)

def potencia(M,n):
    """Potencia de una matriz"""
    if n==1:
        return M
    else:
        A=M
        for i in range(2,n+1):
            A=producto(M,A)
        return A

#Sol=potencia(ex3,7)


############## Determinantes.

def det(M):
    """Resuelve el determinante de la matriz M"""
    if cuadrada(M):
        if y(M)==1:
            return M[0][0]
        elif y(M)==2:
            return (M[0][0]*M[0][3])-(M[0][2]*M[0][1])
        elif y(M)==3:
            return ( (M[0][0]*M[0][4]*M[0][8]) + (M[0][2]*M[0][3]*M[0][7]) + (M[0][1]*M[0][5]*M[0][6]) ) - ( (M[0][2]*M[0][4]*M[0][6]) + (M[0][1]*M[0][3]*M[0][8]) + (M[0][0]*M[0][5]*M[0][7]) )
        else:
            f1=fila(M,1)
            deter=0
            for n in range(y(M)):
                subM=[]
                for nfila in range(2,y(M)+1):
                    fi=fila(M,nfila)
                    del fi[n]
                    subM+=fi
                deter+= f1[n] * ((-1)**n) * det([subM,[y(M)-1,y(M)-1]])
            return deter

#A=[[0,1,2,3,
#    4,5,6,7,
#    8,9,10,11,
#    12,13,14,15],[4,4]]

#print det(A)
#print det(Midentidad(10)) # Un poco lenta 

def traspuesta(M):
    """Devuelve la matriz traspuesta a M"""
    A=[]
    for col in range(1,y(M)+1):
        A+=columna(M,col)
    return [A,[y(M),x(M)]]

#A=[[1,2,3,4,5,6,],[2,3]]
#print traspuesta(A)

def matrizAdjunta(M):
    """Calcula la matriz adjunta de M"""
    if not cuadrada(M):
        raise NameError('La matriz no es cuadrada')
    if x(M) == 1:
        return M[:]
    if x(M) == 2:
        A = [ [ M[0][3], -M[0][2], -M[0][1], M[0][0] ], [2, 2] ]
        return A
    A = Mnula(x(M), y(M))
    for i in range(1, x(M) + 1):
        for j in range(1, y(M) + 1):
            subM = submatriz(M, i, j)
            print subM
            print det(subM)
            A[0][(i - 1) * y(M) + j - 1] = (-1)**(i + j) * det(subM)
    return A

def inversa(M):
    """Devuelve la matriz inversa a M"""
    if cuadrada(M):
        detm=det(M)
        if detm != 0:
            Madj=matrizAdjunta(M)
            return traspuesta(prodnr(Madj,(1/detm)))
        else:
            return error(3)
    else:
        return error(2),error(3)

#A=[[1,2,3,4],[2,2]]
#print inversa(A)

def submatriz(M, f, c):
    """Elimina la fila f y la columna c de una matriz"""
    if x(M) < 2:
        raise NameError("No puedo eliminar la única fila de la matriz")
    if y(M) < 2:
        raise NameError("No puedo eliminar la única columna de la matriz")
    A = [M[0][:], M[1][:]]
    del A[0][(f - 1) * y(A): f * y(A)]
    for i in range(len(A[0]) - y(A) + c, 0, -y(A)):
        del A[0][i - 1]
    A[1][0] = A[1][0] - 1
    A[1][1] = A[1][1] - 1
    return A


def menorescomplementarios():
    pass


def rango(M): # det =!0 mas grande
    pass # analizar por filas o columnas atendiendo a x o y (el más bajo)


############## Sistemas de ecuaciones lineales.
def Mmodcramer(A,S,i):
    csol=columna(S,1)
    B=[]
    for n in range(x(A)):
        fA=fila(A,n+1)
        #print fA
        fA[i]=csol[n]
        B+=fA
    return [B,[x(A),x(A)]]

def cramer(A,S): # A = matriz 
    """Resuelve sistemas empleando el metodo de cramer"""
    da=det(A)
    if da != 0:
        sol=[]
        for i in range(x(A)): #bucle con el numero de incognitas
            xn=det(Mmodcramer(A,S,i))/da
            sol.append(xn)
        return sol # devuelve una lista con las soluciones en orden
    else:
        raise NameError(error(4))

#A=[[1,1,0,
#    0,1,1,
#    1,0,1],[3,3]]

#S=[[3,
#    5,
#    4],[3,1]]

#print cramer(A,S)

def escalonar(M):
    "Devuelve la matriz escalonada"
    #Primero un par de funciones auxiliares
    def simplifica(M):
        for fila in M:
            mcd = 1
            for i in range(2, min([abs(e) for e in fila]) + 1):
                divisor = True
                for e in fila:
                    if e % i != 0:
                        divisor = False
                if divisor:
                    mcd = i
            for i in range(0, len(fila)):
                fila[i] = fila[i] / mcd
                
    def reorganiza_pivote(M, f, c):
        for i in range(f + 1, len(M)):
            if M[i][c] != 0:
                M[f], M[i] = M[i], M[f]
                break
                
    A = Mlistasfilas(M)
    escalon = -1
    for fila in range(0, len(A)):
        simplifica(A)
        escalon = escalon + 1
        if escalon >= len(A[0]): # Se nos agotan las columnas
            break
        while A[fila][escalon] == 0: # Tenemos un cero de pivote. Hay que intercambiar filas
            reorganiza_pivote(A, fila, escalon)
            if A[fila][escalon] == 0: # Si no hay manera, corremos el escalon
                escalon = escalon + 1
                if escalon >= len(A[0]):
                    break
        if escalon >= len(A[0]):
            break
        for fila2 in range(fila + 1, len(A)):
            p1, p2 = A[fila2][escalon], A[fila][escalon]
            for c in range(escalon, len(A[0])):
                A[fila2][c] = A[fila][c] * p1 - A[fila2][c] * p2
    return Mlistadoble(A) 

    
Mex=[[2, 2, 4,-8,
    1,-3,-4, 5,
    2,-1,-1, 0, 
    0,-2,-2, 1],[4,4]]

imprime(escalonar(Mex))

# Solución
#    ┌                 ┐
#    │ -1  -3  -4    5 │
#    │  0  -2  -2    1 │
#A = │  0   0   4  -13 │
#    │  0   0   0    0 │
#    └                 ┘

def Ampliada(A,S):
    """Crea una matriz amploada a partir de dos matrices con el mismo número de filas"""
    M=[]
    for f in range(1,x(A)+1):
        M+=(fila(A,f)+fila(S,f))
    return [M,[x(A),(y(A)+y(S))]]

#imprime(Ampliada(A,S))

def discutir(A,S): 
    rgA=rango(A)
    if rgA != rango(Ampliada(A,S)):
        print "Sistema incompatible (sin solución)"
    else: # falta hacer que prescinda de ecuaciones para luego aplicar cramer 
        if rgA == len(fila(A,1)): # si el rango es igual al numero de incognitas
            print "Sistema compatible determidado (solución unica)"
        elif rgA < len(fila(A,1)): 
            print "Sistema compatible indeterminado (infinitas soluciones)"
