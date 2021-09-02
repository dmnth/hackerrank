# TODO:
# There are same patterns for forming i.e diagonals [%2, 5 %2]/ middle row and middle column [!%2, 5, !%2]
# dont require to check middle value, since it is always 5

# column 1 and 3 / row 1 and 3 also share common principles [%2, !%2, !%2]

#diagonal_one[0] == matrix_rows[0][0]
#diagonal_two[0] == matrix_rows[0][2]
#diagonal_one[1] == diagonal_two[1] == column_one[1] == matrix_rows[1][1]
#diagonal_one[2] == column[0][2] == matrix_rows[2][2]
#diagonal_two[2] == column[2][2] == matrix_rows[2][0]

#column_two[0] == matrix_rows[0][1]
#column_two[1] == matrix_rows[1][1] == 5
#column_two[2] == matrix_rows[2][1]

#column_one[0] == diagonal_one[0] == matrix_rows[0][0]
#column_one[1] == matrix_rows[1][0]
#column_one[2] == matrix_rows[2][0]

#column_three[0] == diagonal_two[0] == matrix_rows[0][2]
#column_three[1] == matrix_rows[1][2]
#Column_three[2] == matrix_rows[2][2]
 
# diagonal_one[2] == matrix_rows[2][2]
# diagonal_two[2] == matrix_rows[2][0]

class magickSquare:

	def __init__(self, matrix):
		self.matrix = matrix
		self.middle_value = self.matrix[1][1]
		#Diagonals
		self.diag_one = []
		self.diag_two = []
		#Rows
		self.row_one = self.matrix[0]
		self.row_two = self.matrix[1]
		self.row_three = self.matrix[2]
		#Columns...

	def get_diagonals(self):
		idx = 0
		for row in self.matrix:
			self.diag_one.append(row[idx])
			idx += 1

		for row in self.matrix:
			self.diag_two.append(row[idx-1])
			idx -= 1

	def check_middle_value(self):
		print("Middle value: ")
		if self.matrix[1][1] != 5:
			print(f"{self.matrix[1]} middle value must be equal 5")
		else:
			print(f"{self.matrix[1]} middle index equals five, ok")

	def check_diagonals(self):
		print("Diagonals: ")
		if sum(self.diag_one) != 15:
			print(f"diag_1: sum of {self.diag_one} is not 15")
		if sum(self.diag_two) != 15:
			print(f"diag_2: sum of {self.diag_two} is not 15")
		else:
			print(f"Both {self.diag_one} and {self.diag_two} are ok" )

	def check_row_one(self):
		print("Row one:")
		if sum(self.matrix[0]) != 15:
			print(f"{self.matrix[0]} must be fixed")
		else:
			print(f"{self.matrix[0]} is ok")

	def check_middle_row(self):
		print("Middle row:")
		if sum(self.matrix[1]) != 15:
			print(f"{self.matrix[1]} must be fixed")
		else:
			print(f"{self.matrix[1]} is ok")

	def check_row_three(self):
		print("Row three:")
		if sum(self.matrix[2]) != 15:
			print(f"{self.matrix[2]} must be fixed")
		else:
			print(f"{self.matrix[2]} is ok")


	def fix_middle_value(self):
		self.matrix[1][1] = 5
		
	def fix_diag_1(self):
		diff = 15 - sum(self.diag_one)
		if self.diag_one[0] % 2 != 0:
			self.diag_one[0] = self.diag_one[0] + diff

		if self.diag_one[2] % 2 != 0:
			self.diag_one[2] = self.diag_one[2] + diff

	def fix_diag_2(self):
		diff = 15 - sum(self.diag_one)
		if self.diag_one[0] % 2 != 0:
			self.diag_one[0] = self.diag_one[0] + diff

		if self.diag_one[2] % 2 != 0:
			self.diag_one[2] = self.diag_one[2] + diff

	def fix_row_one(self):
		diff = 15 - sum(self.row_one)
		print("Diff: ", diff)
		if self.row_one[0] % 2 != 0 and sum(self.row_one) != 15:
			self.row_one[0] = self.row_one[0] + diff

		if self.row_one[1] % 2 != 1 and sum(self.row_one) != 15:
			self.row_one[1] = self.row_one[1] + diff

		if self.row_one[2] % 2 != 0 and sum(self.row_one) != 15:
			self.row_one[2] = self.row_one[2] + diff 
	
	def fix_row_three(self):
		diff = 15 - sum(self.row_three)
		row_three = self.matrix[2]
		print("Diff: ", diff)
		if self.matrix[2][0] % 2 != 0 and sum(self.matrix[2]) != 15:
			self.matrix[2][0] = self.matrix[2][0] + diff

		if self.matrix[2][1] % 2 != 1 and sum(self.matrix[2]) != 15:
			self.matrix[2][1] = self.matrix[2][1] + diff

		if self.matrix[2][2] % 2 != 0 and sum(self.matrix[2]) != 15:
			self.matrix[2][2] = self.matrix[2][2] + diff 

	def fix_middle_row(self):

		diff = 15 - sum(self.row_two)
		if self.row_two[0] % 2 == 0:
			self.row_two[0] = self.row_two[0] + diff

		if self.row_two[2] % 2 == 0:
			self.row_two[2] = self.row_two[2] + diff

	

if __name__ == "__main__":

	sample_matrix = [[4,9,2], [3,5,7], [8,1,5]]
	sample_two = [[4, 4, 4], [3, 3, 3], [1, 2, 3]]
	sample_three = [[4,8,2], [4, 5, 7], [6, 1, 6]]
	sample_four = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
	sample_five = [[7, 6, 5], [7, 2, 8], [5, 3, 4]]

	square = magickSquare(sample_five)
	square.fix_middle_value()
	square.check_middle_value()
	square.get_diagonals()
	square.fix_diag_1()
	square.check_diagonals()
	square.get_diagonals()
	square.check_row_one()
	square.fix_row_one()
	square.check_row_one()
	square.fix_row_three()
	square.check_row_three()
	square.fix_middle_row()
	square.check_middle_row()

	print("############################\n")
	for el in square.matrix:
		print(el)
	
	