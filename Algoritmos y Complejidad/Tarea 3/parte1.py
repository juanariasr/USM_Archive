from math import floor

def mediana(A, B):
    m1 = A[floor((len(A))/2)]
    m2 = B[floor((len(B))/2)]
    if m1 == m2:
        return m1
    elif len(A) == 1 and len(B) == 1:
        return m2
    elif len(A) == 1 and len(B) != 1:
        return mediana(A, B[:floor((len(B))/2)])
    elif len(B) == 1 and len(A) != 1:
        return mediana(A[floor((len(A))/2):], B)
    elif m1 < m2:
        return mediana(A[floor((len(A))/2):], B[:floor((len(B))/2)])
    else:
        return mediana(A[:floor((len(A))/2)], B[floor((len(B))/2):])

casos = int(input("Ingrese el numero de casos: "))
sol = []
sol.append(casos)
for i in range(casos):
    a = []
    b = []  
    n = int(input("Ingrese el tamano de los arreglos: "))
    print("Para el primer arreglo \n")
    for j in range(n):
        a.append(int(input("Ingrese numero: ")))
    print("Para el segundo arreglo \n")
    for j in range(n):
        b.append(int(input("Ingrese numero: ")))
    print("a: ",a)
    print("b: ",b)
    pallalla = int(input("Seguir?: "))
    sol.append(mediana(a,b))
for i in sol:
    print(i)