# A recursive solution

"""
1, 2 ,3 ,4, 5, 6, 7, 8, 9

1: 1, 2
2: 1, 2, 3
3: 2, 3, 4
4: 3, 4, 5
5: 4, 5, 6
6: 5, 6, 7
7: 6, 7, 8
8: 7, 8, 9
9: 8, 9
"""

def pickingNumbers(test_array):
		sorted(test_array)
		hash_map = {}
		for el in test_array:
			hash_map[el] = []
			for i in range(len(test_array)):
				if abs(el - test_array[i]) <= 1:
					hash_map[el].append(test_array[i])

		max_len = 0
		max_len_key = 0
		for key, element in hash_map.items():
			if key in [50, 51, 52, 53, 54, 55]:
				print("!!!!!")
				print(key, element)
		for key, value in hash_map.items():
			if check_hash_map(value) is False:
				pass
			else:
				if len(value) > max_len:
					print(value)
					max_len = len(value)
					max_len_key = key

		return len(hash_map[max_len_key])

def check_hash_map(hash_map_element):
		for element in hash_map_element:
			for component in hash_map_element:
				if abs(component-element) > 1:
					return False
		return True

if __name__ == "__main__":
	test_array = [1, 2, 2, 3, 1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 6, 7, 2, 3, 4, 5 , 1, 2, 3 ,4, 7,4, 5]
	test_array_2 = [4, 6, 5, 3, 3, 1]
	test_array_3 = [33, 33, 45, 32, 31, 45, 45, 46, 32, 47, 99, 99, 99, 99, 100, 98, 98, 97, 97, 97, 97, 96, 96, 96]
	test_array_4 = []
	with open("test_case.txt" , 'r') as file:
		file = file.readlines()[1].split(" ")
		for element in file:
			test_array_4.append(int(element))

	

	result = pickingNumbers(test_array_4)
	
	print(result)
