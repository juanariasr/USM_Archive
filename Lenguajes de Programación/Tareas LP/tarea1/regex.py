import re

sub_cadena = re.search(r"ch", "conchetumadre por la rechucha") #la r significa que el string es regular y lo que esta en comillas es lo que se buscara

print(".search ->", sub_cadena)

print(".group ->", sub_cadena.group())

a = re.search(r"\d\d\d", "wena589pete57")

print(".search numeros consecutivos ->", a)

ex = re.compile("\d\d\d\d")

b = ex.search("curso de4927 python").group()
c = ex.search("juan ar4859ias").group()
d = ex.search("sape6283sape").group()
e = ex.search("sos662sos4")

print("compile ->", b,c,d)

if e is None:
    print("Esta wea no existe wn")
else:
    print("Esta wea si existe wn")

f = re.sub(r"\d", "|", "234sapesaurio234")

print(".sub ->",f)

g = re.sub(r"\d", "|", "234sapesaurio234", 2) #reemplaza los primeros 2 caracteres

print(g)

chain = "Uno<4>Two<5>Tres<7>Four"

h = re.split(r"<\d>", chain)

print(".split ->",h)

new_chain = "".join(h)

print("join ->", new_chain)

cadena = "1111110000"




res = "\(>\d\)"

a = re.search(r"(0|[1-9]",cadena)
print("search: ",a)
if a is None:
    print("No hay parentesis")
else:
    b = a.group()

    str1 = cadena[:a.span()[0]]
    str2 = cadena[a.span()[1]:]

    str3 = str1 + str2


    print("str1: ", str1)
    print("str2: ", str2)
    print("str3: ", str3)
    print("a: ", a.span())
    print("b: ", b)

