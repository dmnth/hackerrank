
class byPairSorter:

	def __init__(self, pile):
		self.pile = pile
		self.sorted_pile = []

		
	def check_for_pair(self):
		counter = 0
		while len(self.pile) > 1:
			current_color = self.pile.pop()
			for element in self.pile:
				if element == current_color:
					pair = (current_color, True)
					self.sorted_pile.append(pair)
					self.pile.remove(element)
					counter += 1
					break
			
				else:
					pair = (current_color, False)
					if pair not in self.sorted_pile:
						self.sorted_pile.append(pair)		

		return counter

	def get_pairless(self):
		return [sock for sock in self.sorted_pile if sock[1] == False]

	def get_pairs(self):
		return [sock for sock in self.sorted_pile if sock not in self.get_pairless()]

	def redeem_ineer_peace(self):
		with_pairs = len(self.get_pairs())
		without_pairs = len(self.get_pairless())
		print(f"[+] Hippity hoppity {without_pairs} socks without pairs are now my property.")

if __name__ == "__main__":
	
	unsorted_pile = [10, 20, 20, 10, 10, 30, 50, 10, 20]
	
	obsessiveSyndrome = byPairSorter(unsorted_pile)
	obsessiveSyndrome.check_for_pair()
	obsessiveSyndrome.redeem_ineer_peace()
	

	
	



