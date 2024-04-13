'''

Problem Statement: Given a Binary Tree, return its Top View. The Top View of a Binary Tree is the set of nodes visible when we see the tree from the top.

Similar to Vertical Traversal, need to add the first node of each vertical col to result array.

'''

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def getTopView(root):
    # Write your code here.
    if not root: 
        return

    res = []
    # Inserting node, verticalIndex into queue
    nodeMap = []
    q = deque([(0, root)])
    l = []
    while q:
        # Pop the queue
        col, node = q.popleft()
            
        # Add the nodeval to list, if col not in map
        if col not in nodeMap:
            l.append([col, node.val])
            nodeMap.append(col)

        # Go to left node, -1 vertical index
        if node.left: 
            q.append((col-1, node.left))
            
        # Go to right node, +1 vertical index
        if node.right: 
            q.append((col+1, node.right))

    for col, node in sorted(l):
        # Append the node vals to res
        res.append(node)
        
    return res

# Taking input.
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root

# Printing the tree nodes.
def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# Main.
T = 1
for i in range(T):
    root = takeInput()
    ans = getTopView(root)
    printAns(ans)
