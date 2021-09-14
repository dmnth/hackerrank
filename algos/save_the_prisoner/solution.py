

def saveThePrisoner(prisoners, candy, chair_num):

	result = ((chair_num - 1 + candy - 1) % prisoners) + 1

	return result

if __name__ == "__main__":

	n = 7  #prisoners
	m = 19 #pieces
	s = 2  #chair

	result = saveThePrisoner(n, m, s)
	print(result)