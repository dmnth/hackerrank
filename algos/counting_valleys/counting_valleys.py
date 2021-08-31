class Path:
	def __init__(self, trail):
		self.trail = [x for x in trail]
		self.length = len(self.trail)
		self.mountains = 0
		self.valleys = 0
		self.sea_level = 1

class Hiker:

	def __init__(self, path_class):
		self.path = path_class
		self.name = None
		self.age = int()
		self.mountains_climbed = 0

	def set_name(self, name):
		self.name = name

	def set_age(self, age):
		self.age = age

	def count_steps(self):
		curr_level = 1
		for el in self.path.trail:
			if el == "D":
				curr_level -= 1
				print("goin down")
				if curr_level == self.path.sea_level:
					print("Went down from mountain.")
					self.path.mountains += 1
					self.mountains_climbed += 1
				if curr_level < self.path.sea_level:
					print('in a valley now')
			if el == "U":
				curr_level += 1
				if curr_level > self.path.sea_level:
					print("climbing mountain")
				if curr_level == self.path.sea_level:
					print("went back to sea level")
					self.path.valleys += 1

	def boris_flex(self):
		if self.path.valleys > 1:
			valleys = "valley's"
		if self.path.mountains > 1:
			mountains = "mountain's"
		else:
			valleys = 'valley'
			mountains = 'mountain'

		print(f"{self.name} went through {self.path.valleys} {valleys} and climbed {self.mountains_climbed} {mountains} at {self.age}.")



if __name__ == "__main__":
	new_path = Path("UDDDUDUU")
	boris = Hiker(new_path) 
	boris.set_name("Boris Miroslavovich Donskihh")
	boris.set_age(45)
	boris.count_steps()
	boris.boris_flex()
