#!/usr/bin/env python
## coding: utf-8
# Modulo para operar con matrices (http://code.google.com/p/modulo-matrices-python/)
# Información sobre el uso de las funciones con ejemplos detallados (http://code.google.com/p/modulo-matrices-python/wiki/Funciones)
# Authors:
#    Diego Rasero
#    Felipe Hommen
# This python module is distributed under the terms of GPLv3 license

import fractions
import string
import sys

dic={} # diccionario como variable global

def error(n):
    if n==1: sys.stderr.write("Fallo de formato, compruebe si es correcta la escritura de la matriz")
    elif n==2: sys.stderr.write("Inserte una matriz cuadrada")
    elif n==3:  sys.stderr.write("La matriz no tiene inversa")
    elif n==4: sys.stderr.write("No se puede aplicar Cramer al sistema")

def x(M):
    """Devuelve el número de filas"""
    return M[1][0]

def y(M):
    """Devuelve el número de columnas"""
    return M[1][1]

def fila(M, f):
    """Devuelve la fila f de la matriz M"""
    if f<=x(M) and f>=1:
        return M[0][(f-1)*y(M):((f-1)*y(M))+y(M)]

def columna(M, c):
    """Devuelve la columna c de la matriz M"""
    if c<=y(M) and c>=1:
        A=[]
        for i in range(1, x(M)+1):
            l=fila(M, i)
            A=A+[l[c-1]]
        return A

def comprueba(M):
    """comprueba la validez de una matriz"""
    try:
        if len(M[0])==x(M)*y(M) and len(M[1])==2:
            return True #M
        else:
            error(1)
            return False #error(1)
    except:
        error(1)
        return False #error(1)

def cuadrada(M):
    """Verifica que se trata de una matriz cuadrada"""
    if x(M)==y(M):
        return True
    else:
        return False
        
def idempotente(M):
    """Comprueba si la matriz es idempotente, es decir si al elevarla al cuadrado es igual a la original"""
    if M == potencia(M, 2):
        return True
    else:
        return False
        
def involutiva(M):
    """Comprueba si la matriz es involutiva, es decir si al elevarla al cuadrado es igual a la identidad"""
    if cuadrada(M):
        if Midentidad(x(M)) == potencia(M, 2):
            return True
        else:
            return False
    else: 
        return False
  
def antisimetrica(M):
    """Comprueba si la matriz es antisimetrica, es decir si su transpuesta negativa es igual a la original"""
    if cuadrada(M):
        if M == prodnr(traspuesta(M) , -1):
            return True
        else: 
            return False
    else: 
        return False

def ortogonal(M):
    """Comprueba si la matriz es ortogonal, es decir si el producto de ella por su transpuesta es la identidad"""
    if cuadrada(M):
        if producto(M, traspuesta(M)) == Midentidad(x(M)):
            return True
        else: return False
    else: return False
       
def diagonalprincipal(M):
    """ Devuelve la diagonal principal de una matriz"""
    if cuadrada(M):
        D=[]
        if x(M)==1:
            D=[[M[0][0]]]
        else:
            for i in range(0, (x(M)*y(M)), (x(M)+1)):
                D.append(M[0][i])
        return D

def diagonalsecundaria(M):
    """ Devuelve la diagonal secundaria de una matriz"""
    if cuadrada(M):
        D=[]
        if x(M)==1:
            D=[[M[0][0]]]
        else:
            for i in range((y(M)-1), (y(M)*(y(M)-1))+1, (y(M)-1)):
                D.append(M[0][i])
        return D

def simetrica(M):
    """comprueba la simetria de una matriz"""
    if cuadrada(M):
        num=0
        for i in range(y(M)):
            if fila(M, i)==columna(M, i):
                num=num+1
        if num==y(M):
            return True
        else:
            return False
    else:
        return False

def Mlistasfilas(M):
    """Cambia el formato de las matrices a una lista con sublistas del tamaño de las columnas"""
    A=[]
    for f in range(1, x(M)+1):
        A.append(fila(M, f))
    return A

def Mlistadoble(M):
    """Cambia el formato de las matrices a una lista con dos sublistas una con todos los elementos y otra con las dimensiones"""
    A=[]
    for i in range(len(M)):
        A+=M[i]
    return [A, [len(M), len(M[0])]]

def imprime(M):
    """Imprime la matriz de forma ordenada"""
    string=""
    print("")
    for f in range(1, x(M)+1):
        for n in fila(M, f):
            if n<10:
                string=string+"   "+str(n)
            elif n<100:
                string=string+"  "+str(n)
            else:
                string=string+" "+str(n)
        print(string)
        string=""
    print("")

def Mnula(x, y):
    """ Crea una matriz nula"""
    A=[0]*x*y
    return [A, [x, y]]

