
# Transponse -> intercharging of rows and columns
def rotateClockwise(mtrx):
	new_matrix = [[0,0,0], [0,0,0], [0, 0,0]]
	for i in range(len(mtrx)):
		for j in range(len(mtrx[0])-1,-1,-1):
			new_matrix[i][j] = mtrx[j][i]
		
	
	return new_matrix

def rotateCounterClockwise(mtrx):
	return

def rotate_matrix(m):
	return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]


if __name__ == "__main__":

	mtrx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	for el in mtrx:
		print(el)
	print('############')
	new_matrix = rotateClockwise(mtrx)
	for i in range(5):
		
		new_matrix = rotateClockwise(new_matrix)
		print("##############")
		for el in new_matrix:
			print(el)

