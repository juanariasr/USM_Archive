#lang scheme

;;(izquierda nodo)
;;Funcion que devuelve el hijo izquierdo de un nodo no nulo
;;Si el nodo es nulo retorna una lista vacia, de lo contrario retorna el hijo izquierdo del nodo pasado como parametro
(define (izquierda nodo)
  (if (null? nodo)
      '()
      (cadr nodo)
      )
  )
;;(derecha nodo)
;;Funcion que devuelve el hijo derecho de un nodo no nulo
;;Si el nodo es nulo retorna una lista vacia, de lo contrario retorna el hijo derecho del nodo pasado como parametro
(define (derecha nodo)
  (if (null? nodo)
      '()
      (caddr nodo)
      )
  )
;;(visitar nodo)
;;Funcion que devuelve el valor de un nodo
;;retorna una lista vacia si el nodo es nulo, de lo contrario retona su valor
(define (visitar nodo)
  (if (null? nodo)
      '()
       (car nodo)
      )
  )

;;(pre-izq arbol)
;;Hace un recorrido en preorden del arbol izquierdo de un arbol no nulo 
;;Si el nodo es nulo retorna una lista vacia, en el caso contrario retorna una lista con los valores de los nodos del arbol izquierdo
(define (pre-izq arbol)
  (let pre([arbol (cadr arbol)])
    (if (null? arbol)
        '()
        (append
         (list (visitar arbol))
         (pre(izquierda arbol))
         (pre(derecha arbol))   
         )
        )
    )
  )
;;(pre-der arbol)
;;Hace un recorrido en preorden del arbol derecho de un arbol no nulo 
;;Si el nodo es nulo retorna una lista vacia, en el caso contrario retorna una lista con los valores de los nodos del arbol derecho
(define (pre-der arbol)
  (let pre([arbol (caddr arbol)])
    (if (null? arbol)
        '()
        (append
         (list(visitar arbol))
         (pre(izquierda arbol))
         (pre(derecha arbol))
         )
        )
    )
  )

(define (vida h arbol)
  (if (null? arbol)
      '()
      (append
       (list(car arbol))
       (let rec1 ([arbol arbol] [h h] [izq (pre-izq arbol)][der (pre-der arbol)])
         (append
         (cond
           [(or (equal? (caadr arbol) h)(equal? (caaddr arbol) h)) '()]
           [(not(equal? (member h izq) #f)) (rec1 (cadr arbol) h (pre-izq (cadr arbol))(pre-der (cadr arbol)))(list(caadr arbol))]
           [(not(equal? (member h der) #f)) (rec1 (caddr arbol) h (pre-izq (caddr arbol))(pre-der (caddr arbol)))(list(caaddr arbol))]
           [else '()]
           )
         )
         )
       )
      )
  )
            
(vida 4 '(5 (3 (2 () ()) (4 () ())) (8 (6 () ()) ())))