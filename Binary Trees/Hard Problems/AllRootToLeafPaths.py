'''

You are given an arbitrary binary tree consisting of 'N' nodes numbered from 1 to 'N'. Your task is to print all the root to leaf paths of the binary tree.

A leaf of a binary tree is the node which does not have a left child and a right child.

Depth-First Search Approach:

We can use a depth-first approach to solve this problem since the tree is a recursive data structure.
Let us create a recursive function ‘DFS’() which takes the root of the tree and the current string curr for maintaining the current path as the parameter.
‘DFS’() traverses the binary tree and stores the root to leaf paths. When we hit a leaf node, 
we can simply store the current string in some data structure as this string represents a valid root to leaf path
Now we can return use the ‘RESULT’ list containing all the root to leaf paths in the form of strings.

Time Complexity - O(N), where ‘N’ is the number of nodes in the tree.
We traverse all the nodes of the binary tree to find the paths. Therefore, the overall time complexity will be O(N).

Space Complexity
O(N), where ‘N’ is the maximum height of a binary tree.

'''

'''
    Following is the class structure of the BinaryTreeNode class:

    class BinaryTreeNode:
        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None

'''
from typing import List

def isLeaf(root):
    return not root.left and not root.right

def getPath(root, res, s):
    if not root:
        return 
    
    # Add curr node to string 
    s += str(root.data)

    # If node is leaf add the string to res
    if isLeaf(root):
        res.append(s)
    else:
        s += " "
        getPath(root.left, res, s)
        getPath(root.right, res, s)

    
def allRootToLeaf(root) -> List[str]:
    # Write your code here.
    res = []
    if not root:
        return res
    
    s = ""
    getPath(root, res, s)
    
    return res



 

Recursive stack for storing paths can contain at most nodes of height of a binary tree which in worst can be equal to ‘N’ (skewed tree). Therefore, the overall space complexity will be O(N).
