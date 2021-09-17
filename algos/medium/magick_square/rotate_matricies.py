
# Transponse -> intercharging of rows and columns
def rotateClockwise(mtrx):
	new_matrix = [[0,0,0], [0,0,0], [0, 0,0]]
	for i in range(len(mtrx)):
		for j in range(len(mtrx[0])-1,-1,-1):
			new_matrix[i][j] = mtrx[j-1][i]
	
	return new_matrix

def rotateCounterClockwise(mtrx):
	return

if __name__ == "__main__":

	mtrx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	new_matrix = rotateClockwise(mtrx)
	for el in new_matrix:
		print(el)