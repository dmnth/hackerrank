#! /usr/bin/env python3

from doubly_linked_list import DoublyLinkedList, Node

def reverse_list(head):

    if head is None:
        return None

    current_node = head
    previous_node = None


    while current_node:
        next_node = current_node.get_next_node()
        if previous_node:
            previous_node.set_prev_node(current_node)
        current_node.set_next_node(previous_node)
        previous_node = current_node
        current_node = next_node
    
    head = previous_node

    return head

        
    
    head = previous_node


    return head 

if __name__ == "__main__":

    my_list = DoublyLinkedList()
    my_list.insert_to_head(5)
    my_list.sorted_insert(3)
    my_list.sorted_insert(8)
    my_list.sorted_insert(12)
    my_list.sorted_insert(0)
    print(my_list.stringify_list()) 
    head = reverse_list(my_list.head_node)
    while head:
        print(head.get_data())
        head = head.get_next_node()

