def cascade(n):
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n // 10)
		'''Repeat the statement above until a None is returned, because there is no return statement
		'''
		print(n)