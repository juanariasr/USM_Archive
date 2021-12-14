#lang scheme

;map
(define my-list '(1 2 3 4 5))
(map add1 my-list) ;map le hace algo a todos los elementos de la lista
(map number->string my-list)
(printf "\n")

; hay mas operaciones de listas en el documento

(filter even? my-list)
(sort my-list >)
(printf "\n")


;funciones anonimas
(define (add2 x) (+ x 2))
(map add2 '(1 2 3))
(printf "\n")

;lambda (λ = ctrl + \)
(lambda (x) (+ x 124))
(printf "\n")


(map (λ  (x) (+ x 124)) '(1 2 3))
(printf "\n")


(define foo (λ (x) x)) ;= (define (foo x) x)

(let ([f (λ (x) x)])
  (f 10))
(printf "\n")

;funcion recursiva
(printf "letrec")
 (letrec ([fact (λ (n)
                  (if (< n 2) 1
                      (* n (fact (sub1 n)))))])
(fact 10))
(printf "\n")

;funciones que crean funciones
(define (addn n)
  (λ (x)
    (+ x n)))

(define add10 (addn 10))
(add10 12)
(printf "\n")

(define (more-than n)
  (λ (m)
    (> m n)))
(filter (more-than 10) '(13 2 31 45 9 10))