def Midentidad(x):
    """ Crea una matriz identidad"""
    A=Mnula(x, x)
    for i in range(0, (x*x), (x+1)):
        A[0][i]=1
    return A

def Maleatoria():
    """Crea una matriz de dimensiones aleatorias con un numeros aleatorios"""
    pass

def suma(M1, M2):
    """Suma de dos matrices de las mismas dimensiones"""
    if y(M1)==y(M2) and x(M1)==x(M2):
        A=[]
        for i in range(y(M1)*x(M1)):
            A=A+[M1[0][i]+M2[0][i]]
        return [A, [y(M1), x(M1)]]

def resta(M1, M2):
    """Resta de dos matrices de las mismas dimensiones"""
    if y(M1)==y(M2) and x(M1)==x(M2):
        A=[]
        for i in range(y(M1)*x(M1)):
            A=A+[M1[0][i]-M2[0][i]]
        return [A, [y(M1), x(M1)]]

def prodnr(M, k):
    """Producto de un número real por una matriz"""
    A=[]
    for i in range(y(M)*x(M)):
        A=A+[M[0][i]*k]
    return [A, [y(M), x(M)]]

def producto(M1, M2):
    """Producto de dos matrices"""
    def mys(l1, l2):
        """Multiplica dos listas iguales y suma el resultado"""
        if len(l1)==len(l2):
            n=0
            for i in range(len(l1)):
                n+=l1[i]*l2[i]
            return n

    if y(M1)==x(M2):
        A=[[], [x(M1), y(M2)]]
        for f in range(1, x(M1)+1):
            for c in range(1, y(M2)+1):
                A[0].append(mys(fila(M1, f), columna(M2, c)))
        return A
    else:
        return error(1)

def potencia(M, n):
    """Potencia de una matriz"""
    if n==1:
        return M
    else:
        A=M
        for i in range(2, n+1):
            A=producto(M, A)
        return A

def det(M):
    """Resuelve el determinante de la matriz M"""
    if cuadrada(M):
        if y(M)==1:
            return M[0][0]
        elif y(M)==2:
            return (M[0][0]*M[0][3])-(M[0][2]*M[0][1])
        elif y(M)==3:
            return ((M[0][0]*M[0][4]*M[0][8])+(M[0][2]*M[0][3]*M[0][7])+(M[0][1]*M[0][5]*M[0][6]))-((M[0][2]*M[0][4]*M[0][6])+(M[0][1]*M[0][3]*M[0][8])+(M[0][0]*M[0][5]*M[0][7]))
        else:
            f1=fila(M, 1)
            deter=0
            for n in range(y(M)):
                subM=[]
                for nfila in range(2, y(M)+1):
                    fi=fila(M, nfila)
                    del fi[n]
                    subM+=fi
                deter+=f1[n]*((-1)**n)*det([subM, [y(M)-1, y(M)-1]])
            return deter

def traspuesta(M):
    """Devuelve la matriz traspuesta a M"""
    A=[]
    for col in range(1, y(M)+1):
        A+=columna(M, col)
    return [A, [y(M), x(M)]]

def matrizAdjunta(M):
    """Calcula la matriz adjunta de M"""
    if not cuadrada(M):
        raise NameError('La matriz no es cuadrada')
    if x(M)==1:
        return M[:]
    if x(M)==2:
        A=[ [ M[0][3],-M[0][2],-M[0][1], M[0][0] ], [2, 2] ]
        return A
    A=Mnula(x(M), y(M))
    for i in range(1, x(M)+1):
        for j in range(1, y(M)+1):
            subM=submatriz(M, i, j)
            A[0][(i-1)*y(M)+j-1]=(-1)**(i+j)*det(subM)
    return A

def inversa(M):
    """Devuelve la matriz inversa a M"""
    if cuadrada(M):
        detm=det(M)
        if detm!=0:
            Madj=matrizAdjunta(M)
            return traspuesta(prodnr(Madj, (fractions.Fraction(1 , detm))))
        else:
            return error(3)
    else:
        return error(2), error(3)

def submatriz(M, f, c):
    """Elimina la fila f y la columna c de una matriz (menor complementario)"""
    if x(M)<2:
        raise NameError("No puedo eliminar la única fila de la matriz")
    if y(M)<2:
        raise NameError("No puedo eliminar la única columna de la matriz")
    A=[M[0][:], M[1][:]]
    del A[0][(f-1)*y(A): f*y(A)]
    for i in range(len(A[0])-y(A)+c, 0,-y(A)):
        del A[0][i-1]
    A[1][0]=A[1][0]-1
    A[1][1]=A[1][1]-1
    return A

def rango(M):
    A=Mlistasfilas(escalonar(M))
    ceros=[0]*len(A[0])
    return len(A)-A.count(ceros)

