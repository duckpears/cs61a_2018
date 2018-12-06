def summation(n, term):
	'''
	Return the sum of the first n terms in the sequence defined by term.
	'''
	if n >= 2:
		return term(n) + summation(n - 1, term)
	else:
		return term(1)