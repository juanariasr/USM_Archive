#lang scheme

(define (transformacion funcion1 funcion2 numeros)
  (if (null? numeros)
      '()
      (if (> (funcion2(funcion1(car numeros))) (funcion1(funcion2(car numeros)))) 
          (append 
           (list (funcion2(funcion1 (car numeros))))
           (transformacion funcion1 funcion2 (cdr numeros))
           )
          (append 
           (list (funcion1(funcion2 (car numeros))))
           (transformacion funcion1 funcion2 (cdr numeros))
           )
          )
      )
  )

(transformacion (lambda (x) (+ 2 x)) (lambda (x) (/ x 2)) '(2 3 4))