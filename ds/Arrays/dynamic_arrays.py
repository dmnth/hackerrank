#! /usr/bin/env python3

# Dynamic arrays
# Declare a 2-dimensional array of n empty arrays
# Declare an integer, lastAnswer and initialize it to 0

def dynamic_array(n, queries):

	answers = [[] for i in range(n)]
	sup = []
	lastAnswer = 0

	for element in queries:

		if element[0] == 1:
			idx = ((element[1] ^ lastAnswer) % n)
			answers[idx].append(element[2])
			print(answers[idx])
			
		elif element[0] == 2:
			idx = ((element[1] ^ lastAnswer) % n)
			lastAnswer = answers[idx][element[2] % len(answers[idx])]
			sup.append(lastAnswer)
			
			

	print(sup)
	return 'Aspergo'

if __name__ == "__main__":
	
	num = 2
	queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
	result = dynamic_array(num, queries)