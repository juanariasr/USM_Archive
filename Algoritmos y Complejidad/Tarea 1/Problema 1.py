def problema1(l, c_deno, vuelto):
    c_monedas = float("inf") #variable que guardara la cantidad minima actual de monedas para el vuelto
    if (vuelto == 0): #Full caso base cuando ya no queda vuelto por dar
        return 0
    i = 0
    while i < c_deno:
        if (l[i] <= vuelto): # aun se pueden utilizar monedas con la denominacion que se esta usando actualmente
            m_aux = problema1(l, c_deno, vuelto-l[i]) + 1 #se añade una moneda de la denominacion actual a la cuenta de monedas
            if (m_aux < c_monedas): #se verifica que si la cantidad actual es menor a la cantidad de monedas minima previamente encontrada
                c_monedas = m_aux
        i += 1
    return c_monedas

vuelto = int(input("Ingrese vuelto: "))
c_deno= int(input("Ingrese cantidad de denominaciones: "))
l = []
for i in range(0, c_deno):
    deno = int(input("Ingrese denominacion: "))
    l.append(deno)
print(problema1(l,c_deno,vuelto))