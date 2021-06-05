#! /usr/bin/env python3

class Node:

    def __init__(self, data, next_node=None):
        
        self.data = data
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_data(self):
        return self.data

class maxStack:

    def __init__(self):

        self.top = None
    
    def push(self, value):

        new_node = Node(value)

        if self.top is None:
            self.top = new_node
            return

        new_node.set_next_node(self.top)
        self.top = new_node

    def pop(self):

        if not self.top:
            return None

        value_to_return = self.top.get_data()
        self.top = self.top.get_next_node()

        return value_to_return


    def peek(self):
        return self.top.get_data()

    def traverse_stack(self):
        current_node = self.top
        max_value = self.top.get_data()
        while current_node:
            if current_node.get_data() > max_value:
                max_value = current_node.get_data()
            current_node = current_node.get_next_node()
        return max_value

if __name__ == "__main__":
    new_stack = maxStack()
    new_stack.push(2)
    new_stack.push(23)
    new_stack.push(1)
    new_stack.push(10)
    new_stack.push(-1)
    new_stack.push(59)
    print(new_stack.peek())
    print(new_stack.traverse_stack())
    new_stack.pop()
    print(new_stack.traverse_stack())
