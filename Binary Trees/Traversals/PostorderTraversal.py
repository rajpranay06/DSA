'''

Solution - Recursive:

Approach: In postorder traversal, the tree is traversed in this way: left, right, root.

The algorithm approach can be stated as:

We first recursively visit the left child and go on left till we find a node pointing to NULL.
Then we return to its parent.
Then we recursively visit the right child.
After we have returned from the right child as well, only then will we print the  current node value.

Time Complexity: O(N).
Reason: We are traversing N nodes and every node is visited exactly once.

Space Complexity: O(N)
Reason: Space is needed for the recursion stack. In the worst case (skewed tree), space complexity can be O(N).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def postorder(node):
            if not node:
                return
            
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)
        
        postorder(root)
        return res


'''

Iterative Solution

Intuition: In postorder traversal, the tree is traversed in this way: left, right, root. We first visit the left child, after returning from it we visit the right child, 
and after returning from both of them, we print the value of the current node. 
The fundamental problem we face in this scenario is that there is no way that we can move from a child to the parent using as our node points to only children and not to the parent. 
To solve this problem, we use an explicit stack data structure. While traversing we can insert node values to the stack in such a way that we always get the next node value at the top of the stack.

Solution 1: Using two stacks

Approach: 
The algorithm approach can be stated as:

We take two explicit stacks S1 and S2.
We insert our node to S1(if it’s not pointing to NULL).
We will set up a while loop to run till S1 is non-empty.
In every iteration, we pop out the top of S1 and then push this popped node to S2. Moreover we will push the left child and right child of this popped node to S1.(If they are not pointing to NULL).
Then we start the next iteration with the next node as top of S1.
We stop the iteration when S1 becomes empty.
At last we start popping at the top of S2 and print the node values, we will get the postorder traversal.

Time Complexity: O(N).
Reason: We are traversing N nodes and every node is visited exactly once.

Space Complexity: O(N+N)

'''

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if not root:
            return None
        st1 = [root]
        st2 = []

        while st1:

            # Pop the node and add it to stack 2
            node = st1.pop()
            st2.append(node)

            # Add node childs to stack 1
            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)
        
        # Stack 2 will have the postorder traversal 
        while st2:
            res.append(st2.pop().val)
        return res


'''

Solution 2: Using a single stack:

Intuition: First we need to understand what we do in a postorder traversal. We first explore the left side of the root node and keep on moving left until we encounter a node pointing to NULL. 
As now there is nothing more to traverse on the left, we move to the immediate parent(say node P) of that NULL node. Now we again start our left exploration from the right child of that node P. 
We will print a node’s value only when we have returned from its both children.

Time Complexity: O(N)
Space Complexity: O(N)

'''

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if not root:
            return None
        st = []

        while st or root:
            # Add all the left childs into stack
            if root:
                st.append(root)
                root = root.left
            else:
                # If no left childs are present add right child of top node of stack
                temp = st[-1].right
                if not temp:
                    # If there is no right child, pop the node add to res
                    temp = st.pop()
                    res.append(temp.val)
                    # Check for other childs of top nodes of the stack
                    while st and temp == st[-1].right:
                        # If temp is the right child of top node, pop it and add to res
                        temp = st.pop()
                        res.append(temp.val)
                else:
                    root = temp

        return res

