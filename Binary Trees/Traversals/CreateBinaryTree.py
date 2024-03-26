'''

Problem statement
Given an array 'arr' that contains 7 integers representing the values of nodes in a binary tree. This represents level order. The first element of the array represents the value of the root node.

Your objective is to construct a binary tree using the remaining 6 elements of the array, creating nodes for each of these values and return root node.


BFS approach

Approach:
This approach uses a level-order traversal approach to construct the binary tree, utilising a queue to keep track of the parent nodes whose children need to be created.

Time complexity: O(N)
Space complexity: O(N)

Where 'N' is the number of elements in the array 'arr'

'''

from collections import deque
from typing import List

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def createTree(arr: List[int]) -> Node:
    q = deque()  # Create a queue to process nodes.
    # Create the root node with the value from the first element of the array.
    root = Node(arr[0])
    q.append(root)

    i = 0

    # Construct the binary tree using the remaining elements of the array.
    while q and i < 3:
        t = q.popleft()

        # Create the left child node with the value from the corresponding index in the array.
        left = Node(arr[2 * i + 1])
        t.left = left
        q.append(left)

        # Create the right child node with the value from the corresponding index in the array.
        right = Node(arr[2 * i + 2])
        t.right = right
        q.append(right)
        i += 1

    return root
