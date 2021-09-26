
def insertionSort(arr):
	shifts = 0
	for i in range(1, len(arr)):
		el = arr[i]
		el_idx = i

		idx = el_idx - 1
		
		while el < arr[idx] and idx >= 0:
			arr[idx+1] = arr[idx]
			shifts += 1
			idx -= 1


		arr[idx+1] = el
		
	return shifts


if __name__ == "__main__":

	arr = [2, 1, 3, 1, 2]
	sorted_arr = insertionSort(arr)
	mid = len(arr) // 2
	print(mid)

	