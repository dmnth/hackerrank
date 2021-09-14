

def hurdleRace(k, height):
	
	max = 0
	for el in height:
		if el > max:
			max = el

	if k > max:
		return 0

	return (max - k)


if __name__ == "__main__":	

	k = 4
	height = [1, 6, 3, 5, 2]

	result = hurdleRace(k, height)
	print(result)