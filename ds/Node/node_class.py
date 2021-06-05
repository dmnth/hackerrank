#! /usr/bin/env python3

class Node:

    def __init__(self, value, next_node=None, prev_node=None):
        
        self.next_node = next_node
        self.prev_node = prev_node
        self.value = value

    def set_next_node(self, node):
        self.next_node = node

    def set_prev_node(self, node):
        self.prev_node = node

    def get_next_node(self):
        return self.next_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value

if __name__ == "__main__":
    new_node = Node('boris')
    print(new_node.get_next_node())
