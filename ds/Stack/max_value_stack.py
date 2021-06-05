#! /usr/bin/env python3

"""
Create an auxiliary stack, say ‘trackStack’ to keep the track of maximum element
Push the first element to both mainStack and the trackStack.
Now from the second element, push the element to the main stack. Compare the element with the top element of the track stack, if the current element is greater than the top of trackStack then push the current element to trackStack otherwise push the top element of trackStack again into it.
If we pop an element from the main stack, then pop an element from the trackStack as well.
Now to compute the maximum of the main stack at any point, we can simply print the top element of Track stack.
"""

    
class maxStack:

    def __init__(self):

        self.mainStack = []
        self.trackStack = []

    def push(self, element):

        self.mainStack.append(element)

        if len(self.mainStack) == 1:
            self.trackStack.append(element)

        if element > self.trackStack[-1]:
            self.trackStack.append(element)
        else:
            self.trackStack.append(self.trackStack[-1])

    def get_max(self):
        return self.trackStack[-1]

    def pop(self):
        self.mainStack.pop()
        self.trackStack.pop()


