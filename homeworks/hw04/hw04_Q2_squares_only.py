from math import *

def squares(s):
	'''
	Returns a new list containing square roots of the elements of the
	original list that are perfect squares.
	'''
	return [round(sqrt(x)) for x in s if sqrt(x) == round(sqrt(x))]		
		