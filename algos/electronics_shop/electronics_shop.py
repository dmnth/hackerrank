import sys


class Person:
	def __init__(self, name, age, budget):
		self.name = name 
		self.age = age
		self.budget = budget

	def process_order(self, items_list):
		max_price = 0
		for price in items_list:
			if price > max_price:
				max_price_item = price
		return max_price_item

	def make_an_order(self, price):
		print(f"{self.name} decided to spend {price}$")


class electronicsShop:
	def __init__(self, keyboards, drives):
		self.keyboards = keyboards
		self.drives = drives

	def make_offer(self, budget):
		possible_pairs = []
		for keyboard in self.keyboards:
			for drive in self.drives:
				summ = keyboard + drive
				if summ <= budget:
					possible_pairs.append(summ)

		if possible_pairs is not []:
			return possible_pairs
		else:
			print("Cant make order for this budget")
			

if __name__ == "__main__":
	boris = Person('Boris', 45, 60)
	stookies = electronicsShop([40, 50, 60], [5, 8, 12])
	offer = stookies.make_offer(boris.budget)
	if offer:
		result = boris.process_order(offer)
		boris.make_an_order(result)
