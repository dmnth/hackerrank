# Utopian tree, planted in onsent of sprint with height=1
# Goes through two cycles of growth every year
# Each spring it doubles in height
# Each summer its height increases by 1 meter

class utopianTree:

	def __init__(self):
		self.height = 1

	def spring_cycle_growth(self):
		self.height *= 2

	def summer_cycle_growth(self):
		self.height += 1

	def calculate_growth(self, cycles):

		for i in range(cycles):
			if i % 2 == 0:
				self.spring_cycle_growth()
			if i % 2 ==1:
				self.summer_cycle_growth()

	def print_height(self):
		print(self.height)

if __name__ == "__main__":
	tree = utopianTree()
	tree.calculate_growth(4)
	new_tree = utopianTree()
	new_tree.calculate_growth(3)
	tree.print_height()
	new_tree.print_height()

