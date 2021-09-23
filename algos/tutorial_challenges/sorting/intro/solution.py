
def elInArr(el, arr):
	idx = 0
	for x in arr:
		if arr == el:
			return idx
		idx += 1

if __name__ == "__main__":
	
	arr = [1, 3, 5, 9, 0, 13, 53]
	el = 3
	result = elInArr(el, arr)
	print(result)