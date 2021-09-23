def recur_factorial(n):
	if n == 1:
		return n
	else:
		return n * recur_factorial(n-1)

if __name__ == "__main__":
	result = recur_factorial(25)
	print(result)