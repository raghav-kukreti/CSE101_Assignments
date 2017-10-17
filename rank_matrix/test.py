"""
	Name 		  : Raghav Dev Kukreti
	Roll No 	  : 2017082
	Section-Group : B1

"""
import unittest

from main import *
from copy import *

a1 =[[1,2,3], [4,5,6], [7,8,9]]
a2 =[[3,25,1], [44,-10,0], [0,1,-1]]
a3 =[[0,0,0], [0,5,0], [0,0,0]]
a4 =[[1,2,3], [0,0,0], [7,8,9]]
a5 =[[-1,-2,-3], [4,5,6], [-7,-8,-9]]
class testpoint(unittest.TestCase):
	def test_swap_rows(self):
		self.assertEqual(swap_rows(deepcopy(a1), 0, 1), [[4,5,6],[1,2,3],[7,8,9]])
		self.assertEqual(swap_rows(deepcopy(a2), 1, 2), [[3,25,1],[0,1,-1],[44,-10,0]])
		self.assertEqual(swap_rows(deepcopy(a3), 0, 2), [[0,0,0], [0,5,0], [0,0,0]])
		self.assertEqual(swap_rows(deepcopy(a4), 1, 1), [[1,2,3], [0,0,0], [7,8,9]])
		self.assertEqual(swap_rows(deepcopy(a5), 1, 1), [[-1,-2,-3], [4,5,6], [-7,-8,-9]])

	def test_row_transform(self):
		self.assertEqual(row_transform(deepcopy(a1), 2, 1,2), [[1, 2, 3], [4, 5, 6], [15, 18, 21]])
		self.assertEqual(row_transform(deepcopy(a2), 2, 0,1), [[3, 25, 1], [50, 40, 2], [0, 1, -1]])
		self.assertEqual(row_transform(deepcopy(a3), 69, 0,2), [[0, 0, 0], [0, 5, 0], [0, 0, 0]])
		self.assertEqual(row_transform(deepcopy(a4), 0, 1,1), [[1, 2, 3], [0, 0, 0], [7, 8, 9]])
		self.assertEqual(row_transform(deepcopy(a5), 1, 1,2), [[-1, -2, -3], [4, 5, 6], [-3, -3, -3]])

	def test_rank(self):
		self.assertEqual(find_rank(deepcopy(a1)), 2)
		self.assertEqual(find_rank(deepcopy(a2)), 3)
		self.assertEqual(find_rank(deepcopy(a3)), 1)
		self.assertEqual(find_rank(deepcopy(a4)), 2)
		self.assertEqual(find_rank(deepcopy(a5)), 2)

if __name__=='__main__':
	unittest.main()
