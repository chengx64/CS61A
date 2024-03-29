; Q1
(define (vir-fib n)
    (cond 
        ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (vir-fib (- n 1)) (vir-fib (- n 2))))
    )
)

(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)

; Q2
; use list
(define with-list
    (list
        (list 'a 'b)
        'c
        'd
        (list 'e)
    )
)

; use quote
(define with-quote
    '((a b) c d (e))
)

; use cons
(define helpful-list
   (cons 'a (cons 'b nil)))

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))

(define with-cons
    (cons
        helpful-list
        another-helpful-list
    )
)


; Q3
; (define (list-concat a b)
;     (append a b)
; )

; (expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
; (expect (list-concat '(3) '(2 1 0)) (3 2 1 0))

;no-use append
(define (list-concat a b)
    (if (null? a)
        b
        (cons (car a) (list-concat (cdr a) b))
    )
)

(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))

; Q4
(define (map-fn fn lst)
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map-fn fn (cdr lst))))
)

(map-fn (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)

; Q5
(define (remove item lst)
    (filter (lambda (val) (not (= val item))) lst)
)

(expect (remove 3 nil) ())
(expect (remove 2 '(1 3 2)) (1 3))
(expect (remove 1 '(1 3 2)) (3 2))
(expect (remove 42 '(1 3 2)) (1 3 2))
(expect (remove 3 '(1 3 3 7)) (1 7))


; Q6
(define (duplicate lst)
    (cond 
        ((null? lst) nil)
        (else (list-concat (list (car lst) (car lst)) (duplicate (cdr lst))))
    )
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))
(expect (duplicate '(1 1)) (1 1 1 1))






