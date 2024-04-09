'''

Problem statement

You are given a binary tree having 'n' nodes.
The boundary nodes of a binary tree include the nodes from the left and right boundaries and the leaf nodes, each node considered once.
Figure out the boundary nodes of this binary tree in an Anti-Clockwise direction starting from the root node.

Example 1:

Input:Binary Tree: 1 2 7 3 -1 -1 8 -1 4 9 -1 5 6 10 11
Output: Boundary Traversal: [1, 2, 3, 4, 5, 6, 10, 11, 9, 8, 7]

Explanation: The boundary traversal of a binary tree involves visiting its boundary nodes in an anticlockwise direction:
				
Starting from the root, we traverse from: 1
The left side traversal includes the nodes: 2, 3, 4
The bottom traversal include the leaf nodes: 5, 6, 10, 11
The right side traversal includes the nodes: 9, 8, 7
We return to the  root and the boundary traversal is complete.

Intuition

The boundary traversal algorithm should be divided into three main parts traversed in the anti-clockwise direction:

Left Boundary: Traverse the left boundary of the tree. Start from the root and keep moving to the left child; if unavailable, move to the right child. Continue this until we reach a leaf node.

Bottom Boundary: Traverse the bottom boundary of the tree by traversing the leaf nodes using a simple preorder traversal. 
We check if the current node is a lead, and if so, its value is added to the boundary traversal array.

Right Boundary: The right boundary is traversed in the reverse direction, similar to the left boundary traversal starting from the root node and keep moving to the right child; 
if unavailable, move to the left child. Nodes that are not leaves are pushed into the right boundary array from end to start to ensure that they are added in the reverse direction.


Complexity Analysis

Time Complexity: O(N) where N is the number of nodes in the Binary Tree.
Adding the left boundary of the Binary Tree results in the traversal of the left side of the tree which is proportional to the the height of the three hence O(H) ie. O(log2N). 
In the worst case that the tree is skewed the complexity would be O(N).
For the bottom traversal of the Binary Tree, traversing the leaves is proportional to O(N) as preorder traversal visits every node once.
Adding the right boundary of the Binary Tree results in the traversal of the right side of the tree which is proportional to the the height of the three hence O(H) ie. O(log2N). 
In the worst case that the tree is skewed the complexity would be O(N).
Since all these operations are performed sequentially, the overall time complexity is dominated by the most expensive operation, which is O(N).

Space Complexity: O(N) where N is the number of nodes in the Binary Tree to store the boundary nodes of the tree. O(H) or O(log2N) Recursive stack space while traversing the tree. 
In the worst case scenario the tree is skewed and the auxiliary recursion stack space would be stacked up to the maximum depth of the tree, resulting in an O(N) auxiliary space complexity.

'''


# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def isLeaf(node):
    if node.left or node.right:
        return False
    return True  

def addLeft(node, res):
    curr = node.left
    while(curr):
        # Add the node if it is not leaf
        if not isLeaf(curr):
            res.append(curr.data)
        # Go to left child
        if curr.left:
            curr = curr.left
        # If no left go to right
        else:
            curr = curr.right

def addLeaves(node, res):
    # Add node if it is leaf
    if isLeaf(node):
        res.append(node.data)
    
    # Left traverse
    if node.left:
        addLeaves(node.left, res)
        # Right traverse
    if node.right:
        addLeaves(node.right, res)

def addRight(node, res):
    curr = node.right
    # We are using temp array, we need nodes in reverse order
    temp = []
    while(curr):
        # Add node if it is not leaf
        if not isLeaf(curr):
            temp.append(curr.data)
        # Go to right
        if curr.right:
            curr = curr.right
        # If no right, go to left
        else:
            curr = curr.left
    # Add temp array in reverse order to res
    res += temp[::-1]

# Functions to traverse on each part.
def traverseBoundary(root):
    # Write your code here.
    res = []
    if not root:
        return res
    # Add to res if root is not leaf node
    if not isLeaf(root):
        res.append(root.data)
    
    # First add the all the left nodes 
    addLeft(root, res)
    # Add the leaf nodes using preorder traversal
    addLeaves(root, res)
    # Add all the right nodes
    addRight(root, res)

    return res



