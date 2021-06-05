#! /usr/bin/env python3

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def traverse_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class Operations:

    def __init__(self, head1, head2):

        self.head1 = head1
        self.head2 = head2

    def remove_dublicates(self)
        
if __name__ == "__main__":

    ll_1 = SinglyLinkedList()
    ll_2 = SinglyLinkedList()

    ll_1.insert_node(1)
    ll_1.insert_node(2)
    ll_1.insert_node(3)

    ll_2.insert_node(1)

    ll_1.traverse_list()
    ll_2.traverse_list()  