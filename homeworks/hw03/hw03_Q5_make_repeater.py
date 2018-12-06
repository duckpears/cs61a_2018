square = lambda x: x * x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def make_repeater(f, n):
	'''
	Return the function that computes the nth application of f.
	'''
	def g(x):
		k = 1
		if n == 0:
			return x
		else:
			while k < n:
				x = f(x)
				k += 1
			return f(x)					
	return g
