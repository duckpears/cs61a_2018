def towers_of_hanoi(n, start, end):
	'''
	Pirnt the moves required to solve the towers of hanoi game, starting
	with n disks on the start pole and finishing on the end pole.
	The game is assumed to have 3 poles.
	'''
	assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
	if n == 1:
		print("Move the top disk from rod", start, "to rod", end)
	else:
		next = 6 - start - end
		towers_of_hanoi(n - 1, start, next)
		towers_of_hanoi(1, start, end)
		towers_of_hanoi(n - 1, next, end)