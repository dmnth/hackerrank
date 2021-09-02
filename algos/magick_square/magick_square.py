
class magickSquare:

	def __init__(self, matrix):

		self.matrix = matrix
		
		self.diag_one = []
		self.diag_two = []

	def get_diagonals(self):
		idx = 0
		for row in self.matrix:
			self.diag_one.append(row[idx])
			idx += 1

		for row in self.matrix:
			self.diag_two.append(row[idx-1])
			idx -= 1

			
	def check_rows(self, idx):
		row = self.matrix[idx]
		cost = 0
		diff = 15 - sum(row)
		# Checks middle row of matrix
		if idx == 1:
			
			for idx in range(len(row)):
				if row[idx] % 2 == 0:
					print(f"This should not be divisible by 2: {row}")
					old_value = row[idx]
					new_value = row[idx] + diff
					row[idx] = new_value
					cost += abs(new_value-old_value)


		# Checks top and bottom row of matrix
		if sum(row) != 15:
			print("This particular row aint good:")
			
			if row[0] % 2 == 1:
				print(f"{row[0]} in {row} needs to be replaced")
				old_value = row[0]
				new_value = row[0] + diff
				row[0] = new_value
				cost += abs(new_value - old_value)
				print(new_value, cost)

			if row[1] % 2 == 0:
				print(f"{row[1]} in {row} needs to be replaced")
				old_value = row[0]
				new_value = row[0] + diff
				row[0] = new_value
				cost += abs(new_value - old_value)
				print(new_value, cost)

			if row[2] % 2 == 1:
				print(f"{row[2]} in {row} needs to be replaced")
				old_value = row[0]
				new_value = row[0] + diff
				row[0] = new_value
				cost += abs(new_value - old_value)
				print(new_value, cost)

			if row[0] == row[2] :
				print(f"dublicates in {row}")
				old_value = row[0]
				new_value = row[0] + diff
				row[0] = new_value
				cost += abs(new_value - old_value)
				print(new_value, cost)

		return cost
		
	def form_row(self):
		row = self.matrix[0]
		print(row)
		
		while True:

			diff = 15 - sum(row)
			print(row, diff)
			if row[0] % 2 == 1:
				row[0] += diff

			if row[0] == row[2]:
				row[0] += diff

			if row[1] % 2 == 0:
				row[1] += diff

			if sum(row) == 15 and row[1] % 2 == 1:
				return

	def for_loops(self):
		for i in range(len(self.range)):
			for j in range(len(self.range)):
				for k in range(len(self.range)):
					if i+j+k == 15 and j != k:
						el = [i, j, k]
						if el[1] == 5:
							print(el, ": middle row")

						if i % 2 == 0 and k % 2 == 0:
							print(el)	

	def nice_try(self):
		# Check center -> check diags -> check rows




if __name__ == "__main__":

	sample_matrix = [[4,9,2], [3,5,7], [8,1,5]]
	sample_two = [[4, 4, 4], [3, 3, 3], [1, 2, 3]]
	sample_three = [[4,8,2], [4, 5, 7], [6, 1, 6]]
	sample_four = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
	sample_five = [[7, 6, 5], [7, 2, 8], [5, 3, 4]]
	square = magickSquare(sample_five)
	square.get_diagonals()
	cost = 0
	for idx in range(len(square.matrix)):
		cost += square.check_rows(idx)
	print(cost)
	print(square.matrix)
	"""
	
	for el in square.matrix:
		print(el)
	print("\n")
	result = square.check_rows()
	print(f"swap cost: {result}")
	for el in square.matrix:
		print(el)
	"""
	
