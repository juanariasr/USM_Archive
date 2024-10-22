#lang scheme

(define (append . item)
  (cond ((null? item) '())
  ((null? (car item)) (apply append (cdr item)))
  (else (cons (caar item)(apply append (cdar item) (cdr item))))))

(define (mazo list x)
  (cond [(null? list) #f]
        [(equal? (car list) x) #t]
        [else (mazo (cdr list)
                        x)]))

(mazo '(1 2 3 4 5) 1)
