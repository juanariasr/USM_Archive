#lang scheme

(define (zeta_simple i s)
  (if (equal? i 0)
      0
      (+ (expt(/ 1 i) s) (zeta_simple (- i 1) s) )
      )
  )

(define (zeta_cola i s)
    (let res ([i i] [s s] [resultado 0])
      (if (equal? i 0)
          resultado
          (res (- i 1) s (+ (expt(/ 1 i) s) resultado))
          )
      )
  )


(zeta_simple 3 2)
(zeta_cola 3 2)