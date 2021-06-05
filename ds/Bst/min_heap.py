#! /usr/bin/env python3

class MinHeap:

    def __init__(self):
        self.heap_list = [None]
        self.count = 0 

    def add(self, element):
        print("adding {} to self.heap_list".format(element))
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Restoring heap property ... ")

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    

if __name__ == "__main__":
    heap = MinHeap()
    print(heap.heap_list)
