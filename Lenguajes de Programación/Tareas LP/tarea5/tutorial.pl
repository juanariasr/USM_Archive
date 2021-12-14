%gtrace, comando para un debbuger mejor que trace

loves(romeo, juliet).

%si el valor de la derecha es verdadero el valor de lo de la izquierda sera verdadero tambien
loves(juliet, romeo) :- loves(romeo,juliet).

%las funciones parten con minuscula, las variables con mayuscula

%estos son los HECHOS   
waifu(nagatoro).
waifu(haruhi).
waifu(asahina).
waifu(komi).

girls(anna).
girls(ahsoka).
girls(leia).

tanlines(nagatoro).
/*Ahora vamos a las reglas, las reglas se usan para cuando uno quiere que un hecho dependa de otros hechos
para esto debemos usar un ':-' que equivale a un if
la coma funciona como un and con los ifs*/

bestgirl(nagatoro) :-
    waifu(nagatoro),
    tanlines(nagatoro).

es_nagatoro_bestgirl :- bestgirl(nagatoro),
    write('Ella si es tu best girl papu').

parents(haruhi, nagatoro).
parents(haruhi, asahina).
parents(haruhi, ahsoka).

%en el minuto 17.50 hay un ejemplo de como hacer preguntas con variables 'anidadas'

parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).
 
parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).
 
parent(bob, carl).
parent(bob, charlie).

get_grandchild :-
    parent(albert, X),
    parent(X, Y),
    write('Alberts grandchild is '),
    write(Y), nl.

get_grandparent :-
    parent(X, carl),
    parent(X, charlie),
    format('~w ~s grandparent ~n', [X, 'is the']). %~w es para variable ~s es para string ~n es para newline

blushes(X) :- human(X).
human(derek).

stabs(haruhi, nagatoro, sword).
hates(gamo, X) :- stabs(X, nagatoro, sword).

%human(_) checkea si existe el predicado human
/*En Prolog realmente no hay ifs, pero se puede rodear este problema explicitando diferentes comportamientos para diferentes entradas
de la siguiente manera*/

what_grade(5) :-
    write('go to kindergarten you fucking weeb').

what_grade(6) :-
    write('fuck off and go to 1st grade dipshit').

what_grade(Other) :- %notese que Other empieza con mayuscula ya que es una variable
    Grade is Other - 5, %el is funciona como un igual al definir variables
    format('Go to hell number ~w', [Grade]).


%ESTRUCTURAS    
has(albert, olvie). %albert tiene una oliva, pero que chucha es una oliva? un perro, una fruta, un auto?

owns(albert, pet(cat, olive)). %albert owns a pet thats a car named olive

customer(tom, smith, 20.55).
customer(sally, smith, 120.55). %con customer(sally,_,Bal). podemos buscar el saldo de sally y GUARDARLO en la variable Bal. No nos importa el apellido de sally

get_cust_bal(FName, LName) :- customer(FName, LName, Bal),
  write(FName), tab(1),
  format('~w owes us $~2f ~n', [LName, Bal]). %2f es un flotante con 2 decimales

  %minuto 30 hay un ejemplo delineas horizontales y verticales


%como comparar valores en prolog
/*var = var = 'var' 
para preguntar si algo no es igual se usa \+ (nagatoro = haruhi)
para comparar numeros se usa >= y =< 
W = alice retorna W = alice, lo que significa que le podemos asignar a W el valor de alice, pero no necesariamente W es igual a alice
rich(money, X) = rich(Y, sos). retorna X = sos e Y = money*/

warm_blooded(penguin).
warm_blooded(human).
 
produce_milk(penguin).
produce_milk(human).
 
have_feathers(penguin).
have_hair(human).
 
mammal(X) :-
  warm_blooded(X),
  produce_milk(X),
  have_hair(X).

%TRACE SE USA PARA DEBBUGEAR EN PROLOG, para apagralo se usa notrace

%RECURSION
related(X, Y) :-
    parent(X, Y). %esto no funciona con related(albert, carl) siendo albert el abuelo de carl

related(X, Y) :-
    parent(X, Z),
    related(Z , Y).

%X is 2 + 2 devuelve X = 4
% =:= se usa para verificar igualdad entre expresiones, para desigualdad es =\=
%or es ; ej: 5 > 10 ; 10 < 100
%mod() es modulo
double_digit(X, Y) :-
    Y is X*2.
%random(limite_inferior, limite_superior, variable) para un numero aleatorio dentro del rango
%between(limite_inferior, limite_superior, variable) para todos los numeros dentro del rango
%aumentar en uno el valor se hace con succ(2,X) X = 3
%abs, max, min, round, truncate, floor, ceiling, las potencias son como en python

is_even(X) :-
    Y is X//2,X =:= Y * 2.

%loops con recursion
count_to_10(10) :- write(10), nl.
 
count_to_10(X) :-
  write(X),nl,
  Y is X + 1,
  count_to_10(Y).

count_down(Low, High) :-
    % Assigns values between Low and High to Y
    between(Low, High, Y),
    % Assigns the difference to Z
    Z is High - Y,
    write(Z),nl,
    % Continue looping until Y = 10
    Y = 10.

%LISTAS
%constructor de listas, o sea appendiar pero en la primera posicion
% wr, ite([albert|[alicebob]]), nl.
% length([1,2,3], X).
% [H|T] = [a,b,c]. H seria el car y T seria el cdr
%[X1, X2, X3, X4|T] = [a,b,c,d]. esto te deja sacar los primero 4 elementos de una lista y el resto lo mete en la cola T, tambien se pueden usar variables anonimas
% [_, _, [X|Y], _, Z|T] = [a, b, [c, d, e], f, g, h]. valores de listas dentro de listas
%member(a, List1). checkea si a esta en List1
% member(X, [a, b, c, d]). Nos da TODOS los elementos de la lista, uno por uno
% append([1,2,3], [4,5,6], X). a diferencia de scheme el append ahora si crea una nueva lista y se la asigna a X

write_list([]).
 
write_list([Head|Tail]) :-
  write(Head), nl,
  write_list(Tail).
% write_list([1,2,3,4,5]). recorre la lista como en scheme y podemos hacer opeacions sobre el contenido

%clase LP
tercero(L,T) :-
    append([_,_,T],_,L).

sublistasiguales(L) :- 
    append(L1,L1,L).

todos_iguales([_]). %caso base de recursion es cuando la variable tiene 1 elemento
todos_iguales([H1,H2|T]) :- %se lograria el mismo efecto defiendola como todos_iguales([H,H|T]) porque la funcion ya hace la comparacion viendo si el elemento primero y segundo son el mismo, por lo que la linea 183 seria innecesaria
    H1 = H2,
    todos_iguales([H2|T]).

separa([],[],[]).
separa([H|T], [H|TP],N) :- %el formato real es LISTA, POSITIVOS, NEGATIVOS
    H > 0,
    separa(T, TP, N).
separa([H|T], P,[H|TN]) :- %el formato real es LISTA, POSITIVOS, NEGATIVOS
    H < 0,
    separa(T, P, TN).

alfinal(L,N,L1) :-
    append(L,[N],L1).