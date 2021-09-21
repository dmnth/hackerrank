

def cloudCounter(clouds, jump_size):

	energy_level = 100
	idx = 0
	n = len(clouds)

	while True:

		idx = (idx + jump_size) % n

		if clouds[idx] == 1:
			energy_level -= 3
		else:
			energy_level -= 1

		if idx == 0:
			break

	return energy_level
if __name__ == "__main__":

	c = [0, 0, 1, 0, 0, 1, 1, 0]
	k = 2
	result = cloudCounter(c, k)
	print(result)