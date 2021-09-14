

def viralAdvertising(n):
	recepients = 5
	people_received_adv = 0
	for day in range(n):
		people_received_adv += (recepients // 2)
		recepients = (recepients // 2) * 3
	return people_received_adv

if __name__ == "__main__":

	n = 3
	result = viralAdvertising(n)
	print(result)