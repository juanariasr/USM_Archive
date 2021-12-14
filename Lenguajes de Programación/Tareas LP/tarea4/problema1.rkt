#lang scheme

(define (mazo cartas divisor)  
  (if (null? cartas)
      '()
      (if (integer? (/ (car cartas) divisor))
          (append
           (list (car cartas))
           (mazo (cdr cartas) divisor)
           )
          (mazo (cdr cartas) divisor)
          )
      )
  )

(mazo '(1 2 3 4 5) 3)
(mazo '(1 2 3 4 5) 2)