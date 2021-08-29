# Prints amount of monet Brian owes Anna if bill wasnt fairly split

class Person:

	def __init__(self, foods):
		self.order = foods

	def exclude(self, idx):
		return self.order.pop(idx)

	def calculate_total(self):
		return sum(self.order)

	def spare_order(self):
		return self.calculate_total() // 2


if __name__ == "__main__":

	order = [2, 4, 6]

	Anna = Person(order)
	Brian = Person(order)

	
	brian_spare = Brian.spare_order()

	item = Anna.exclude(2)
	anna_spare = Anna.spare_order()

	if anna_spare != brian_spare:
		print("brian owes to ann:")
		print(brian_spare - anna_spare)