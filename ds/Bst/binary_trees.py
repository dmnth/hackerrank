#! /usr/bin/env python3

# Features to add: delete value, self-balance, level-order traversal

class Bst:

	def __init__(self, value, depth=1):

		self.value = value
		self.depth = depth
		self.left = None
		self.right = None

	def insert(self, value):

		# O(logN)

		if value < self.value:

			if self.left is None:
				self.left = Bst(value, self.depth + 1)
				print(f"value {value} added to the left of {self.value} at depth {self.depth}")

			else:
				self.left.insert(value)

		if value > self.value:

			if self.right is None:
				self.right = Bst(value, self.depth + 1)
				print(f"value {value} added to the right of {self.value} at depth {self.depth}")

			else:
				self.right.insert(value)

	def get_node_by_value(self, value):

		# O(logN)

		if self.value == value:
			return self.value

		elif self.left and value < self.value:
			return self.left.get_node_by_value(value)

		elif self.right and value > self.value:
			return self.right.get_node_by_value(value)
		else:
			return None

	def depth_first_traversal(self):
		# Preorder:
		print(f"Depth = {self.depth}, value = {self.value}")
		# Traverse the left subtree if present:
		if self.left is not None:
			self.left.depth_first_traversal()

		# Print out result for inorder traversal:
		# print(f"Depth = {self.depth}, value = {self.value}")

		# Traverse the right subtree if present:
		if self.right is not None:
			self.right.depth_first_traversal()

		# Postorder:
		# print(f"Depth = {self.depth}, value = {self.value}")

if __name__ == "__main__":

	new_bst = Bst(39)
	new_bst.insert(28)
	new_bst.insert(51)
	new_bst.insert(13)
	new_bst.insert(37)
	new_bst.insert(46)
	new_bst.insert(60)
	print(new_bst.depth_first_traversal())
