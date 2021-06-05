#! /usr/bin/env python3

class Node:

	def __init__(self, data, next_node=None):

		self.data = data
		self.next_node = next_node

class Stack:

	def __init__(self):

		self.top = None 
		self.height = 0

	def is_empty(self):
		if self.height == 0:
			return True

	def push(self, value):

		new_node = Node(value)

		if not self.top:
			self.top = new_node
			self.height += value
			return

		new_node.next_node = self.top
		self.top = new_node
		self.height += value

	def pop(self):

		if not self.is_empty():
			value_to_remove = self.top.data
			self.top = self.top.next_node
			self.height -= value_to_remove
			return value_to_remove

		else:
			print('stack is empty')

	def peek(self):

		if not self.is_empty():
			print(self.top.data)
			return

		else:
			print('stack is empty')

class Solution():

	def __init__(self, stack1, stack2, stack3):

		self.stack_1 = stack1
		self.stack_2 = stack2
		self.stack_3 = stack3

	def get_biggest_stack(self):

		hash_map = {self.stack_1.height: self.stack_1, self.stack_2.height: self.stack_2, self.stack_3.height: self.stack_3}

		largest_key = 0
		for key in hash_map:
			if key > largest_key:
				largest_key = key

		return hash_map[largest_key]

	def equalize_stacks(self):

		while True:

			largest_stack = self.get_biggest_stack()

			if self.stack_1.height == self.stack_2.height and self.stack_2.height == self.stack_3.height:
				break
			
			largest_stack.pop()

		return largest_stack.height


if __name__ == "__main__":



	first_stack = Stack()
	second_stack = Stack()
	third_stack = Stack()

	first_stack.push(1)
	first_stack.push(1)
	first_stack.push(1)
	first_stack.push(2)
	first_stack.push(3)

	second_stack.push(2)
	second_stack.push(3)
	second_stack.push(4)

	third_stack.push(1)
	third_stack.push(4)
	third_stack.push(1)
	third_stack.push(1)


	operations = Solution(first_stack, second_stack, third_stack)
	result = operations.equalize_stacks()
	print(result)