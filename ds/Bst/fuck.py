from collections import deque

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Function to perform vertical traversal on a given binary tree
def printVertical(root):
 
    # base case
    if root is None:
        return
 
    # create a dictionary to store the vertical order of binary tree nodes
    dict = {}
 
    # create an empty queue for level order traversal.
    # `It` stores binary tree nodes and their horizontal distance from the root.
    q = deque()
 
    # enqueue root node with horizontal distance as 0
    q.append((root, 0))
 
    # loop till queue is empty
    while q:
 
        # dequeue front node
        node, dist = q.popleft()
 
        # insert front node value into the dictionary using its horizontal distance
        # as the key
        dict.setdefault(dist, []).append(node.key)
 
        # enqueue non-empty left and right child of the front node
        # with their corresponding horizontal distance
        if node.left:
            q.append((node.left, dist - 1))
 
        if node.right:
            q.append((node.right, dist + 1))
 
    # print the dictionary
    for key in sorted(dict.keys()):
        print(dict.get(key))
 
 
if __name__ == '__main__':
 
    ''' Construct the following tree
            1
          /   \
         /     \
        2       3
              /   \
             /     \
            5       6
          /   \
         /     \
        7       8
              /   \
             /     \
            9      10
    '''
 
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(5)
    root.right.right.left = Node(3)
    root.right.right.right = Node(6)
    root.right.right.left.right = Node(4)
 
    printVertical(root)