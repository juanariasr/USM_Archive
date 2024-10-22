%hechos del enunciado
ancestro(p2,p1).
ancestro(p3,p1).
ancestro(p4,p1).
ancestro(p5,p1).

ancestro(p2,p10).
ancestro(p3,p10).
ancestro(p4,p10).
ancestro(p6,p10).
ancestro(p7,p10).

ancestro(p5,p2).
ancestro(p6,p2).

ancestro(p5,p3).
ancestro(p9,p3).

ancestro(p6,p4).

ancestro(p8,p5).

ancestro(p7,p6).
ancestro(p9,p6).

ancestro(p8,p7).

ancestro(p1,p9).

%regla para disminuir en uno el valor de una variable
notplus(X,X1) :-
    X1 is X-1.

%regla para inicializar una lista que ayudara a recordar los nodos visitados y una variable que sera el contador de pasos que servira para cuando no se encuentre camino
ancestrosidad(A,B,L) :-
    ancestrosidad(A,B,L,[],0).

%caso base donde encuentra una conexion directa
ancestrosidad(A,B,1,_,_) :-
    ancestro(A,B).

%caso para cuando no existe camino, donde le resta por ultima vez uno a la variable que contaba pasos y detiene el programa
ancestrosidad(A,_,L,V,H) :-
    L is H - 1,
    member(A,V), !.
%regla recursiva que va probando los hijos de A, almacenados en C
%si no hay una conexion directa pasa C como el padre hasta que se encuentre una conexion a B
%en ese momento empieza a sumar la cantidad de ancestros que tiene
%ademas le resta uno a la variable H y añade el nodo actual a la lista de visitiados V
ancestrosidad(A, B, L, V,H) :-
    ancestro(A, C),
    notplus(H,Hs),
    ancestrosidad(C, B, Ls, [A|V],Hs),
    L is Ls + 1.