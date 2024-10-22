%Hecho base de recursion de la regla sum, cuando la lista esta vacia y el valor inicial de la suma es 0
sum([],0).
/*Regla sum
Usando recursion, recorre la lista hasta que no queda ningun valor, y va sumando los valores
Le asigna a S el valor de la suma*/
sum([H|T],S) :-
    sum(T, Sc),
    S is Sc + H.

/*Regla prom
Haciendo uso de la regla sus y la regla length para obtener el largo de una lista, encuentra el promedio de los valores de la lista
Le asigna ese valor a P*/
prom(L, P) :-
    sum(L, S),
    length(L, X),
    P is S/X.

/*Regla mediana cuando se tiene una lista de largo par
Haciendo uso de la regla length obtiene la posicion de la mediana y se le asigna a la variable Y, posteriormente usando
la regla nth0 se obtiene el valor de la mediana y se le asigna a la variable M*/
mediana(L, M) :-
    length(L, X),
    mod(X,2) =:= 0,
    Y is X/2,
    msort(L, Sorted),
    nth0(Y, Sorted, Ma),
    Z is Y-1,
    nth0(Z,Sorted,Mb),
    M is (Ma+Mb)/2.

/*Regla mediana cuando se tiene una lista de largo impar
Haciendo uso de la regla length obtiene la posicion de la mediana y se le asigna a la variable Y, posteriormente usando
la regla nth0 se obtiene el valor de la mediana y se le asigna a la variable M*/
mediana(L, M) :-
    length(L, X),
    Y is floor(X/2),
    msort(L, Sorted),
    nth0(Y, Sorted, M).

%Hecho base de recursion de la regla bondad, donde la lista que se esta recorriendo esta vacia
bondad([],[]).

/*Regla bondad
Usando recursion, se usa las reglas prom y mediana previamente definidas para comparar si el promedio es mayor a la mediana
en caso de serlo, se agrega un string 'true' a una lista*/
bondad([H|T],['true'|Ls]) :-
    prom(H, P),
    mediana(H, M),
    P > M,
    bondad(T, Ls).
    
/*Regla bondad
Usando recursion, es el caso contrario a la regla definida arriba, o sea, el promedio es menor o igual a la mediana
se agrega un string 'false' a la misma lista de arriba*/
bondad([_|T],['false'|Ls]) :-
    bondad(T,Ls).