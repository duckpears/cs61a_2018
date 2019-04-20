'''
Q1. GCD
'''

def gcd(a, b):
	'''
	Returns the greatest common divisor of a and b.
	Should be implemented using recursion.
	Using Euclid's algorithm:
	1. the smaller value if it evenly divides the larger value, or
	2. the greatest common divisor of the smaller value and the remainder of the larger value divided by the smaller value.
	'''
	if a == b:
		return a
	elif a < b:
		return gcd(b, a)
	elif a % b == 0:
		return b
	else:
		return gcd(b, a % b)
		

'''
Q2. Hailstone
'''

def hailstone(n):
	'''
	Print out the hailstone sequence starting at n, and return the
	number of elements in the sequence.
	'''
	print(n)
	if n == 1:
		return 1
	elif n % 2 == 0:
		return 1 + hailstone(n // 2)
	else:
		return 1 + hailstone(n * 3 + 1)
		
		
'''
Q4. I heard you liked functions
'''

def cycle(f1, f2, f3):
	'''
	Returns a function that is itself a higher-order function.
	'''
	def cycle_n(n):
		def cycle_x(x):
			i = 0
			while i < n:
				if i % 3 == 0:
					x = f1(x)
				elif i % 3 == 1:
					x = f2(x)
				else:
					x = f3(x)
				i += 1
			return x
		return cycle_x
	return cycle_n
	
	
'''
Q5. Palindrome
'''

def is_palindrome(n):
	x, y = n, 0
	f = lambda: y * 10 + x % 10 
	while x > 0:
		x, y = x // 10 , f()
	return y == n
	
	
'''
Q7. Find the Bug
'''

def skip_mul(n):
	'''
	Return the product of n * (n - 2) * (n - 4) * ...
	'''
	if n <= 2 and n > 0:
		return n
	else:
		return n * skip_mul(n - 2)
		
		
'''
Q8. Is Prime
'''

def is_prime(n):
	'''
	Returns True if n is a prime number and False otherwise.
	'''
	def is_prime_helper(i):
		if i > (n ** 0.5):
			return True
		elif n % i == 0:
			return False
		return is_prime_helper(i + 1)
	return is_prime_helper(2)


'''
Q9. Interleaved Sum
'''

def interleaved_sum(n, odd_term, even_term):
	'''
	Return the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up to n
	'''
	def interleaved_helper(term0, term1, k):
		if k == n:
			return term0(k)
		else:
			return term0(k) + interleaved_helper(term1, term0, k + 1)
	return interleaved_helper(odd_term, even_term, 1) 
	
	
'''
Q10. Ten-pairs
'''

def ten_pairs(n):
	'''
	Return the number of ten-pairs within positive integer n.
	'''
	if n < 10:
		return 0
	else:
		return ten_pairs(n // 10) + count_digit(n // 10, 10 - n % 10)
		
def count_digit(n, digit):
	'''
	Return how many times digit appears in n.
	'''
	if n == 0:
		return 0
	else:
		if n % 10 == digit:
			return count_digit(n // 10, digit) + 1
		else:
			return count_digit(n // 10, digit)
			

			





	
	
	
	
	
	
	
	
	
	
	
	
	
	