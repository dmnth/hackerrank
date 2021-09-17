

def magickSquare(square):

	swaps = 0

	# Check middle row middle index, must be 5
	if square[1][1] != 5:
		square[1][1] -= square[1][1] - 5
		swaps += 1

	# Check corners
	corner_values = [2, 4, 8, 6]

	# (row index, element index, element value)
	known_corner = {}
	
	for row_idx in range(len(square)):
		for idx in range(len(square[row_idx])):
			if square[row_idx][idx] in corner_values:
				known_corner = {"row_idx": row_idx, "el_index": idx,"el_value": square[row_idx][idx]}
				break

	if known_corner:

		if known_corner['row_idx'] == 2 and known_corner['el_index'] == 0:
			opposite_element = square[0][2]
			if opposite_element + known_corner['el_value'] != 10:
				diff = (opposite_element + known_corner['el_value']) - 10
				square[0][2] -= diff

		elif known_corner['row_idx'] == 2 and known_corner['el_index'] == 2:
			opposite_element = [0][0]
			if opposite_element + known_corner['el_value'] != 10:
				diff = (opposite_element + known_corner['el_value']) - 10
				square[0][0] -= diff

		elif known_corner['row_idx'] == 0 and known_corner['el_index'] == 2:
			opposite_element = square[2][0]
			if opposite_element + known_corner['el_value'] != 10:
				diff = (opposite_element + known_corner['el_value']) - 10
				square[2][0] -= diff

		elif known_corner['row_idx'] == 0 and known_corner['el_index'] == 0:
			opposite_element = [2][2]
			if opposite_element + known_corner['el_value'] != 10:
				diff = (opposite_element + known_corner['el_value']) - 10
				square[2][2] -= diff


	return square

if __name__ == "__main__":

	square = [
			  [9,8,3],
			  [3,6,7],
			  [8,9,7]
			  ]

	result = magickSquare(square)
	for row in result:
		print(row)