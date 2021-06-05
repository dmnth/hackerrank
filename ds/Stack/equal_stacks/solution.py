#! /usr/bin/env python3

# First try to equalize two small stacks

class Equalizer:

    def __init__(self, stack_1, stack_2, stack_3):

        self.stack_list = [stack_1, stack_2, stack_3]
        self.stack_heights = [sum(stack) for stack in self.stack_list]

    def get_index_of_largest_stack(self):

        largest_element_index = 0

        for index in range(len(self.stack_list)):
            if self.stack_list[index] > self.stack_list[largest_element_index]:
                largest_element_index = index

        return largest_element_index

    def get_largest_stack(self):
        return max(self.stack_heights)
    
    def pop_from_largest_stack(self, largest_stack):
        print('popping from: ', largest_stack)
        return largest_stack.pop() 
    
    def equality_check(self):
        if self.stack_heights[0] == self.stack_heights[1]\
                == self.stack_heights[2]:
                    return True

    def find_difference(self):
        

    def equalize_stacks(self):

        if self.equality_check() is True:
            print("all stacks are equal")
            return sum(self.stack_list[0])

        if [] in self.stack_list:
            return 0

        

        

if __name__ == "__main__":

    h1 = [2, 1, 1]
    h2 = [3, 2]

    h3 = [1, 2, 1, 1]
    h4 = [1, 1, 2]

    h6 = [3, 2, 1, 1, 1]
    h5 = [1, 1, 4, 1]
    h = [4, 3, 2]
    
    h7 = []
    h8 = [1, 1, 3]

    h9 = []
    h10 = []
    h11 = []

    h12 = [1, 1, 2]
    h13 = [4]
    h14 = [2, 2]
    equals = Equalizer(h1, h6, h3)
    empty_equals = Equalizer(h9, h10, h11)
    equal_equals = Equalizer(h12, h13, h14)
    empty_equals.equlize_stacks()
    equal_equals.equlize_stacks()
    print(equals.stack_heights)
    print('height of stack: ', equals.get_largest_stack())
    print('index of stack: ', equals.get_index_of_largest_stack())

