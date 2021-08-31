class Book:

	def __init__(self, pages):
		self.pages = pages
		self.first_page = 1

	def count_pages_from_last(self, num):
		counter = 0
		if self.pages % 2 == 1:
			while self.pages-1 != num:
				self.pages -= 2
				counter += 1

		if self.pages % 2 == 0:
			while self.pages != num:
				self.pages -= 2
				counter += 1

		return counter

	def count_pages_from_first(self, num):
		counter = 0
		while counter != num:
			counter += 1

		if num % 2 == 0:
			return counter // 2
		else:
			return (counter-1) // 2




		

if __name__ == "__main__":

	book = Book(5)
	
	print(book.count_pages_from_first(4))
	print(book.count_pages_from_last(4))