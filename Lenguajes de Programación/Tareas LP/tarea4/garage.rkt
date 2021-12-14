#lang scheme



;(and (null? (cadr arbol)) (null? (caddr arbol))) ;hijo
;(or (memv 4 (cadr arbol)) (memv 4 (caddr arbol))) ;si en los hijos esta la wea
(append (list 3)
        (let haruhi ([a 2])
          (if (= 3 a)
            (list 4)
            (haruhi (+ 1 a)) 
            )
          )
        (let nagatoro([b 3])
          (if ( = 4 b)
              (list 69)
              (nagatoro (+ 1 b))
              )
          )
        )


(define (encontrar grafo n)
  (if (null? grafo)
      '()
      (cond
        [(equal? (caar grafo) n)(car grafo)]
        [else (encontrar (cdr grafo) n)]
        )
      )
  )

(define (eliminar lts n)
   (if (null? lts)
       '()
       (if (not(equal? (car lts) n))
           (append
            (list (car lts))
            (eliminar (cdr lts) n)
            )
           (eliminar (cdr lts) n)
           )
       )
  )

(define (encontrar_veci grafo nodo elegidos h)
  (if (null? grafo)
      '()
      (let rec1 ([grafo grafo] [vecinos (cadr (encontrar grafo h))] [elegidos elegidos][template elegidos])
        (if (null? vecinos)
            (if (equal? elegidos template)
                '()
                elegidos)
            (cond  
              [(and (not(equal? (member (caar grafo) vecinos) #f))(equal? (member (caar grafo) elegidos) #f)) (rec1 (cdr grafo) (eliminar vecinos (caar grafo)) (append elegidos (list (caar grafo))) template)]
              [(not(equal? (member (caar grafo) elegidos) #f)) (rec1 (cdr grafo) (eliminar vecinos (caar grafo)) elegidos template)]
              [else (rec1 (cdr grafo) vecinos elegidos template)]
              )
            )
        )
      )
  )

(define (contagio grafo n d)
  (if (null? grafo)
      '()
      (let rec1 ([grafo grafo] [n n][d d][contador 0] [elegidos (append (list (car (encontrar grafo n)))(encontrar_veci grafo '() '() n))])
        (if (or (equal? (length elegidos) (length grafo)) (equal? contador d))
            elegidos
            (rec1 grafo (car elegidos) d (+ 1 contador) (append elegidos (encontrar_veci grafo '() elegidos (car elegidos)))) 
            )
        )  
      )
  )
  


(contagio '((2 (1 3 4)) (1 (2)) (3 (2)) (4 (2))) 2 1) 

