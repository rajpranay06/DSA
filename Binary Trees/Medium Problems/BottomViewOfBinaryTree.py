'''

Problem Statement: Given a Binary Tree, return its Bottom View. The Bottom View of a Binary Tree is the set of nodes visible when we see the tree from the bottom.

Similar to top view, just need to return last node value of the particular column.

'''

from typing import List
from collections import defaultdict
from collections import deque

# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
    # Write your code here.
    if not root: 
        return

    res = []
    # Inserting node, verticalIndex into queue
    nodeMap = defaultdict(lambda: 0)
    q = deque([(0, root)])
    while q:
        # Pop the queue
        col, node = q.popleft()
        
        # Change the col node Val for every node, to get last nodeVal
        nodeMap[col] = node.data

        # Go to left node, -1 vertical index
        if node.left: 
            q.append((col-1, node.left))
            
        # Go to right node, +1 vertical index
        if node.right: 
            q.append((col+1, node.right))
    
    for col in sorted(nodeMap):
        # Append the node vals to res
        res.append(nodeMap[col])
        
    return res
