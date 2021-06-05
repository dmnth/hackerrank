#! /usr/bin/env python3

from node_class import Node

class DoublyLinkedList:

    def __init__(self):
        
        self.head_node = None
        self.tail_node = None


    def get_head_node(self):
        return self.head_node

    def get_tail_node(self):
        return self.tail_node

    def printout(self):
        
        strng = ''

        current_node = self.head_node
        index = 0
        while current_node:
            strng += str(index) + ': ' + str(current_node.get_value()) + '\n'
            index += 1
            current_node = current_node.get_next_node()

        return strng

    # Insert value at back:
    def push(self, data):

        new_node = Node(data)

        if not self.tail_node:

            self.tail_node = new_node
            self.head_node = new_node
            return
        
        self.tail_node.set_next_node(new_node)
        new_node.set_prev_node(self.tail_node)
        self.tail_node = new_node

    # remove value at back
    def pop(self):

        if not self.tail_node.get_prev_node():
            self.tail_node = None
            self.head_node = None
            return

        prev = self.tail_node.get_prev_node()
        prev.set_next_node(None)
        self.tail_node = prev

        


    # remove value at front
    def shift(self):

        new_head = self.head_node.get_next_node()
        self.head_node.set_next_node(None)
        self.head_node = new_head

    # Insert value at front
    def unshift(self, value):

        new_value = Node(value)

        if not self.head_node:

            self.head_node = new_value
            self.tail_node = new_value
            return
        
        new_value.set_next_node(self.head_node)
        self.head_node = new_value
        
    
if __name__ == "__main__":

    new_list = DoublyLinkedList()
    new_list.push(10)
    new_list.push(20)
    new_list.shift()
    new_list.shift()
    new_list.shift()
    print(new_list.printout())

