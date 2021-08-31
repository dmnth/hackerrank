

def catAndMouse(q):
	a = q[0]
	b = q[1]
	c = q[2]

	a_point = abs(c - a)
	b_point = abs(c - b)

	while True:

		if a_point < b_point:
			print("A")
			return a_point
		if a_point > b_point:
			print("B")
			return b_point
		else:
			print("Escapes")
			return
			c += 1

if __name__ == "__main__":
	q = [1, 3, 2]
	result = catAndMouse(q)
	print(result)