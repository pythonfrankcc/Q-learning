#using the setUp and tearDown method in tests so as to remove repetition
#importing necessary dependencies and the file under test
import unittest
from employee import Employee

class testEmployee(unittest.Testcase):

	def setUp(self):#runs its code before every single code
		self.self.employee_1 = Employee('Francis','Macharia',20000)#set them as intsance attributes so as to be accessible by all of the other tests
		self.self.employee_2 = Employee('Dickens','Mugendi',80000)
		

	def tearDown(Self):#runs its code after every single code
		pass

	def test_email(self):
		self.assertEqual(self.employee_1.email,'Francis.Macharia@gmail.com')
		self.assertEqual(self.employee_2.email,'Dickens.Mugendi@gmail.com')
		#changing the first names of the employees
		self.employee_1.first = Jonathan
		self.employee_2.first = Solomon
		#test now to see if the changes have been reflected
		self.assertEqual(self.employee_1.email,'Jonathan.Macharia@gmial.com')
		self.assertEqual(self.employee_2.email,'Solomon.Mugendi@gmail.com')


	def test_fullname(self):
		self.assertEqual(self.employee_1.email,'Francis.Macharia@gmail.com')
		self.assertEqual(self.employee_2.email,'Dickens.Mugendi@gmail.com')
		#changing the first names of the employees
		self.employee_1.first = Jonathan
		self.employee_2.first = Solomon
		#test now to see if the changes have been reflected
		self.assertEqual(self.employee_1.email,'Jonathan.Macharia@gmial.com')
		self.assertEqual(self.employee_2.email,'Solomon.Mugendi@gmail.com')

	def test_raise(self):
		self.employee_1.appy_raise()
		self.employee_2.apply_raise()

		self.assertEqual(self.employee_1.pay,21000)
		self.assertEqual(self.employee_2.pay,84000)
#to run this on your cmd 
if __name__ == '__main__':
	unittest.main()
#remember taht tests dont run in order,that is,  from top to down 
 		

