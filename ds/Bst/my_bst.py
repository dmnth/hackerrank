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

        return
    
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
    obj = tree.root.get_right_child().get_right_child()
    print(obj.get_left_child().get_value())
