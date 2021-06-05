#! /usr/bin/env python3

class TreeNode:

    def __init__(self, value):
        print("initializing tree node...")
        self.value = value
        # List of children:
        self.children = []

    def add_child(self, child_node):
        print("adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("removing " + child_node.value + " from " +\
                self.value)
        self.children = [child for child in self.children if \
                child is not child_node.value]

    def traverse(self):
        print("Traversing")
        nodes_to_visit = [self]
        while len(nodes_to_visit) != 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

if __name__ == "__main__":
    seed_1 = TreeNode('Half-diamond')
    root = TreeNode('Hooks')
    seed_2 = TreeNode('Diamond')
    rake = TreeNode('worm')
    seed_3 = TreeNode('Deep_hook')
    seed_4 = TreeNode('Travelers_hook')

    seed_1.add_child(seed_3)
    seed_1.add_child(seed_4)
    root.add_child(seed_1)
    root.add_child(seed_2)
    root.add_child(rake)

    root.remove_child(rake)
    root.traverse()

    
