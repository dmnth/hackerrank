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

    def __init__(self, node):

        self.root = node 


    def add_child(self, child):

        if self.root is None:
            self.root = child

        current = self.root

        while True:

            if child.value < current.get_value():
                if current.left is None:
                    current.left = child
                    break
                else:
                    current = current.left

            if child.value > current.get_value():
                if current.right is None:
                    current.right = child
                    break
                else:
                    current = current.right

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
                print(f"{current.value} at level {level}")
                current = current.right 

            else:
                break

    def vertical_order_traversal(self):

        x_axis = 0
        kiu = [(x_axis, self.root)]
        hash_mape = {0: [self.root.value]}

        while kiu:

            x_distance, element = kiu.pop(0)

            if element.left:

                if x_distance-1 not in hash_mape.keys():
                    hash_mape[x_distance - 1] = [element.left.value]
                else:
                    pass
                    #hash_mape[x_distance - 1].append(element.left.value)

                kiu.append((x_distance-1, element.left))

            if element.right:

                if x_distance+1 not in hash_mape.keys():
                    hash_mape[x_distance + 1] = [element.right.value]
                else:
                    pass
                    #hash_mape[x_distance + 1].append(element.right.value)

                kiu.append((x_distance+1, element.right))

        print(hash_mape)


        
if __name__ == "__main__":
    
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(5)
    node_4 = Node(6)
    node_5 = Node(4)

    print(node_1.value)
    tree = binaryTree(node_1)
    tree.add_child(node_2)
    tree.add_child(node_3)
    tree.add_child(node_4)
    tree.add_child(node_5)

    tree.traverseTree()
    tree.vertical_order_traversal()
