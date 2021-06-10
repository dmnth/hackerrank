#! /usr/bin/env python3

# Left rotation

def left_rotation(num, array):
	last_index = len(array) - 1
	
	idx = 0
	for i in range(num):
		for j in range(len(array)-1):
			array[j], array[j+1] = array[j+1], array[j]

			print(array)
	
def left_rotation_2(num, arr):
	return arr[num:] + arr[:num]
		
		
if __name__ == "__main__":
	
	arr = [1, 2, 3, 4, 5]
#	left_rotation(4, arr)
	left_rotation_2(4, arr)
