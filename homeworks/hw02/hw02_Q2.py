def make_adder(n):
	'''
	Return a function that takes an argument K and returns N + K
	'''
	return lambda k: n + k
	
	
def make_adder2(n):
	def inner(k):
		return n + k
	return inner