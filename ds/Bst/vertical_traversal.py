# Vertical level order traversal

from binary_tree_class import BinarySearchTree, Node


def verticale_traversal(root):

	if root is None:
		return 

	# Hhorizontal distance on X axis
	hd = 0
	q = [(hd, root)]
	# Need to iterate through node and hd simulatenousl...whatever
	hash_map = {0: [root.info]}
	while q:

		
		distance, element = q.pop(0)

		if element.left:
		
			if distance-1 not in hash_map.keys():
				hash_map[distance-1] = [element.left.info]
			else:
				hash_map[distance-1].append(element.left.info)
			q.append((distance-1, element.left))
		
		if element.right:
			
			if distance+1 not in hash_map.keys():
				hash_map[distance+1] = [element.right.info]
			else:
				hash_map[distance+1].append(element.right.info)
			q.append((distance+1, element.right))

	

			
	print(hash_map)

if __name__ == "__main__":

	my_tree = BinarySearchTree()
	elements = [1, 2, 5, 3, 6, 4, 7, 8, 9, 19, 39, 102, 934, 991, 1241, 32, 43, 54]
	uno_elements = [39, 28, 51, 13, 7, 26, 37, 30, 38, 46, 41, 50, 60, 59, 61]
	numbers ="37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 112 20 26 30 93 96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 92 45 75 116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 89 51 19 3"
	more_numbers = numbers.split()
	for element in more_numbers:

		my_tree.create(element)
	result = verticale_traversal(my_tree.root)
	print(result)