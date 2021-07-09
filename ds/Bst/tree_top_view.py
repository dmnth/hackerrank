# Tree top view

# traverse by level
# Store horizontal indexes in hash_map
# return keys
# ??? 
# profit

from binary_tree_class import BinarySearchTree, Node

def top_view(root_node):

	if root_node is None:
		return
	
	hash_map = {}
	level = 0
	kiu = [(root_node, level)]

	# Iterative in-order traversal:
	# Way to count nodes on each level

	while len(kiu):

		node = kiu[0][0]
		value = kiu[0][0].info
		depth = kiu[0][1]

		if depth not in hash_map.keys():
			hash_map[depth] = str(value)

		#if depth not in hash_map.keys():
		#	hash_map[depth] = str(value) 

		if node.left:
			level = depth - 1
			element = (node.left, level)
			kiu.append(element)

		if node.right:
			level = depth + 1
			element = (node.right, level)
			kiu.append(element)

		kiu.pop(0)

	print(hash_map)
	print(' '.join(sorted(hash_map.values())))

# Find difference between these two

def topView(root):
    #Write your code here
    topView_node = {}
    topView_node[root] = 0
    node_list = []
    v = [root, 0]
    node_list.append(v)
    while len(node_list) > 0:
        node1 = node_list.pop(0)
        node = node1[0]
        if node1[1] not in topView_node.values():
            topView_node[node] = node1[1]
        if node.left:
            value = node1[1] - 1
            v = [node.left, value]
            node_list.append(v)
        if node.right:
            value = node1[1] + 1
            v = [node.right, value]
            node_list.append(v)
    
    for key, value in sorted(topView_node.items(), key = lambda x: x[1]):
        print(key.info, end=" ")





	
if __name__ == "__main__":
	
	my_tree = BinarySearchTree()
	elements = [-1, -2, -3, 0, 1, 2, 5, 3, 6, 4, 7, 8, 10]
	board_elements = [39, 28, 51, 13, 37, 46, 60, 12, 14, 53, 65, 52]
	test_string = "37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 112 20 26 30 93 96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 92 45 75 116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 89 51 19 3"
	test_array = test_string.split()
	#test_array = [37, 23, 108, 59, 55, 86, 64, 94, 65, 14, 105, 17, 111, 115]
	#test_array = [99, 60, 155, 41, 73, 81, 85, 86, 87, 80, 79, 78, 77, 40]
	#test_array = [1, 2, 5, 3, 6, 4]
	#test_array = [39, 28, 51, 13, 7, 26, 37, 30, 38, 46, 60, 47, 48, 49]
	#test_array = [1, 2, 3, 4, 5, 6]
	for element in test_array:
		my_tree.create(element)

	result = top_view(my_tree.root)
	topView(my_tree)
	#for key, value in result.items():
	#	print(key, value)