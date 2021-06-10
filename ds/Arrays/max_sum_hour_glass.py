#! /usr/bin/env python3

"""
Given two integers N, M and a 2D matrix Mat of dimensions NxM, the task is to find the maximum sum of
an hourglass.
An hourglass is made of 7 cells in the following form.
    A B C
      D
    E F G
"""

class Solution:

	def __init__(self, cols, rows, array):

		self.cols = cols
		self.rows = rows
		self.array = array

	def is_present(self):

		if self.cols < 3 or self.rows < 3:
			print('Abandon')
			return -1
		
		matrix = self.array
		max_sum = 0
		print(len(matrix) -2)
		print(len(matrix[1]) -2)
		for i in range(0, len(matrix)-2):
			for j in range(0, len(matrix[i])-2):
				max_hour_sum = sum(matrix[i][j:j+3]) + matrix[i+1][j+1] + sum(matrix[i+2][j:j+3])
				if max_hour_sum > max_sum:
					max_sum = max_hour_sum
				else:
					continue

		return max_sum
	#			print('num: ', iteration, matrix[i], matrix[i][j:j+3])
	#			print('     ',' ', matrix[i+1], matrix[i+1][j+1])
	#			print('     ',' ', matrix[i+2], matrix[i+2][j:j+3])
		
if __name__ == "__main__":

	n = 6
	m = 6
	mat = [[0, 3, 8, 6, 1, 5], [7, 9, 1, 0, 0, 2], [2, 5, 7, 2, 3, 1], [0, 0, 4, 1, 7, 0], [1, 3, 6, 1, 2, 3], [5, 4, 2, 3, 6, 9]]
	mat_2 = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4]]
	mat_3 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
	hour_glass = Solution(n, m, mat_3)
	print(hour_glass.is_present())