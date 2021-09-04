

class Number:

	def __init__(self, num):
		self.num = num

	def absolute_difference(self, num):
		return abs(self.num-num)

	def get_value(self):
		return self.num

class subArray:

	def __init__(self):
		self.array = []

	def add_number(self, number):
		self.array.append(number)

	def counter(self, test_array):
		possible_subsets = []
		counter = {}
		for i in range(len(test_array)-1):
			difference = abs(test_array[i]-test_array[i+1])
			if difference <= 1:
				print("possible subset: ", test_array[i], test_array[i+1], "differens: ", abs(test_array[i]-test_array[i+1]))
				subset = (test_array[i], test_array[i+1])
				possible_subsets.append(subset)
				if subset not in counter:
					counter[subset] = 0

		for i in range(len(test_array)-1):
			for j in range(len(possible_subsets)):
				if test_array[i] == possible_subsets[j][0] and test_array[i+1] == possible_subsets[j][1]:
					counter[possible_subsets[j]] += 1

		print(counter)

if __name__ == "__main__":
	test_array = [1, 2, 2, 3, 1, 2]
	test_array_2 = [4, 6, 5, 3, 3, 1]

	def pickingNumbers(array):
		hash_map = {}
		for el in test_array:
			hash_map[el] = []
			for i in range(len(test_array)):
				if abs(el - test_array[i]) <= 1:
					hash_map[el].append(test_array[i])
		return hash_map

	result = pickingNumbers(test_array)
	print(result)