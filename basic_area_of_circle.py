#testing a basic function that calculates the area of a circle
from math import pi

def area_of_circle(r):
	if type(r) not in [float,int]:
		raise TypeError('the radius must be of int or float and a non-negative real_number')
	if r < 0:
		raise ValueError('the radius cannot be negative')
	'''assuming this function takes calculates all the available areas of all circles'''
	return pi*(r**2)

#check the accompanying file for its unit_tests
