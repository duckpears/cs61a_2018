def summation(n):
	k, total = 1, 0
	while k < n:
		k, total = k + 1, total + 1/k
	return total