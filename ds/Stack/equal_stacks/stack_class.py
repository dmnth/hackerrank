#! /usr/bin/env python3

from node_class import Node

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True

    def push(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.top = new_node
            self.size += 1
            return

        new_node.set_next_node(self.top)
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return

        value_to_remove = self.top
        self.top = value_to_remove.get_next_node()
        self.size -= 1

        print(value_to_remove.get_value())

    def peek(self):
        print(self.top.get_value())
        return

if __name__ == "__main__":

    new_stack = Stack()
    new_stack.push('H1')
    new_stack.push('h2')
    new_stack.push('h3')
    new_stack.peek()
    new_stack.pop()
    new_stack.peek()
