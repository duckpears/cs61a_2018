from math import *

def divisors(n):
	'''
	Return divisors of n, which are positive integers less than n that divide 
	evenly into n.
	'''
	return [1] + [x for x in [2, n] if n % x == 0]
	
def width_of_rectangle(area, height):
	assert area % height == 0
	return area // height
	
def perimeter_of_rectangle(width, height):
	return 2 * width + 2 * height
	
def minimum_perimeter_of_rectangle(area):
	heights = divisors(area)
	perimeters = [perimeter_of_rectangle(width_of_rectangle(area, height), height) for height in heights]
	return min(perimeters)
	