def cramer(A, S):
    """Resuelve sistemas empleando el metodo de cramer"""
    def Mmodcramer(A, S, i):
        csol=columna(S, 1)
        B=[]
        for n in range(x(A)):
            fA=fila(A, n+1)
            fA[i]=csol[n]
            B+=fA
        return [B, [x(A), x(A)]]
    da=det(A)
    if da!=0:
        sol=[]
        for i in range(x(A)):
            xn=det(Mmodcramer(A, S, i))/da
            sol.append(xn)
        return sol
    else:
        raise NameError(error(4))

def escalonar(M):
    "Devuelve la matriz escalonada"
    #Primero una funcion auxiliar

    def reorganiza_pivote(M, f, c):
        for i in range(f+1, len(M)):
            if M[i][c]!=0:
                M[f], M[i]=M[i], M[f]
                break

    A=Mlistasfilas(M)
    escalon=-1
    for fila in range(0, len(A)):
        escalon=escalon+1
        if escalon>=len(A[0]): # Se nos agotan las columnas
            break
        while A[fila][escalon]==0: # Tenemos un cero de pivote. Hay que intercambiar filas
            reorganiza_pivote(A, fila, escalon)
            if A[fila][escalon]==0: # Si no hay manera, corremos el escalon
                escalon=escalon+1
                if escalon>=len(A[0]):
                    break
        if escalon>=len(A[0]):
            break
        for fila2 in range(fila+1, len(A)):
            p1, p2 = A[fila2][escalon], A[fila][escalon]
            for c in range(escalon, len(A[0])):
                A[fila2][c] = A[fila][c]*p1 - A[fila2][c]*p2
    return Mlistadoble(A)

def ampliada(A, S):
    """Crea una matriz ampliada a partir de dos matrices con el mismo número de filas"""
    M=[]
    for f in range(1, x(A)+1):
        M+=(fila(A, f)+fila(S, f))
    return [M, [x(A), (y(A)+y(S))]]

def discutir(A, S):
    rgA=rango(A)
    if rgA!=rango(Ampliada(A, S)):
        print("Sistema incompatible (sin solución)")
        return 0
    else: 
        if rgA==len(fila(A, 1)):
            print("Sistema compatible determidado (solución unica)")
            return 1
        elif rgA<len(fila(A, 1)):
            print("Sistema compatible indeterminado (infinitas soluciones)")
            return 2

