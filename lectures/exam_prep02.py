'''
1. Express Yourself
'''

def kbonacci(n, k):
	'''
	Return element N of a K-bonacci sequence.
	'''
	if n < k - 1:
		return 0
	elif n == k - 1:
		return 1
	else:
		total = 0
		i = n - k
		while i < n:
			total = total + kbonacci(i, k)
			i = i + 1
		return total
		

'''
2. Combine, Reverse, and Remove
'''

def combine(left, right):
	'''
	Return all of LEFT's digits followed by all of RIGHT's digits.
	'''
	factor = 1
	while factor <= right:
		factor = factor * 10
	return left * factor + right
	
def reverse(n):
	'''
	Return the digits of N in reverse.
	'''
	if n < 10:
		return n
	else:
		return combine(n % 10, reverse(n // 10))

def remove(n, digit):
	'''
	Return all digits of N that are not DIGIT, for DIGIT less than 10.
	'''
	removed = 0
	while n != 0:
		n, last = n // 10, n % 10
		if last != digit:
			removed = removed * 10 + last
	return reverse(removed)	
	
	
'''
3. You Complete Me
'''

square = lambda x: x * x

double = lambda x: 2 * x

def memory(x, f):
	'''
	Return a higher-order function that prints its memories.
	'''
	def g(h):
		print(f(x))
		return memory(x, h)
	return g
	
		
		
		
		
		
		