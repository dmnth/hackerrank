
def angryProfessor(k, a):
	
	stats = k.split()

	total = int(stats[0])
	threshold = int(stats[1])

	arrived = 0
	for t in a:
		if t <= 0:
			arrived += 1
	
	if arrived < threshold:
		return "YES"

	return "NO"

if __name__ == "__main__":

	inpt = open("./input/input01.txt", 'r').readlines()
	cases_num = int(inpt[0])

	test_idx = 1

	for i in range(cases_num):
		cap = inpt[test_idx].split()[0]
		min_att = inpt[test_idx].split()[1]
		treshold = inpt[test_idx]
		sl = [int(x) for x in inpt[test_idx+1].split()]
		result = angryProfessor(treshold, sl)
		print(result)
		test_idx += 2

		