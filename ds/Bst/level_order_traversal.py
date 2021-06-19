# level order traversal

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def level_order_traversal(root):

	queue = [root]
	answer_string = f"{root}, "
	print(root, end = " ")
	while queue:

		print([x.info for x in queue])
		item = queue.pop(0)

		if item.left:
			print(item.left, end = " ")
			answer_string += f"{item.left}, "
			queue.append(item.left)

		if item.right:
			print(item.right ,end = " ")
			answer_string += f"{item.right}, "
			queue.append(item.right)

	return answer_string
		
		
	
if __name__ == "__main__":
	
	elements = [1, 2, 5, 3, 6, 4]
	my_tree = BinarySearchTree()

	for element in elements:
		my_tree.create(element)

	print(level_order_traversal(my_tree.root))
