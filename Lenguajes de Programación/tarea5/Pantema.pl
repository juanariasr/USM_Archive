%hecho numero(0)
numero(0).

%regla que verfica que la entrada sea una entrada valida
numero(X) :-
    is_of_type(integer, X);
    is_of_type(float,X).



%reglas para las operaciones 
%el formato de los parametros es (operando, numero/operacion, numero/operacion, R (resultado))
%todas estas reglas realizan la operacion segun sea el operando
operacion("+", A, C, R) :-
    R is A + C.
operacion("-", A, C, R) :-
    R is A - C.
operacion("*", A, C, R) :-
    R is A * C.
operacion("/", A, C, R) :-
    R is A / C.
operacion("mod", A, C, R) :-
    R is mod(A,C).
operacion("^", A, C, R) :-
    R is A**C.

%caso base donde tanto A como C son numeros y B es el operando
matematica([A,B,C],RES) :-
    numero(A),
    numero(C),
    operacion(B,A,C,R),
    RES is R.

%regla matematica cuando hay dos operaciones
matematica([A,B,C], RES) :-
    not(numero(A)),
    not(numero(C)),
    matematica(A,Rea),
    matematica(C,Rec),
    operacion(B,Rea,Rec,R),
    RES is R.

%regla matematica cuando C es un numero pero A es una operacion
matematica([A,B,C], RES) :-
    not(numero(A)),
    numero(C),
    matematica(A,Re),
    operacion(B,Re,C,R),
    RES is R.

%regla matematica cuando A es un numero pero C es una operacion
matematica([A,B,C], RES) :-
    not(numero(C)),
    numero(A),
    matematica(C,Re),
    operacion(B,A,Re,R),
    RES is R.