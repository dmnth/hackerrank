# minMaxSum

arr = [1, 2, 3, 4, 5]

def minmax(arr):

	sums_arr = []
	for i in range(len(arr)):
		print(sum(arr[1:]))
		for j in range(1, len(arr)):
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp

	return min(sums_arr), max(sums_arr)

minmax(arr)
		
	
