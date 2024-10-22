import comandos
import re

mario = (0,0) #variable que almacenara la posicion de mario en la matriz
codigo = open("codigo.txt", "r")
tam_matriz = int(codigo.readline()) #variable que almacenara el tamano de la matriz
matriz = comandos.matrix(tam_matriz)
matriz_segura = comandos.matrix(tam_matriz) #variable que almacenara una copia de la matriz actual por si se encuentra un error en la linea que esta siendo procesada
errores = open("errores.txt", "w")
linea_para_imprimir = "" #variable que almacena los caracteres o enteros que se imprimiran

contador_errores = 0 #variable que si permanece en cero se escribira "no hay errores!" en el archivo errores.txt
contador_lineas = 0 #variable que lleva el conteo de lineas



#failsafe = 0
for string_comandos in codigo:  #ciclo que recorre el archivo codigo.txt
    linea_actual = string_comandos #variable que se escribe en errores.txt si hay algun error en la linea que se esta procesando
    linea_segura = linea_para_imprimir  #variable que guarda los caracteres y enteros a imprimir por si hay un error en la linea que se esta procesando
    
    matriz_segura = comandos.copy_matrix(matriz,matriz_segura) #se hace una copia de la matriz por si hay un error en la linea que se esta procesando
    
    mario_seguro = mario #variable que guarda la posicion de mario por si hay un error en la linea que se esta procesando
    if string_comandos[0] != "(" or string_comandos[-1] != ")": #Si la linea de codigo no viene entre parentesis, se colocan parentesis
        string_comandos = "(" + string_comandos.rstrip() + ")"

    contador_lineas += 1 #se aumenta el numero de lineas
    
    while string_comandos != "": #ciclo que procesa la linea actual
        flag_condicional = False #variable que ayuda a identificar si () es un error o no
        flag_condicional2 = False #variable que ayuda a verificar que las casillas del condicional sean mayor a cero
        operacion_en_parentesis = re.search(r"\((?:[^)(]+)*\)", string_comandos) #variable que reconoce el parentesis mas interno presente en la linea que esta siendo procesada 
       
        if operacion_en_parentesis is not None: #Verifica que la operacion en parentesis se haya reconocido correctamente
            oep_span = operacion_en_parentesis.span()[0] #variable que almacena el indice donde comienza la operacion en parentesis que servira para borrarla de la variable string_comandos posteriormente
            operacion_en_parentesis = operacion_en_parentesis.group() #(si algo falla debo quitar esto y volver al formato de la linea 28)
            
            condicional = re.search(r"^\?((<|>|U|D)([1-9][0-9]*|0))+((\?((<|>|U|D)([1-9][0-9]*|0))+)+)?",operacion_en_parentesis[1:-1]) #variable que reconoce si hay una condicional 
            span_con = re.search(r"\?((<|>|U|D)([1-9][0-9]*|0))+((\?((<|>|U|D)([1-9][0-9]*|0))+)+)?", string_comandos)#variable que encuentra el condicional en la variable string_comandos lo que ayudara a removerla posteriormenta
            
            if condicional is not None: #Se verifica que se haya reconocido correctamente el condicional 
                span_con = span_con.span() 
                condicional = condicional.group()
                condicional_para_borrar = condicional #variable que servira para borrar la condicional de la variable condicional
                luigi = mario #variable que copia la posicion de mario. Esta variable se utilizara para ver los valores que requieren los condicionales y las operaciones X[dir] e Y[dir]
                while condicional != "": #ciclo que procesa la condicional encontrada
                    print("condicional while: ", condicional)
                    if condicional[0] == "?": #elimina el caracter "?" de la variable condicional
                        condicional = condicional[1:]
                        if luigi != mario and matriz[luigi[0]][luigi[1]] <= 0: #evita que se sigan leyendo los condicionales anidados si la casilla que apunta [dir] es menor o igual a cero
                            flag_condicional2 = True
                            
                    direccion = re.search(r"^((<|>|U|D)([1-9][0-9]*)|0)",condicional) #reconoce  las direcciones del condicional
                    if direccion.group()[0] == "<":
                        luigi = comandos.left(int(direccion.group()[1:]),luigi,tam_matriz)
                    elif direccion.group()[0] == ">":
                        luigi = comandos.right(int(direccion.group()[1:]),luigi,tam_matriz)
                    elif direccion.group()[0] == "U":
                        luigi = comandos.U(int(direccion.group()[1:]),luigi,tam_matriz)
                    elif direccion.group()[0] == "D":
                        luigi = comandos.D(int(direccion.group()[1:]),luigi,tam_matriz)
                    condicional = condicional.replace(direccion.group(),"",1) #elimina la [dir] ya procesada de la lista de direcciones del condicional
                
                if matriz[luigi[0]][luigi[1]] > 0 and flag_condicional2 == False: #verifica que la casilla al final de todos los condicionales anidados sea mayor a cero
                    string_comandos = string_comandos[:span_con[0]] + string_comandos[span_con[1]:] #borra el condicional de la variable string_comandos, excepto el comando a realizar que se procesara posteriormente
                    operacion_en_parentesis = operacion_en_parentesis.replace(condicional_para_borrar,"",1) #borra el condicional de la variable operacion_en_parentesis, excepto el comando a realizar que se procesara posteriormente
                    flag_condicional = True #reestablece el valor de flag_condicional por si mas adelante hay que procesar otro condicional
                    
                else:
                    flag_condicional = True #reestablece el valor de flag_condicional por si mas adelante hay que procesar otro condicional
                    condicional_fallida = re.search(r"\?((<|>|U|D)[0-9]+)+((\?((X|Y)?(<|>|U|D)([1-9][0-9]*|0))+)+)?([ABRZ]|(S|L)(c|e)|((X|Y)((<|>|U|D)[0-9]+)+))",string_comandos) #variable que ayuda a borrar el condicional por completo de la variable string_comandos, dado que no se debe hacer su operacion
                    op_fallida = re.search(r"\?((<|>|U|D)[0-9]+)+((\?((X|Y)?(<|>|U|D)([1-9][0-9]*|0))+)+)?([ABRZ]|(S|L)(c|e)|((X|Y)((<|>|U|D)[0-9]+)+))",operacion_en_parentesis) #variable que ayuda a borrar el condicional por completo de la variable operacion_en_parentesis, dado que no se debe hacer su operacion
                    string_comandos = string_comandos = string_comandos[:condicional_fallida.span()[0]] + string_comandos[condicional_fallida.span()[1]:] #borra el condicional completo de la variable string_comandos
                    operacion_en_parentesis = operacion_en_parentesis.replace(condicional_fallida.group(),"",1) #borra el condicional completo de la variable operacion_en_parentesis
                    
            operacion = re.search(r"([ABRZ]|(X|Y)?(<|>|U|D)([1-9][0-9]*|0)|(L|S)(c|e))", operacion_en_parentesis[1:-1]) #variable que reconoce una por una las operaciones presentes 
            while operacion != "": #ciclo que procesa las operaciones
                if operacion is not None: #si no reconoce una operacion rompe el ciclo y anota la linea como un error
                    operacion = operacion.group()
                    unica_operacion = re.search(r"[ABRZ]", operacion) #filtra las operaciones [ABRZ]
                    if unica_operacion is not None: 
                        uo0 = unica_operacion.span()[0]
                        uo1 = unica_operacion.span()[1]
                        if unica_operacion.group() == "A": #Estas facilmente se podrian hacer con REGEX
                            matriz = comandos.A(matriz, mario)
                        elif unica_operacion.group() == "B":
                            matriz = comandos.B(matriz, mario)
                        elif unica_operacion.group() == "R":
                            matriz = comandos.R(matriz, mario)
                        elif unica_operacion.group() == "Z":
                            matriz = comandos.Z(tam_matriz)
                        operacion = operacion.replace(unica_operacion.group(),"",1) #borra la operacion de la variable operacion
                        x_span = oep_span + 1 + uo0
                        y_span = x_span + uo1
                        string_comandos = string_comandos[:x_span] + string_comandos[y_span:] #se borra la operacion de la variable string_comandos
                    unica_operacion = re.search(r"^((<|>|U|D)([1-9][0-9]*|0))", operacion) #filtra las direcciones
                    if unica_operacion is not None: 
                        uo0 = unica_operacion.span()[0]
                        uo1 = unica_operacion.span()[1]
                        if unica_operacion.group()[0] == "<":
                            mario = comandos.left(int(unica_operacion.group()[1:]),mario,tam_matriz)
                        elif unica_operacion.group()[0] == ">":
                            mario = comandos.right(int(unica_operacion.group()[1:]),mario,tam_matriz)
                        elif unica_operacion.group()[0] == "U":
                            mario = comandos.U(int(unica_operacion.group()[1:]),mario,tam_matriz)
                        elif unica_operacion.group()[0] == "D":
                            mario = comandos.D(int(unica_operacion.group()[1:]),mario,tam_matriz)
                        operacion = operacion.replace(unica_operacion.group(),"",1) #borra la direccion de la variable operacion
                        x_span = oep_span + 1 + uo0
                        y_span = x_span + uo1
                        string_comandos = string_comandos[:x_span] + string_comandos[y_span:] #se borra la direccion de la variable string_comandos
                    prod_div = re.search(r"(X|Y)((<|>|U|D)([1-9][0-9]*|0))+", operacion) #filtra las operaciones X[dir] e Y[dir]
                    prod_div_str_comandos = re.search(r"(X|Y)((<|>|U|D)[0-9]+)+", string_comandos) #variable que ayuda a borrar las operacions X[dir] e Y[dir] de la variable string_comandos
                    if prod_div is not None: 
                        x_y = prod_div.group()[0]
                        prod_div_span_str_comandos = prod_div_str_comandos.span()
                        prod_div_op = re.search(r"((<|>|U|D)([1-9][0-9]*|0))+", operacion_en_parentesis[1:-1])
                        prod_div_op = prod_div_op.group()
                        luigi = mario
                        while prod_div_op != "": #ciclo que se ocupa de la secuencia de direcciones de la operacion
                            unica_operacion = re.search(r"(<|>|U|D)([1-9][0-9]*|0)", prod_div_op) 
                            if unica_operacion.group()[0] == "<":
                                luigi = comandos.left(int(unica_operacion.group()[1:]),luigi,tam_matriz)
                            elif unica_operacion.group()[0] == ">":
                                luigi = comandos.right(int(unica_operacion.group()[1:]),luigi,tam_matriz)
                            elif unica_operacion.group()[0] == "U":
                                luigi = comandos.U(int(unica_operacion.group()[1:]),luigi,tam_matriz)
                            elif unica_operacion.group()[0] == "D":
                                luigi = comandos.D(int(unica_operacion.group()[1:]),luigi,tam_matriz)
                            prod_div_op = prod_div_op.replace(unica_operacion.group(),"",1) #borra la operacion de la variable  prod_div_op
                        if x_y == "X":
                            matriz = comandos.X(luigi,mario,matriz)
                        else:
                            matriz = comandos.Y(luigi, mario, matriz)
                        operacion = ""
                        string_comandos = string_comandos[:prod_div_span_str_comandos[0]] + string_comandos[prod_div_span_str_comandos[1]:] #borra las operaciones X[dir] e Y[dir] de la variable string_comandos
                    slce = re.search(r"(L|S)(c|e)", operacion) #filtra las operaciones (L|S)(c|e)
                    if slce is not None:
                        uo0 = slce.span()[0]
                        uo1 = slce.span()[1]
                        slce = slce.group()
                        if slce[0] == "L":
                            linea_para_imprimir += comandos.L(slce[1],mario,matriz)
                        elif slce[0] == "S":
                            print(linea_para_imprimir + comandos.S(slce[1],matriz))
                            linea_para_imprimir = ""
                        operacion = operacion.replace(slce,"",1)
                        x_span = oep_span + 1 + uo0
                        y_span = x_span + uo1
                        string_comandos = string_comandos[:x_span] + string_comandos[y_span:]
                else:
                    break
            cache = re.search(r"\((X|Y)?\)",string_comandos) #variable que se deshace de los parentesis residuales de las operaciones ya procesadas en la variable string_comandos
            if cache is not None:
                string_comandos = string_comandos.replace(cache.group(),"",1)
                if string_comandos == "()":
                    string_comandos = ""
        elif string_comandos == "()":
            break
        if operacion_en_parentesis is None : #reconoce los errores presentes en las lineas y los escribe en el archivo errores.txt y reestablece los valores de mario y la matriz a los de la linea anterior
            contador_errores += 1
            mario = mario_seguro 
            matriz = comandos.copy_matrix(matriz_segura,matriz)
            linea_para_imprimir = linea_segura 
            errores.write(str(contador_lineas) + " " + linea_actual)
            break
        elif re.search(r"((?<!(\?|<|>|A|D|X|Y))[ABRZ]|(X|Y)?(<|>|U|D)([1-9][0-9]*|0)|(L|S)(c|e))", operacion_en_parentesis[1:-1]) is None and flag_condicional == False:
            contador_errores += 1
            mario = mario_seguro
            matriz = comandos.copy_matrix(matriz_segura,matriz)
            linea_para_imprimir = linea_segura
            errores.write(str(contador_lineas) + " " + linea_actual)
            break
codigo.close()
if contador_errores == 0: #verifica que no se hayan encontrado errores en el archivo codigo.txt 
    errores.write("No hay errores!")
errores.close()
if linea_para_imprimir != "": #imprime la "cola" de prints si es que no se encuentra un Se en el archivo
    print(linea_para_imprimir)
for line in matriz:
    print(line)