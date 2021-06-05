#! /usr/bin/env python3


class Node:
    
    def __init__(self, data, next_node=None):
        self.next_node = next_node
        self.data = data
        
    def set_next_node(self, node):
        self.next_node = node
        
    def get_next_node(self):
        return self.next_node
    
    def get_data(self):
        return self.data
    
    
class Queue:
    
    def __init__(self):
        
        self.top = None
        self.bottom = None
        
    def enqueu(self, some_data):
        
        node_to_add = Node(some_data)
        
        if not self.top:
            self.top = self.bottom = node_to_add
            return
        
        self.bottom.set_next_node(node_to_add)
        self.bottom = node_to_add

            
        
        
    def dequeue(self):
        
        if not self.top:
            return
        
        if self.top.get_next_node() is None:
            self.top = None
            return
        
        new_head = self.top.get_next_node()
        self.top = new_head
        
        
    def peek(self):
        
        if self.top:
            return self.top.get_data()
        else:
            return
        
            

    
new_queue = Queue()
new_queue.enqueu(42)
new_queue.dequeue()
new_queue.enqueu(14)
print(new_queue.peek())
new_queue.enqueu(28)
print(new_queue.peek())
new_queue.enqueu(60)
new_queue.enqueu(78)
new_queue.dequeue()
new_queue.dequeue()

