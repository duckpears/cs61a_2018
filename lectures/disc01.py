from math import *



'''
1.1
'''

def wears_jacket(temp, raining):
	return temp < 60 or raining
	
	
'''
1.2
'''

def handle_overflow(s1, s2):
	if s1 <= 30 and s2 <= 30:
		print("No overflow")
	elif s2 > 30 and s1 < 30:
		print("Move to Section 1:" + str(30 - s1))
	elif s1 > 30 and s2 < 30:
		print("Move to Section 2:" + str(30 - s2))
	else:
		print("No space left in either section")
		
'''
1.4
'''

def is_prime(n):
	if n == 1:
		return False
	k = 2
	while k < sqrt(n):
		if n % k == 0:
			return False
		k += 1
	return True		
		
		
'''
2.1
'''

def keep_ints(cond, n):
	k = 1
	while k <= n:
		if cond(k):
			print(k)
		k += 1

def is_even(x):
	''' 
	Even numbers have remainder 0 when divided by 2 
	'''
	return x % 2 == 0

'''
2.3
'''

def keep_ints2(n):
	def judge_cond(cond):
		k = 1
		while k <= n:
			if cond(k):
				print(k)
			k += 1
	return judge_cond
	
def is_even(x):
	''' 
	Even numbers have remainder 0 when divided by 2 
	'''
	return x % 2 == 0
	

	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
		
		
		
		
		
		
		
		
		
		