def evalua(expresion):
	"""Evalua una expresion matricial. Por ahora acepta sumas ,restas y productos"""
	def formatea(expresion):
		
		if expresion.count('(') != expresion.count(')'):
			return None # No ha la misma cantidad de parentesis abiertos que cerrados
		cuenta = 0
		for i in range(len(expresion)):
			if expresion[i] == '(':
				cuenta = cuenta + 1
			elif expresion[i] == ')':
				cuenta = cuenta - 1
			if cuenta < 0:
				return None # Hemos encontrado un parentesis que cierra antes de abrir
				
		expresion = expresion.replace(' ', '')	# Eliminamos los espacios
		
		expresion = expresion.replace(')(', ').(')
		for i in range(0, len(expresion) - 1):
			if expresion[i].isupper() and expresion[i + 1].isupper():
				expresion = expresion[:i + 1] + '.' + expresion[i + 1:] # introduce punto entre dos mayusculas seguidas
			
		return expresion
        
    
	def calcula(expresion):
		while expresion[0] == '(' and expresion[-1:] == ')':
			expresion = expresion[1:-1] # Quitamos parentesis globales si los hay
			
		if expresion in list(dic.keys()): # Si es directamente el identificador de una matriz, devovemos su valor
			return dic[expresion]
			
		s = hazsumas(expresion)
		if s != None :
			return s
			
		s = hazrestas(expresion)
		if s != None:
			return s
			
		s = hazproductos(expresion)
		if s != None:
			return s
			
		s = hazpotencias(expresion)
		if s != None:
			return s
			
		s = haztraspuesta(expresion)
		if s != None:
			return s
			
		s = hazinversa(expresion)
		if s != None:
			return s
			
		return None	# Esto si no ha habido exito con ninguno de los anteriores intentos
				
	
	def hazsumas(expresion):
		
		i=0
		p = 0 # nivel de parentesis
		marca = 0
		operandos = []
		
		while i < len(expresion):	# Buscamos sumas globales
			if expresion[i] == '(':
				p = p + 1
			elif expresion[i] == ')':
				p = p - 1
			elif expresion[i] == '+' and p == 0:
				operandos.append(expresion[marca:i]) # Incluimos desde la marca hasta este "+"
				marca = i + 1
			i = i + 1
		
		operandos.append(expresion[marca:])	# Incluimos todo lo que va despues del ultimo "+"
		
		if marca != 0: # Hemos encontrado una suma primaria
			if len(operandos) == 1: # Una suma de una sola matriz. Podria ser
				return calcula(operandos[0])
			else: #Suma esperada de varias matrices
				acumulado = calcula(operandos[0])
				for i in operandos[1:]:
					acumulado = suma(acumulado, calcula(i))
				return acumulado
		else:
			return None
			
	def hazrestas(expresion):
		i=0
		p = 0
		marca = 0
		operandos = []
		
		while i < len(expresion):	# Buscamos restas globales
			if expresion[i] == '(':
				p = p + 1
			elif expresion[i] == ')':
				p = p - 1
			elif expresion[i] == '-' and p == 0 and i != 0:
				operandos.append(expresion[marca:i])
				marca = i + 1
			i = i + 1
		operandos.append(expresion[marca:])
		if marca != 0: # Hemos encontrado restas primarias
			if len(operandos) == 1: # Una resta de una sola matriz. Podria ser
				M = calcula(operandos[0])
				return prodnr(M, -1)
			else: # Resta esperada de varias matrices
				if expresion[0] != '-': #La primera no es negativa
					acumulado = calcula(operandos[0])
				else: # La primera es negativa
					M=calcula(operandos[0])
					acumulado = prodnr(M, -1)
				for i in operandos[1:]:
					acumulado = resta(acumulado, calcula(i))
			return acumulado
		else:
			return None
		
	def hazproductos(expresion):
		i=0
		p = 0
		marca = 0
		operandos = []
		while i < len(expresion):	# Buscamos productos globales
			if expresion[i] == '(':
				p = p + 1
			elif expresion[i] == ')':
				p = p - 1
			elif expresion[i] == '.' and p == 0:
				operandos.append(expresion[marca:i])
				marca = i + 1
			i = i + 1
		operandos.append(expresion[marca:])
		if marca != 0: # Hemos encontrado productos
			if len(operandos) < 2:
				return None # Necesitamos al menos dos operandos
			else:
				acumulado = calcula(operandos[0])
				for i in operandos[1:]:
					r = calcula(i)
					if isinstance(acumulado, list) and isinstance(r, list):
						acumulado = producto(acumulado, r)
					elif isinstance(acumulado, list) and not isinstance(r, list):
						acumulado = prodnr(acumulado, r)
					elif not isinstance(acumulado, list) and isinstance(r, list):
						acumulado = prodnr(acumulado, r)
					elif not isinstance(acumulado, list) and not isinstance(r, list):
						acumulado = acumulado * r
				return acumulado
		return None
		
	def hazpotencias(expresion):
		# Suponemos que en la expresión pasada como parametro hay una unica potencia. A la izquerda está la base, y a la derecha hay un exponente entero
		i = 0
		p = 0
		encontrado = False
		while i < len(expresion):
			if expresion[i] == '(':
				p = p + 1
			elif expresion[i] == ')':
				p = p - 1
			elif expresion[i] == '^' and p == 0:
				base = expresion[:i]
				exponente = int(expresion[i + 1:])
				encontrado = True
			i = i + 1
		if not encontrado:	# No hay potencias fuera de parentesis
			return None
		n = abs(exponente)
		M = evalua(base)
		acumulado = prodnr(M, 1)	# Esto es para hacer una copia, no un clon (o como quiera que se diferencie esto)
		for i in range(n):
			acumulado = producto(acumulado, M)
		if n != exponente:
			return inversa(acumulado)	# El exponente era negativo
		else:
			return acumulado
			
	def haztraspuesta(expresion):
		# La letra "t" debe ser el ultimo caracter de la expresion, ¿no?
		if expresion[-1:] != 't':
			return None
		else:
			M = calcula(expresion[:-1])
			return traspuesta(M)
		
	def hazinversa(expresion):
		# La prima debe ser el ultimo caracter de la expresion, ¿no?
		if expresion[-1:] != "'":
			return None
		else:
			M = calcula(expresion[-1:])
			return inversa(M)
				
	expresion = formatea(expresion)
	return calcula(expresion)
	

def insM(letra,M):
    """Función que inserta una nueva matriz al diccionario de matrices"""
    if len(letra) > 1:
        letra=letra[0] #condición para que solo sea un caracter
    letra=letra.upper()
    dic[letra]=M
    
def latex(M):
	if not comprueba(M):	# La propia funcion comprueba ya devuelve un mensaje de error
		return None
	prefijo = "\\begin{pmatrix} "
	sufijo = "\\end{pmatrix}"
	expresion = prefijo
	M = Mlistasfilas(M)
	for f in M:
		for c in range(len(f)):
			if c == 0:
				expresion = expresion + str(f[c])
			else:
				expresion = expresion + ' & ' + str(f[c])
		expresion = expresion + " \\\\ "
	expresion = expresion + sufijo
	return expresion
