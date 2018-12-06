def g(n):
	'''
	Return the value of G(n), computed recursively.
	'''
	if n <= 3:
		return n
	else:
		return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)
		
def g_iter(n):
	'''
	Return the value of G(n), computed iteratively.
	'''
	if n <= 3:
		return n
	a, b, c = 1, 2, 3
	while n > 3:
		a, b, c = b, c, c + 2 * b + 3 * a
		n -= 1
	return c