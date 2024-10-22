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


%caso base donde encuentra una conexion directa
ancestrosidad(A,B,1) :-
    ancestro(A,B).

%regla recursiva que va probando los hijos de A, almacenados en C
%si no hay una conexion directa pasa C como el padre hasta que se encuentre una conexion a B
%en ese momento empieza a sumar la cantidad de ancestros que tiene
ancestrosidad(A, B, L) :-
    ancestro(A, C),
    ancestrosidad(C, B, Ls),
    L is Ls + 1.