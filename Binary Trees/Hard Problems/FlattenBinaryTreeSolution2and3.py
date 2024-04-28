'''

Solution 2: Iterative Approach - Using Stack

Intuition:

In a binary tree, generally, we need to set the right child of the node to the left and the left child to NULL. If the given tree is a left-skewed tree, this action alone will flatten the binary tree.

Now the main question arises is what if the current node doesn’t have a left child? In that case, we don’t want to assign its right child to NULL( its left child), 
rather we want it to assign to itself so that our preorder sequence is maintained. In case the right child is also not present(a leaf node) we would want to assign the right child to some parent node’s right child.

To get to this parent’s right node we will use a stack. Whenever we are at a node we want to prioritize its left child if it is present. If it is not present we want to look at the right child. 
A stack is a LIFO data structure, we first push the right child and then the left child. Then we set the right child of the node to the stack’s top and left child as NULL. 
This way the stack always provides the correct next node.

Approach:

The algorithm approach can be stated as:

Take a stack and push the root node to it.
Set a while loop till the stack is non-empty.
In every iteration, take the node at the top of the stack( say cur) and pop the stack.
If cur has a right child, push it to the stack.
If cur has a left child, push it to the stack.
Set the right child of cur to node at stack’s top.
Set the left child of cur as NULL.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
           
        st = [root]

        while st:
            curr = st.pop()
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
            
            if st:
                # Set top element of stack to curr right
                curr.right = st[-1]
            curr.left = None

'''

Time Complexity: O(N)
Reason: The loop will execute for every node once.

Space Complexity: O(N)

'''

'''

Solution 3 - Using Intuition behind Morris Traversal.

Pre- req: Morris Traversal

Intuition: 

We will use the intuition behind morris's traversal. In Morris Traversal we use the concept of a threaded binary tree.
If we set the right child of every node like this(marked in red) and the left child as NULL, our job will be done.

Approach:

The algorithm can be described as:

At a node(say cur) if there exists a left child, we will find the rightmost node in the left subtree(say prev).
We will set prev’s right child to cur’s right child,
We will then set cur’s right child to it’s left child.
We will then move cur to the next node by assigning cur it to its right child
We will stop the execution when cur points to NULL.

'''

class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
           
        curr = root

        while curr:
            if curr.left:
                prev = curr.left

                # Go to right most node from left sub-tree
                while prev.right:
                    prev = prev.right
                
                # Set right most node right to curr right
                prev.right = curr.right
                # Set curr right to curr left
                curr.right = curr.left
                curr.left = None
        
            curr = curr.right

'''

Time Complexity: O(N)
Reason: Time complexity will be the same as that of a morris traversal

Space Complexity: O(1)
Reason: We are not using any extra space.
        
'''
