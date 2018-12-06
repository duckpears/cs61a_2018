identity = lambda k: k
square = lambda k: k*k
triple = lambda k: k*3
increment = lambda k: k+1

def product(n, term):
	'''
	Return the product of the first n terms in a sequence
	'''
	total, k = 1, 1
	while k <= n:
		total, k = term(k) * total, k + 1
	return total
	
def factorial(n):
	'''
	Return n factorial for n >= 0 by calling product
	'''
	if n == 0:
		return 1
	else:
		return product(n, identity)
		
	
		
		