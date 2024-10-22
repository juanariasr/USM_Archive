'''
Nombre: matrix
______________
tam_matriz: integer
______________
Crea una matriz cuadrada de tamaño "tam_matriz" y la retorna
'''
def matrix(tam_matriz):
    filas = []
    for numero in range(tam_matriz):
        filas.append([])
    a = 0
    while a < tam_matriz:
        for num in range(tam_matriz):
            filas[num].append(0)
        a += 1
    return filas


'''
Nombre: copy_matrix
______________
matriz: list
matriz2: list
______________
Recibe una matriz y la copia en "matriz2", retornando la copia, o sea, "matriz2" 
'''
def copy_matrix(matriz,matriz2):
    lineas = 0
    for line in matriz:
        columnas = 0
        for column in matriz:
            matriz2[lineas][columnas] = matriz[lineas][columnas]
            columnas += 1
        lineas += 1
    return matriz2

'''
Nombre: U
______________
numero: string
mario: tuple
tam_matriz: integer
______________
actualiza la primera coordenada de la tupla "mario" (mario[0]), restando uno la cantidad de veces que indique "numero". Respetando la matriz ciclica. Retorna la tupla "mario" actualizada
'''
def U(numero, mario, tam_matriz):
    numero = int(numero)
    if numero == 0:
        return mario
    c = 0
    while c < numero:
        if mario[0] == 0:
            mario = (tam_matriz-1, mario[1])
            c += 1
        else:
            mario = (mario[0]-1,mario[1])
            c += 1        
    return mario

'''
Nombre: D
______________
numero: string
mario: tuple
tam_matriz: integer
______________
actualiza la primera coordenada de la tupla "mario" (mario[0]), sumando uno la cantidad de veces que indique "numero". Respetando la matriz ciclica. Retorna la tupla "mario" actualizada
'''
def D(numero, mario, tam_matriz):
    numero = int(numero)
    if numero == 0:
        return mario
    c = 0
    while c < numero:
        if mario[0] == tam_matriz-1:
            mario = (0, mario[1])
            c += 1
        else:
            mario = (mario[0]+1, mario[1])
            c += 1
    return mario

'''
Nombre: left
______________
numero: string
mario: tuple
tam_matriz: integer
______________
actualiza la segunda coordenada de la tupla "mario" (mario[1]), restando uno la cantidad de veces que indique "numero". Respetando la matriz ciclica. Retorna la tupla "mario" actualizada
'''
def left(numero, mario, tam_matriz):
    numero = int(numero)
    if numero == 0:
        return mario
    c = 0
    while c < numero:
        if mario[1] == 0:
            mario = (mario[0], tam_matriz-1)
            c += 1
        else:
            mario = (mario[0],mario[1]-1)
            c += 1
    return mario

'''
Nombre: right
______________
numero: string
mario: tuple
tam_matriz: integer
______________
actualiza la primera coordenada de la tupla "mario" (mario[1]), sumando uno la cantidad de veces que indique "numero". Respetando la matriz ciclica. Retorna la tupla "mario" actualizada
'''
def right(numero, mario, tam_matriz):
    numero = int(numero)
    if numero == 0:
        return mario
    c = 0
    while c < numero:
        if mario[1] == tam_matriz-1:
            mario = (mario[0], 0)
            c += 1
        else:
            mario = (mario[0],mario[1]+1)
            c += 1
    return mario

'''
Nombre: A
______________
matriz: list
mario: tuple
______________
aumenta en 1 el valor de la casilla de la matriz que corresponde a la posicion de "mario". Retorna la matriz actualizada
'''
def A(matriz, mario):
    matriz[mario[0]][mario[1]] += 1
    return matriz

'''
Nombre: B
______________
matriz: list
mario: tuple
______________
disminuye en 1 el valor de la casilla de la matriz que corresponde a la posicion de "mario". Retorna la matriz actualizada
'''
def B(matriz, mario):
    matriz[mario[0]][mario[1]] -= 1
    return matriz

'''
Nombre: X
______________
luigi: tuple
mario: tuple
matriz: tuple
______________
multiplica el valor de la casilla que corresponde a la posicion de "mario" por el valor de la casilla que corresponde a la posicion "luigi". Retorna la matriz actualizada
'''
def X(luigi, mario, matriz):
    valor_casilla = matriz[mario[0]][mario[1]]
    valor_factor = matriz[luigi[0]][luigi[1]]
    valor_casilla *= valor_factor
    matriz[mario[0]][mario[1]] = valor_casilla
    
    return matriz

'''
Nombre: Y
______________
luigi: tuple
mario: tuple
matriz: tuple
______________
Divide el valor de la casilla que corresponde a la posicion de "mario" por el valor de la casilla que corresponde a la posicion "luigi". Retorna la matriz actualizada
'''
def Y(luigi, mario, matriz):
    valor_casilla = matriz[mario[0]][mario[1]]
    valor_cociente = matriz[luigi[0]][luigi[1]]
    if valor_cociente == 0:
        return matriz
    valor_casilla //= valor_cociente
    matriz[mario[0]][mario[1]] = valor_casilla
    return matriz

'''
Nombre: L
______________
ce: string
mario: tuple
matriz: tuple
______________
Retorna el valor de la casilla que corresponde a la posicion de "mario" su version entero transformado a string (si "ce" es c), excepto si el valor es 127 porque ahi imprime un salto de linea o en formato caracter (si "ce" es e). 
'''
def L(ce, mario, matriz):
    if ce == "c":
        if matriz[mario[0]][mario[1]] >= 25 and matriz[mario[0]][mario[1]] < 127:
            return chr(matriz[mario[0]][mario[1]])
        elif matriz[mario[0]][mario[1]] == 127:
            print("\n")
            return ""
    return str(matriz[mario[0]][mario[1]])

'''
Nombre: R
______________
matriz: list
mario: tuple
______________
Actualiza el valor de la matriz correspondiente a la posicion de "mario" y retorna la matriz actualizada
'''
def R(matriz, mario):
    matriz[mario[0]][mario[1]] = 0
    return matriz

'''
Nombre: Z
______________
tam_matriz: integer
______________
crea una nueva matriz con todos los valores en 0 y la retorna
'''
def Z(tam_matriz):
    filas = []
    for numero in range(tam_matriz):
        filas.append([])
    a = 0
    while a < tam_matriz:
        for num in range(tam_matriz):
            filas[num].append(0)
        a += 1
    return filas
'''
Nombre: S
______________
ce: string
matriz: list
______________
Retorna todos los valores de la matriz en una linea en formato caracter si "ce" es "c", excepto si el valor es 127 porque ahi imprime la linea y un salto de linea, o en su version entera convertido a string si "ce" es "e" 
'''
def S(ce, matriz):
    linea = ""
    if ce == "c":
        for line in matriz:
            for column in line:
                if column >= 25 and column < 127:
                    linea += chr(column)   
                elif column == 127:
                    print(linea)
                    linea = ""        
        return linea
    for line in matriz:
            for column in line:
                linea += str(column)
    return linea