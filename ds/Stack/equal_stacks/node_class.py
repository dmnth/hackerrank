#! /usr/bin/env python3

class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

if __name__ == "__main__":

    node = Node('h1')
    node2 = Node('h2')
    node3 = Node('h3')

    node.set_next_node(node2)
    node2.set_next_node(node3)

    print(node.get_next_node().get_next_node().get_value())
