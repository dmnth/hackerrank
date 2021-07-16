#! /usr/bin/env python3

class Node:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right


class binaryTree:

    def __init__(self, node=None):

        self.root = node 


    def add_child(self, child):

        if self.root is None:
            self.root = child

        current = self.root

        while True:

            if current.get_value() < child.get_value():

                if current.left:
                    current = current.left
               
                else:
                    current.left = child
                    break

            if current.get_value() > child.get_value():

                if current.right:
                    current = current.right

                else:
                    current.right = child
                    break

            else:
                break
    

    def traverseTree(self):

        current = self.root
        stack = []
        level = 0
        hash_map = {level: self.root}
        """
        
            Traverse left child, if none --> switch to right child
            Proceed until stack is empty

        """
        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            elif stack:
                current = stack.pop()
                print(current.get_value())
                current = current.right 

            else:
                break

    def vertical_order_traversal(self):

        x_axis = 0
        kiu = [(x_axis, self.root)]
        hash_mape = {0: [self.root.value]}

        while kiu:

            x_distance, element = kiu.pop()

            if element.left:

                if x_distance-1 not in hash_mape.keys():
                    hash_mape[x_distance - 1] = [element.left.value]
                else:
                    hash_mape[x_distance - 1].append(element.left.value)

                kiu.append((x_distance-1, element.left))

            if element.right:

                if x_distance+1 not in hash_mape.keys():
                    hash_mape[x_distance + 1] = [element.right.value]
                else:
                    hash_mape[x_distance + 1].append(element.right.value)

                kiu.append((x_distance+1, element.right))

        return hash_mape

    def topView(self):
        # Initialize the level
        this_level = [(self.root, 0)]
        scores = {}

        while this_level:
            # Iterate over the nodes on a single level
            node, score = this_level.pop(0)
            # Skip empty nodes
            if not node:
                continue 

            # Store score if it is a new one
            if score not in scores:
                scores[score] = node.value

            # Add node children to the next level
            this_level.extend([(node.left, score-1), (node.right, score+1)])

        # Sort the scores and print their values

        for _, value in sorted(list(scores.items())):
            print(value, end = ' ')


        
if __name__ == "__main__":
    
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(5)
    node_4 = Node(6)
    node_5 = Node(4)

    tree = binaryTree(node_1)
    tree.add_child(node_2)
    tree.add_child(node_3)
    tree.add_child(node_4)
    tree.add_child(node_5)

    new_tree = binaryTree()
    sample = [39, 28, 51, 13, 37, 46, 60, 7, 26, 30, 38]

    for element in sample:
        new_tree.add_child(Node(element))

    
#    new_tree.vertical_order_traversal()
    new_tree.topView()
