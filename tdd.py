
import unittest
from solutiontest import operators 

class TestSolution(unittest.TestCase):
	def test_addition(self):
		op = operators()
		self.assertTrue(op.solution(10,20,"+") , 30)
	def test_subtraction(self):
		op = operators()
		self.assertTrue(op.solution(10,20,"-") , -10)
	def test_multiplication(self):
		op = operators()
		self.assertTrue(op.solution(10,20,"*") , 200)
	def test_division(self):
		op = operators() 
	 	self.assertTrue(op.solution(20,10,"/") , 2)

if __name__=="__main__":
	unittest.main()