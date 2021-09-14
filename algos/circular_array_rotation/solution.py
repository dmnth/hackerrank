

def circularArrayRotation(arr, k, queries):
	
	ind = []
	for i in queries:
		ind.append(arr[(i-k)%len(arr)])

	return ind
if __name__ == "__main__":

	a = [1, 2, 3]
	q = [0, 1, 2]
	k = 2

	result = circularArrayRotation(a, k, q)
	print(result)