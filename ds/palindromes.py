#! /usr/bin/env python3

from queue_my import Queue
from stack import Stack
from node_class import Node

class Solutions:

    def __init__(self, qu, stck):

        self.qu = qu()
        self.stk = stck()

    def pushCharacter(self, char):
        self.stk.push(char)

    def enqueueCharacter(self, char):
        self.qu.enqueue(char)

    def popCharacter(self):
        return self.stk.pop()

    def dequeuCharacter(self):
        return self.qu.dequeue()

    def peek(self):
        return self.qu.peek()

if __name__ == '__main__':

    result = Solutions(Queue, Stack)
    strng_1 = "({[[(])]})"
    strng_2 = "((((({{{[[]]}}})))))"

    for i in range(len(strng_2)):
        result.pushCharacter(strng_2[i])
        result.enqueueCharacter(strng_2[i])
    
    isPalindrome = True

    for i in range(len(strng_2) // 2):
        left_element = result.dequeuCharacter()
        right_element = result.popCharacter()
        print(left_element, right_element)
        if left_element == '(' and right_element == ')':
            pass

        elif left_element == '{' and right_element == '}':
            pass

        elif left_element == '['and right_element == ']':
            pass

        else:
            isPalindrome = False
       # while result.dequeuCharacter() != result.popCharacter():
        #if result.dequeuCharacter() != result.popCharacter():
        #   isPalindrome = False
         #   break

    if isPalindrome is True:
        print('is palindrome')
    else:
        print('is not')

