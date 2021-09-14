
def beautifulDays(i, j, k):
	days_range = [x for x in range(i, j+1)]
	bDays = 0
	for day in days_range:
		if (day - reversed(day)) % k == 0:
			bDays += 1

	return bDays

def reversed(num):
	rev_num = 0
	while num > 0:
		remainder = num % 10
		rev_num = (rev_num * 10) + remainder
		num = num // 10
	return rev_num

if __name__ == "__main__":

	i = 20
	j = 23
	k = 6

	result = beautifulDays(i, j, k)
	print(result)