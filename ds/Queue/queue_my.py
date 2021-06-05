#! /usr/bin/env python3

class Node:

    def __init__(self, value, next_node=None):
        
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node


class Queue:

    def __init__(self):
        
        self.head = None
        self.tail = None

    def enqueue(self, value):

        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        if self.head.get_next_node() is None:
            self.tail = new_node
            self.head.set_next_node(new_node)
            return

        # insert at tail
        current_node = self.head

        while current_node.get_next_node().get_next_node():
            current_node = current_node.get_next_node()

        current_node.get_next_node().set_next_node(new_node)
        new_node.set_next_node(None)

    def dequeue(self):
        # removes from head 
        if not self.head:
            print("Nothing left")
            return

        
        if not self.head.get_next_node():
            node_to_remove = self.head.get_value()
            self.head = None
            self.tail = None
            return node_to_remove
        node_to_remove = self.head

        new_head = self.head.get_next_node()
        self.head = new_head

        return node_to_remove.get_value()

    def peek(self):

        if self.head:
            return self.head.get_value()
        else:
            print('is empty') 




