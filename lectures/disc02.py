'''
2.1
'''

def product(m, n):
	if n == 0:
		return 0
	else:
		return m + product(m, n - 1)
		
'''
2.2
'''

def countdown(n):
	if n:
		print(n)
		return countdown(n - 1)
	else:
		print("0")
		
'''
2.3
'''

def countup(n):
	if n <= 0:
		return
	countup(n - 1)
	print(n)
	
'''
2.4
'''

def sum_digits(n):
	if n < 10:
		return n
	else:
		rest_but_last, last = n // 10, n % 10
		return sum_digits(rest_but_last) + last
		
'''
3.1
'''

def count_stair_ways(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return count_stair_ways(n - 1) + count_stair_ways(n - 2)
		
'''
3.2
'''

def count_k(n, k):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif k == 0:
		return 0
	else:
		with_k = count_k(n - k, k)
		without_k = count_k(n, k - 1)
		return with_k + without_k
	
	
	
	
	
	
			
		
		
		
		
		
		
		
		














