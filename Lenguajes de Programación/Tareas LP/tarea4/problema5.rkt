#lang scheme

;;(encontrar grafo n)
;;encuentra el nodo con valor n en un grafo
;;retorna el nodo con valor n
(define (encontrar grafo n)
  (if (null? grafo)
      '()
      (cond
        [(equal? (caar grafo) n)(car grafo)]
        [else (encontrar (cdr grafo) n)]
        )
      )
  )

;;(eliminar lts n)
;;elimina el valor n de una lista
;;retorna la lista n sin el elemento de valor n
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

;;(encontrar_veci grafo nodo elegidos h)
;;encuentra los vecinos de un nodo y los añade a una lista elegidos si es que no estan previamente en la lista
;;retorna la lista elegidos si es diferente a la que se dio como parametro en la funcion rec1, de lo contrario retorna una lista vacia
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
