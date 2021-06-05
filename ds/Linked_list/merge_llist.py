#! /usr/bin/env python3

# Merge linked lists here

class Node:

	def __init__(self, value, next_node=None):

		self.value = value
		self.next_node = next_node

	def set_next_node(self, next_node):

		self.next_node = next_node

	def get_next_node(self):

		return self.next_node

	def get_node_value(self):

		return self.value 

class LinkedList:

	def __init__(self):

		self.head_node = None
		self.tail_node = None

	def get_head_node(self):
		return self.head_node

	def search(self, value):

		if self.head_node.get_node_value() == value:
			msg = 'Node with value {} is found'.format(value)
			return

		current_node = self.head_node
		while current_node:
			if current_node.get_node_value() == value:
				break
			current_node = current_node.get_next_node()

		if current_node:
			return current_node.get_node_value()
		else:
			return 'no such value in this list, sir'

	def sorted_insert(self, value):

		if type(value) is not int and type(value) is not float:
			msg = '(._.) cannot into strings'
			print(msg)
			return 

		node_to_add = Node(value)

		if self.head_node is None:
			self.head_node = node_to_add
			self.tail_node = node_to_add
			return

		if node_to_add.get_node_value() <= self.head_node.get_node_value():
			self.add_head(value)
			return

		if node_to_add.get_node_value() >= self.tail_node.get_node_value():
			self.add_tail(value)
			return

		current_node = self.head_node
		previous_node = None

		while current_node.get_next_node():

			if node_to_add.get_node_value() > current_node.get_next_node().get_node_value():
				current_node = current_node.get_next_node()

			if node_to_add.get_node_value() <= current_node.get_next_node().get_node_value():
				node_to_add.set_next_node(current_node.get_next_node())
				current_node.set_next_node(node_to_add)
				break

	def add_head(self, value):

		node = Node(value)

		if self.head_node is None:
			self.head_node = node 
			self.tail_node = node
			return

		node.set_next_node(self.head_node)
		self.head_node = node 

	def add_tail(self, value):

		new_tail = Node(value)

		if self.head_node is None:
			self.head_node = new_tail
			self.tail_node = new_tail
			return

		# Get current tail
		self.tail_node.set_next_node(new_tail)
		self.tail_node = new_tail

	def remove_from_list(self, value):

		node_to_remove = Node(value)

		current_node = self.head_node

		return

	def traverse_list(self):

		string = ''

		current_node = self.head_node

		while current_node:

			string += str(current_node.get_node_value()) + '\n'
			current_node = current_node.get_next_node()

		return string

	def remove_dublicates(self):

		current_node = self.head_node

		while current_node.next_node is not None:

			if current_node.get_node_value() == current_node.get_next_node().get_node_value():
				current_node.set_next_node(current_node.get_next_node().get_next_node())

			else:

				if current_node.get_next_node().get_next_node() is None and current_node.get_node_value() == current_node.get_next_node().get_node_value():
					current_node.set_next_node(None)

				current_node = current_node.get_next_node()

class Solution:

	def __init__(self, ll_1, ll_2):

		self.ll_1 = ll_1
		self.ll_2 = ll_2

	def populate_lists(self, test_case_txt):

		with open('merge_list_test_1.txt', 'r') as file:
			test_case = file.readlines()
	
		counter = 0
		test_list = []
		for element in test_case:
			element = int(element.strip('\n'))
			test_list.append(element)
			
		first_test_case_1 = test_list[2:99]
		first_test_case_2 = test_list[100:170]

		for element in first_test_case_1:
			other_list.sorted_insert(element)

		for element in first_test_case_2:
			ol_list.sorted_insert(element)


	def merge_lists(self):

		current_1 = self.ll_1.get_head_node()
		current_2 = self.ll_2.get_head_node()
		other_list = LinkedList()


		if current_1.get_node_value() <= current_2.get_node_value():
			other_list.head_node = current_1
			other_list.tail_node = current_1
			current_1 = current_1.get_next_node()

		else:
			other_list.head_node = current_2
			other_list.tail_node = current_2
			current_2 = current_2.get_next_node()


		while current_1 is not None and current_2 is not None:

			
			if current_1.get_node_value() <= current_2.get_node_value():
				new_node = Node(current_1.get_node_value())
				other_list.tail_node.set_next_node(new_node)
				other_list.tail_node = new_node
				current_1=current_1.get_next_node()

			else:
				new_node = Node(current_2.get_node_value())
				other_list.tail_node.set_next_node(new_node)
				other_list.tail_node = new_node
				current_2 = current_2.get_next_node()
				

		if current_1:
			other_list.tail_node.set_next_node(current_1)

		if current_2:
			other_list.tail_node.set_next_node(current_2)

		return other_list.head_node


if __name__ == "__main__":

	new_list = LinkedList()
	ol_list = LinkedList()
	
	new_list.add_tail(1)
	new_list.add_tail(1)
	new_list.add_tail(1)
	new_list.add_tail(2)
	new_list.add_tail(2)
	new_list.add_tail(2)
	new_list.add_tail(3)
	new_list.add_tail(3)
	new_list.add_tail(3)
	new_list.add_tail(3)
	new_list.add_tail(3)
	new_list.add_tail(4)
	new_list.add_tail(5)
	new_list.add_tail(5)
	new_list.add_tail(5)
	new_list.add_tail(5)
	

	ol_list.sorted_insert(2)
	ol_list.sorted_insert(19)

	ol_list.remove_dublicates()
	new_list.remove_dublicates()
	print('\n', '*' * 20, '\n')
	print(new_list.traverse_list())
	print(ol_list.traverse_list())


