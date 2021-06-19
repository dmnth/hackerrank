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
				hash_map[distance-1] = elements.left.info
			else:
				hash_map[distance-1].append(element.left.info)
			q.append((distance-1, element.left))
		
		if element.right:
			if distance+1 not in hash_map.keys():
				hash_map[distance+1] = [element.right.info]
			else:
				hash_map[distance+1].append(element.right.info)
			q.append((distance+1, element.right))

	

			
	return hash_map

if __name__ == "__main__":

	my_tree = BinarySearchTree()
	elements = [1, 2, 5, 3, 6, 4]
	for element in elements:
		my_tree.create(element)
	result = verticale_traversal(my_tree.root)
	print(result)