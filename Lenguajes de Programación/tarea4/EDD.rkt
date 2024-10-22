#lang scheme

;pares supongo que son tuplas
(cons 1 2)
(car (cons 1 2))
(cdr (cons 1 2))
(printf "\n")

;listas
empty
(cons 2 empty)
(cons 1 (cons 2 (cons 3 empty)))

(define l (list 1 2 3 4 5 6))
l

(append (list 7 8 9) (list 10 11 12))
(cons (list 7 8 9) (list 10 11 12))

(car l)
(cdr l)
(car (cdr l))
(cadr l)
(cadddr l)

(first l)
(rest l)
(second l)
(fourth l)

(list 1 2 (+ 1 2))
(second '(define (inc x) (+ 1 x)))
(printf "\n")

;vectores
(define v (vector 1 2 3 4 5 6))
(vector-ref v 4)

(vector-set! v 2 "Nagatoro")
v

(define v2 #(1 2 3)) ;vector literal
(vector->list v2)
(list->vector '(1 2 3))