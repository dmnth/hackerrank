

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr[len(arr) // 2]
	if low < high:
		p = iterPartition(arr, low, high)
		quickSort(arr, low, p-1)
		quickSort(arr, p+1, high)


def partition(arr):

	pivot = arr[0]

	left = [x for x in arr if x < pivot]

	right = [x for x in arr if x > pivot]

	return left + [pivot] + right

def iterPartition(arr, low, high):

	pivot_value = arr[high]
	pivot_index = (low-1)

	for i in range(low, high):
		
		if arr[i] <= pivot_value:
			pivot_index += 1
			arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
			
	arr[pivot_index+1], arr[high] = arr[high], arr[pivot_index+1]

	return pivot_index + 1


if __name__ == "__main__":
	arr_6 = [5, 3, 1, 2, 4]
	arr_5 = [5, 7, 4, 3, 8]
	arr_4 = [3, 1, 6, 4, 7, 2]
	arr_3 = [3, 9, 4, 1, 7, 11, -2, -1, 0]
	arr_2 = [4, 5, 3, 7, 2]
	arr_1 = [-13, 68, -43, -71, -39, -10, -49, -19, -3, -70, -62, -76, -94, -73, 64, 72, -5, 88, 2, -63, 92, -40, 16, 49, 47, -86, -51, -9, -14, 96, 74, -22, -34, 38, -12, 6, 63, 19, -69, 14, -90, -27, 76, 54, 57, -87, -91, 43, -92]
	arr = [4, 7, 1, 9, 12, 33, 0]
	n = len(arr_6)
	result_2 = quickSort(arr_6, 0, n-1)
	print(result_2)
	print("###")