def count_change(amount):
	'''
	Return the number of ways to make change for amount
	'''
	def count_partitions(n, m):
		if n < m:
			return 0
		elif n == m:
			return 1
		else:
			with_m = count_partitions(n-m, m)
			without_m = count_partitions(n, 2 * m)
			return with_m + without_m
	return count_partitions(amount, 1)
	
