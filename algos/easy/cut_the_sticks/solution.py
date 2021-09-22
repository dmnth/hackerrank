
def cut_the_sticks(arr):
	cut = 0
	while len(arr) > 0:
		smallest_stick = arr[0]
		for stick in arr:
			if stick < smallest_stick:
				smallest_stick = stick

		cut = arr.count(smallest_stick)
		arr = [x for x in arr if x != smallest_stick]
		
		for i in range(len(arr)):
			arr[i] -= smallest_stick
			cut += 1
		print(cut)
	
		

if __name__ == "__main__":

	stick_lengths = [5, 4, 4, 2, 2, 8]
	stick_lengths_1 = [1, 2, 3, 4, 3, 3, 2, 1]
	result = cut_the_sticks(stick_lengths_1)
	print(result)