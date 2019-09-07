import unittest
#importing the function for test
from basic_area_of_circle import area_of_circle
from math import pi
'''
#use a test function just to see if what you are doing is right
radii=[0,2,-3,True,'radius',2 + 5j]
message='area of circle with r = {radius} is {area}'
for r in radii:
	Area = area_of_circle(r)
	print(message.format(radius=r,area=Area))'''
#from the above test function we can already see an error in our function but lets comment out this and carry out a unittest using unittest module
#when running this on python best use >>python -m unittest (xxx)
#lets build our test class
class testCircleArea(unittest.TestCase):
	#each test method must begin with the word test
	def test_area(self):
		#test the computational soundness of the function
		self.assertAlmostEqual(area_of_circle(1),pi)
		self.assertAlmostEqual(area_of_circle(2.1),pi*2.1**2)
	#testing to see if the function  raises a value error when the input is a negative no
	def test_values(self):
		self.assertRaises(ValueError,area_of_circle,-2)
		#this spits out an error and you go back to your function and alter that
		#python has various other assert methods that one can do your tests in
	#making sure that the test spits out a type error when r is not a real no
	def test_types(self):
		self.assertRaises(TypeError,area_of_circle,3+5j)
		self.assertRaises(TypeError,area_of_circle,True)
		self.assertRaises(TypeError,area_of_circle,'radius')
		#then fix this on the function given
