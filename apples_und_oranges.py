# Apples and oranges

def do_some_calculations(s, t, a, b, apples, oranges):
	answer_oranges = 0
	answer_apples = 0

	house_zone = [x for x in range(s, t+1)]

	for idx in range(len(apples)):
		if a + apples[idx] in house_zone:
			answer_apples += 1

	for idx in range(len(oranges)):
		if b + oranges[idx] in house_zone:
			answer_oranges += 1
	
	print(answer_oranges)
	print(answer_apples)

if __name__ == "__main__": 
	
	left_pointer = 7
	right_pointer = 10
	apple_tree_location = 4
	orange_tree_location = 12
	amount_apples = [2, 3, -4]
	amount_oranges = [3, -2, -4]

	do_some_calculations(left_pointer, right_pointer, apple_tree_location, \
	orange_tree_location, amount_apples, amount_oranges)