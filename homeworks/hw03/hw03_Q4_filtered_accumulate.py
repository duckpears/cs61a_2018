odd = lambda x: x % 2 == 1

greater_than_5 = lambda x: x > 5

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

add = lambda x, y: x + y

mul =  lambda x, y: x * y

def accumulate(combiner, base, n, term):
	'''
	Retrun the result of combining the first n terms in a sequence and base.
	The terms to be combined are term(1), term(2), ..., term(n).
	combiner is a two-argument commutative function.
	'''
	total, k = base, 1
	while k <= n:
		total, k = combiner(total, term(k)), k + 1
	return total
	
	'''
	if n == 0:
		return base
	else:
		return combiner(term(n), accumulate(combiner, base, n - 1, term)
	'''

def filtered_accumulate(combiner, base, pred, n, term):
	'''
	Return the result of combining the terms in a sequence of N terms
	that satisfy the predicate pred. combiner is a two-argument function.
	The implementation uses accumulate.
	'''
	def combine_if(x, y):
		if pred(y):
			return combiner(x, y)
		else:
			return x							
	return accumulate(combine_if, base, n, term)	
		
		
		
		
		
		
		
		
		
	