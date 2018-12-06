(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  （car   (cdr  s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
    ((< x 0) -1)
    ((> x 0) 1)
    (else 0))
)

(define (square x) (* x x))

(define (pow b n)
  (if (= 0 n)
      1
      (if (even? 0)
          (square (pow b (quotient n 2)))
          (* b (pow b (- n 1)))))
)

(define (ordered? s)
  (cond
    ((null? s) #t)
    ((null? (cdr s)) #t)
    ((<= (car s) (car (cdr s))) (ordered? (cdr s)))
    (else #f))
)

(define (nodots s)
  (cond
    ((null? s) s)
    ((and (pair? (car s)) (number? (cdr s))) (cons (nodots (car s)) (cons (cdr s) nil)))
    ((number? (cdr s)) (cons (car s) (cons (cdr s) nil)))
    ((pair? (car s)) (cons (nodots (car s)) (nodots (cdr s))))
    (else (cons (car s) (nodots (cdr s)))
)))

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          'YOUR-CODE-HERE
          (else nil) ; replace this line
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond
      ((empty? s) (list v))
      ((= (car s) v) s)
      ((< (car s) v) (cons (car s) (add (cdr s) v)))
      ((> (car s) v) (cons v s))
))
          
          
          
          
(define (intersect s t)
    (cond 
      ((or (empty? s) (empty? t)) nil)
      ((= (car s) (car t))
        (cons (car s) (intersect (cdr s) (cdr t))))
      ((< (car s) (car t))
        (intersect (cdr s) t))
      (else
        (intersect s (cdr t)))
))
          

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond 
      ((empty? s) t)
      ((empty? t) s)
      ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
      ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))    
      (else (cons (car t) (union s (cdr t))))
))