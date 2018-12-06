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
	
def compose1(f, g):
	'''
	Return a function h, such that h(x) = f(g(x)).
	'''
	def h(x):
		return f(g(x))
	return h
	
def make_repeater(f, n):
	return accumulate(compose1, lambda x: x, n, lambda k: f)	
	
	
	