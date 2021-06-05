#! /usr/bin/env python3

import random

class Node:
    
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

class LinkedList:

    def __init__(self):
        self.head_node = None

    def get_head_node(self):
        return self.head_node

    def remove_at_front(self):
        next_node = self.head_node.get_next_node()
        self.head_node.set_next_node(None)
        self.head_node = next_node

    def remove_at_tail(self):
        
        current_node = self.head_node

        if self.head_node.get_next_node() is None:
            self.head_node = None
            return

        while current_node.get_next_node().get_next_node():
            current_node = current_node.get_next_node()
        
        node_to_remove = current_node.get_next_node()
        current_node.set_next_node(None)

        return node_to_remove.get_data()


    def insert_beginning(self, new_value):

        new_node = Node(new_value)

        if self.head_node == None:
            self.head_node = new_node

        else:
            new_node.set_next_node(self.head_node)
            self.head_node = new_node

    def traverse_und_print(self):
        
        current_node = self.head_node
        index = 0
        strng = '' 

        while current_node:
            strng += str(index) + ': ' + str(current_node.get_data()) + '\n'
            index += 1
            current_node = current_node.get_next_node()

        return strng 

    def print_in_reverse(self):

        current_node = self.head_node

        if self.head_node.get_next_node() == None:
            print(self.head_node.get_data())
            return 

        while current_node.get_next_node().get_next_node():
            current_node = current_node.get_next_node()

        new_head = current_node.get_next_node()
        new_tail = current_node
        print(new_head.data)

        new_tail.set_next_node(None)
        
        self.print_in_reverse()

        return 

    def remove_node_by_index(self, searched_index):

        # Assign current nod
        current_node = self.head_node
        current_index = 0

        # Mistake. Was current_index == searched_index
        # Forgot to return needed value. That's why code didnt work in first place.
        if searched_index == 0: 
            print('Zero index matches: ',current_node.data)
            self.head_node = self.head_node.get_next_node()
            return self.head_node

        # Look for node ahead of searched
        while current_index != searched_index - 1:
            print(current_index, ': ', current_node.get_data())
            current_index += 1
            current_node = current_node.get_next_node()
        
        
        # Capture in new variable
        current_node.set_next_node(current_node.get_next_node().get_next_node())
        current_index -= 1

        if not self.head_node:
            return None
        else:
            return self.head_node 


    def reverse_list(self):

        current_node = self.head_node
        previous = None

        while current_node:
            next_node = current_node.get_next_node()
            current_node.set_next_node(previous)
            previous = current_node
            current_node = next_node 
        
        self.head_node = previous
    
        return previous 

    def sort_list(self):

        previous = None
        current_node = self.head_node
        next_node = current_node.get_next_node()

        # elements to be swapped are current node and next node
        # if current > next
        if self.head_node is None:
            self.head_node = current_node

        while current_node != None:

            if current_node.get_data() > next_node.get_data():
                current_node.set_next_node(next_node.get_next_node())
                previous.set_next_node(next_node)
                next_node.set_next_node(current_node)
                previous = current_node
                current_node = current_node.get_next_node()
                next_node = current_node.get_next_node()
            else:
                previous = current_node
                current_node = current_node.get_next_node()
                next_node = current_node.get_next_node()

    def single_sorted_insert(self, data):
        
        node_to_insert = Node(data)
        # Check if node is not on list:


        if self.head_node is None:
            self.head_node = node_to_insert
            return

        if node_to_insert.get_data() < self.head_node.get_data(): 
            node_to_insert.set_next_node(self.head_node)
            self.head_node = node_to_insert
            return
        
        # Handle insertions at tail
        current_node = self.head_node

        while current_node.get_next_node():

            if node_to_insert.data == current_node.data:
                return

            if node_to_insert.get_data() < current_node.get_next_node().get_data():
                node_to_insert.set_next_node(current_node.get_next_node())
                current_node.set_next_node(node_to_insert)
                return 

            current_node = current_node.get_next_node()

        if node_to_insert.get_data() > current_node.get_data():
            current_node.set_next_node(node_to_insert)
            node_to_insert.set_next_node(None)


if __name__ == '__main__':

    new_node = Node('a')
    other_node = Node('b')

    new_node.set_next_node(other_node)


    new_list = LinkedList()
    new_list.single_sorted_insert(1)
    new_list.single_sorted_insert(2)
    new_list.single_sorted_insert(2)
    new_list.single_sorted_insert(2)
    new_list.single_sorted_insert(3)
    new_list.single_sorted_insert(3)
    new_list.single_sorted_insert(4)
    new_list.single_sorted_insert(4)
    new_list.single_sorted_insert(4)
    new_list.single_sorted_insert(5)
    new_list.single_sorted_insert(5)
    print(new_list.traverse_und_print())
