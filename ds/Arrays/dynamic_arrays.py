#! /usr/bin/env python3

# Dynamic arrays
# Declare a 2-dimensional array of n empty arrays
# Declare an integer, lastAnswer and initialize it to 0

def dynamic_array(n, queries):

	arr = [[] for i in range(n)]
	answers = []
	lastAnswer = 0

	for element in queries:

		if element[0] == 1:
			idx = ((element[1] ^ lastAnswer) % n)
			arr[idx].append(element[2])
			print(arr[idx])
			
		elif element[0] == 2:
			idx = ((element[1] ^ lastAnswer) % n)
			lastAnswer = arr[idx][element[2] % len(arr[idx])]
			answers.append(lastAnswer)
			
	return answers

if __name__ == "__main__":
	
	num = 2
	queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
	result = dynamic_array(num, queries)
	print(result)