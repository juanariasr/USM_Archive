def problema2(l_inicial, largo_lista, resultado, suma,lista_resultados):
    if (suma == 0) :
        resultado.sort()
        if resultado not in lista_resultados:
            lista_resultados.append(resultado)
        return "NADA"
    elif (largo_lista == 0):
        return "NADA"
    else :
        problema2(l_inicial, largo_lista - 1, resultado, suma,lista_resultados)
        aux = [] + resultado
        aux.append(l_inicial[largo_lista - 1])
        problema2(l_inicial, largo_lista - 1, aux, suma - l_inicial[largo_lista - 1],lista_resultados)
    if len(lista_resultados) != 0:
        return lista_resultados
    else:
        return "NADA"


l = []
suma = int(input("Ingrese el numero a encontrar mediante sumas: "))
c_enteros = int(input("Ingrese el largo de la lista con los enteros: "))
lista=[]
auxiliar = 0
while c_enteros > auxiliar :
    numero = int(input("Ingrese el entero: "))
    l.append(numero)
    auxiliar += 1


print("Suma de " + str(suma), ":")
funcion= problema2(l, c_enteros, [], suma,lista)
contador = 0
if funcion!= "NADA":
    while contador < len(funcion):
        string=""
        if len(funcion[contador]) == 1:
            print(funcion[contador][0])
            contador += 1
        else:
            contador_dos = 0
            while len(funcion[contador]) > contador_dos:
                string += str(funcion[contador][contador_dos])
                string += "+"
                contador_dos += 1
            print(string[:-1])
            contador += 1
else:
    print(funcion)