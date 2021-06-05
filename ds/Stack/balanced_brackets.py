#! /usr/bin/env python3

class Node:

	def __init__(self, value, next_node = None):

		self.value = value
		self.next_node = next_node

	def set_next_node(self, next_node):
		self.next_node = next_node

	def get_next_node(self):
		if self.next_node is None:
			msg = 'Ooopsie woopsie, looks like fuckie wuckie =)))))))))))))))'
			return msg

		return self.next_node

	def get_value(self):
		return self.value

class Stack:

	def __init__(self, limit=90000):

		self.limit = limit
		self.top = None
		self.bottom = None
		self.size = 0

	def is_empty(self):
		if self.size == 0:
			return True

	def push(self, value):
		new_node = Node(value)

		if not self.top:
			self.top = new_node
			self.bottom = new_node
			self.size += 1
			return

		new_node.set_next_node(self.top)
		self.top = new_node
		self.size += 1

	def pop(self):

		if not self.is_empty():

			value_to_return = self.top.get_value()
			self.top = self.top.get_next_node()
			self.size -= 1
			return value_to_return

		return 'Stack is empty, go pop yourself.'


	def peek(self):

		if not self.is_empty():
			print('{} is on top of this shitpile'.format(self.top.get_value()))
			return
		print('Stack is empty, fool!')

if __name__ == "__main__":

	my_stack = Stack()
	ol_stack = Stack()
	string = '([{([[]]})])'
	middle_idx = len(string) // 2
	first_half = string[:middle_idx]
	second_half = string[middle_idx:]
	for i in range(len(string) // 2):
		my_stack.push(first_half[i])
		ol_stack.push(second_half[i])
	
	while not my_stack.is_empty():
		print(my_stack.pop(), ol_stack.pop())
	
	









		

