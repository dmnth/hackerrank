#! /usr/bin/env python3 

class Node:

    def __init__(self, value, next_node=None, prev_node=None):
        
        self.value = value
        self.prev_node = None
        self.next_node = None

    def set_next_node(self, next_node):

        self.next_node = next_node

    def set_prev_node(self, previous_node):
        
        self.prev_node = previous_node

    def get_next_node(self):

        return self.next_node

    def get_prev_node(self):

        return self.prev_node

    def get_data(self):
        return self.value


class DoublyLinkedList:

    def __init__(self):

        self.head_node = None
        self.tail_node = None

    def get_head_node(self):
        return self.head_node

    def get_tail_node(self):
        return self.tail_node

    def insert_to_head(self, new_value):

        new_node = Node(new_value)

        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
            return

        if self.head_node is not None:

            new_node.set_next_node(self.head_node)
            self.head_node.set_prev_node(new_node)
            new_node.set_prev_node(None)


        self.head_node = new_node

        return self.head_node

    def insert_at_tail(self, value):

        new_tail = Node(value)
        new_tail.set_next_node(None)

        # Why did u decided to end method here, inserting a RETURN
        # after conditional
        
        if self.tail_node is None and self.head_node is None:

            self.head_node = new_tail
            self.tail_node = new_tail
            return
            
        if self.tail_node is not None:

            self.tail_node.set_next_node(new_tail)
            new_tail.set_prev_node(self.tail_node)
            new_tail.set_next_node(None)

        self.tail_node = new_tail

        return self.tail_node

    def stringify_list(self):

        strng = ''

        current_node = self.head_node

        while current_node:
            strng += str(current_node.get_data()) + "\n"
            current_node = current_node.get_next_node()
        
        return strng

    def remove_head(self):

        if self.head_node is not None:

            self.head_node = self.head_node.get_next_node()
            self.head_node.set_prev_node(None)

        return

    def remove_tail(self):

        if self.tail_node is not None:

            self.tail_node = self.tail_node.get_prev_node()
            self.tail_node.set_next_node(None)

        return


    def find_and_remove(self, value):

        current_node = self.head_node
        data_to_remove = value

        if self.head_node.get_data() == data_to_remove:
            self.remove_head()

        elif self.tail_node.get_data() == data_to_remove:
            self.remove_tail

        else:

            while current_node:

                if current_node.get_data() == data_to_remove:

                    previous_node = current_node.get_prev_node()
                    next_node = current_node.get_next_node()
                    previous_node.set_next_node(next_node)
                    next_node.set_prev_node(previous_node)
                    break

                current_node = current_node.get_next_node()
                
            if current_node is not None:
                print(current_node.get_data(), ' is TERMINATED.')

            else:
                print('Not found')

        return

    def sorted_insert(self, data):
        
        current_node = self.head_node

        node_to_insert = Node(data)

        if self.head_node is None:
            self.head_node = node_to_insert
            self.tail_node = node_to_insert
            return

        current_node = self.head_node

        if self.head_node.get_data() > node_to_insert.get_data():
            node_to_insert.set_next_node(self.head_node)
            self.head_node = node_to_insert 
            return

        if self.tail_node.get_data() < node_to_insert.get_data():
            self.tail_node.set_next_node(node_to_insert)
            node_to_insert.set_next_node(None)
            node_to_insert.set_prev_node(self.tail_node)
            self.tail_node = node_to_insert 
            return
        
        # Handle insertion at the middle of list

        current_node = self.head_node
        while current_node.get_data() <= node_to_insert.get_data():
            current_node = current_node.get_next_node()

        previous_node = current_node.get_prev_node()
        previous_node.set_next_node(node_to_insert)
        node_to_insert.set_prev_node(previous_node)
        node_to_insert.set_next_node(current_node)

        print('current: ', current_node.get_data())
        print('prev: ', current_node.get_prev_node().get_data())
        return 



                    

if __name__ == "__main__":

    sorted_list = DoublyLinkedList()
    input_list = [1, 3, 4, 10]
    for element in input_list:
        sorted_list.sorted_insert(element)
    sorted_list.sorted_insert(5)
    print(sorted_list.stringify_list())
    



