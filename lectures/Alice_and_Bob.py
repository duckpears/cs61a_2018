def is_even(n):
	if n == 0:
		return True
	elif (n-1) == 0:
		return False
	else:
		return is_even(n-2)
			
def play_Alice(n):
	if n == 0:
		print("Bob wins")
	else:
		return play_Bob(n-1)
		
def play_Bob(n):
	if n == 0:
		print("Alice wins")
	elif is_even(n):
		return play_Alice(n-2)
	else:
		return play_Alice(n-1)