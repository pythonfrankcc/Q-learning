#importing necessary dependencies and the file under test
import unittest
from employee import Employee
class testEmployee(unittest.Testcase):

 	def test_email(self):
 		employee_1 = Employee('Francis','Macharia',20000)
 		employee_2 = Employee('Dickens','Mugendi',80000)

 		self.assertEqual(employee_1.email,'Francis.Macharia@gmail.com')
 		self.assertEqual(employee_2.email,'Dickens.Mugendi@gmail.com')
 		#changing the first names of the employees

 		employee_1.first = Jonathan
 		employee_2.first = Solomon
 		#test now to see if the changes have been reflected

 		self.assertEqual(employee_1.email,'Jonathan.Macharia@gmial.com')
 		self.assertEqual(employee_2.email,'Solomon.Mugendi@gmail.com')
 	def test_fullname(self):
 		employee_1 = Employee('Francis','Macharia',20000)
 		employee_2 = Employee('Dickens','Mugendi',80000)

 		self.assertEqual(employee_1.email,'Francis.Macharia@gmail.com')
 		self.assertEqual(employee_2.email,'Dickens.Mugendi@gmail.com')
 		#changing the first names of the employees

 		employee_1.first = Jonathan
 		employee_2.first = Solomon
 		#test now to see if the changes have been reflected

 		self.assertEqual(employee_1.email,'Jonathan.Macharia@gmial.com')
 		self.assertEqual(employee_2.email,'Solomon.Mugendi@gmail.com')
 	def test_raise(self):
 		employee_1 = Employee('Francis','Macharia',20000)
 		employee_2 = Employee('Dickens','Mugendi',80000)

 		employee_1.appy_raise()
 		employee_2.apply_raise()


 		self.assertEqual(employee_1.pay,21000)
 		self.assertEqual(employee_2.pay,84000)

#to run this on your cmd 
if __name__ == '__main__':
	unittest.main()
 		

