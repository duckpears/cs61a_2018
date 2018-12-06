def has_seven(k):
	'''
	Returns True if at least one of the digits of k is a 7, False otherwise.
	'''
	if k % 10 == 7:
		return True
	elif  k < 10:
		return False
	else:
		return has_seven(k // 10)


def pingpong(n):
	'''
	Return the nth element of the ping-pong sequence.
	'''
	def pingpong_next(k, p, up):
		if k == n:
			return p
		elif up:
			return pingpong_switch(k + 1, p + 1, up)
		else:
			return pingpong_switch(k + 1, p - 1, up)
			
	def pingpong_switch(k, p, up):
		if k % 7 == 0 or has_seven(k):
			return pingpong_next(k, p, not up)
		else:
			return pingpong_next(k, p, up)
			
	return pingpong_next(1, 1, True)