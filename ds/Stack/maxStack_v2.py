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

    ongoing_stack = []
    track_stack = []

    def push(self, data):
        self.ongoing_stack.append(data)

        if len(self.ongoing_stack) == 1:
            self.track_stack.append(data)
            return
        
        if int(data) >= int(self.track_stack[-1]):
            self.track_stack.append(data)
        else:
            self.track_stack.append(self.track_stack[-1])

    def pop(self):

        self.ongoing_stack.pop()
        self.track_stack.pop()

    def get_max_val(self):
        return self.track_stack[-1]

stack = maxStack()
stack.push(1)
stack.push(44)
print(stack.get_max_val())
print(stack.get_max_val())
stack.pop()
print(stack.get_max_val())
print(stack.get_max_val())
stack.push(3)
stack.push(37)
stack.pop()
print(stack.get_max_val())

"""
with open('max_stack_test_case.txt') as fuke:
    lines = fuke.readlines()
    print(lines)
    new_list = []
    for element in lines:
        new_list.append(element.strip('\n'))

for element in new_list:
    operatio = element.split()[0]
    if operatio == '1':
        new_element = element.split()[1]
        stack.push(new_element)
    if operatio == '2':
        stack.pop()
    if operatio == '3':
        print(stack.get_max_val())
"""
