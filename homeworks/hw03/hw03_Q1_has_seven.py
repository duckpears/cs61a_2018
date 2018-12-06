def has_seven(n):
	'''
	Returns True if at least one of the digits of n is a 7, False otherwise.
	'''
	others_but_last, last = n // 10, n % 10
	if last == 7:
		return True
	elif n < 10:
		return False
	else:
		return has_seven(others_but_last)	