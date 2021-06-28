# Tree top view

# traverse by level
# Store horizontal indexes in hash_map
# return keys
# ??? 
# profit

from binary_tree_class import BinarySearchTree, Node

def top_view(root_node):
	
	stack = []
	current_node = root_node
	hash_map = {}
	level = 0

	while True:

		if current_node is not None:
			stack.append(current_node)
			current_node = current_node.left

		elif stack:
			current_node = stack.pop()
			hash_map[level+1] = current_node
			print(current_node.info, end=" ")
			current_node = current_node.right

		else:
			break

	print(hash_map)
	
if __name__ == "__main__":
	
	my_tree = BinarySearchTree()
	elements = [-1, -2, -3, 0, 1, 2, 5, 3, 6, 4, 7, 8, 10]
	board_elements = [39, 28, 51, 13, 37, 46, 60, 12, 14, 53, 65, 52]
	test_string = "37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 112 20 26 30 93 96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 92 45 75 116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 89 51 19 3"
	#test_array = test_string.split()
	test_array = [37, 23, 108, 59, 55, 86, 64, 94, 65, 14, 105, 17, 111, 115]
	#test_array = [99, 60, 155, 41, 73, 81, 85, 86, 87, 80, 79, 78, 77, 40]
	for element in test_array:
		my_tree.create(element)

	result = top_view(my_tree.root)
	#for key, value in result.items():
	#	print(key, value)