
def countSort(arr):
	new_arr = [0 for x in range(len(arr)-1)]
	max_el = max(arr) 
	count_len = max_el + 1
	counter = [0] * count_len
	print(counter)
	print(new_arr)


	for idx in range(len(arr)):
		new_arr[arr[idx]] += 1

	pos = 0
	print(new_arr)
	for n in range(len(new_arr)):
		for i in range(new_arr[n]):
			print(arr[pos], n, pos)
			arr[pos] = n
			pos += 1

	
	return arr

if __name__ == "__main__":
	arr = [1, 1, 3, 2, 1]
	result = countSort(arr)
	print(result)