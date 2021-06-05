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


class Stack:

    def __init__(self):
        
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def push(self, value):

        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        new_node.set_next_node(self.head)
        self.head = new_node

        self.size += 1

    def pop(self):

        if not self.is_empty():
            value_to_remove = self.head.get_value() 

            if self.head.get_next_node() is None:
                self.head = None
                self.size -= 1
                return value_to_remove 

            self.head = self.head.get_next_node()

            self.size -= 1
        
            return value_to_remove

        else:
            print('Nothing to pop')


    def peek(self):
        if self.head:
            return self.head.get_value()



