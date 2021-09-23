
def find_digits(num):
	counter = 0
	div = num
	while num != 0:
		mod = num % 10
		num = num // 10
		if mod != 0 and div % mod == 0:
			counter += 1

	return counter
		
if __name__ == "__main__":
	
	num = 12
	find_digits(num)