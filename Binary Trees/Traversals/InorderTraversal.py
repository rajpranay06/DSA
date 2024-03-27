'''

Solution - Iterative:
Intuition: In inorder traversal, the tree is traversed in this way: left, root, right. We first visit the left child, after returning from it we print the current node value, then we visit the right child. 
The fundamental problem we face in this scenario is that there is no way that we can move from a child to a parent. To solve this problem, we use an explicit stack data structure. 
While traversing we can insert node values to the stack in such a way that we always get the next node value at the top of the stack.

Time Complexity: O(N).
Reason: We are traversing N nodes and every node is visited exactly once.

Space Complexity: O(N)
Reason: In the worst case (a tree with just left children), the space complexity will be O(N).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return None
        st = []

        while True:
            if root:
                # Go to the left child, until there is no left child
                st.append(root)
                root = root.left
            else:
                # If st is empty we traversed whole tree, so break
                if not st:
                    break
                
                # Else get the top element, add it to res and move to its right child
                root = st.pop()
                res.append(root.val)
                root = root.right
        
        return res


'''

Solution 2 - Recursive:
Approach: In inorder traversal, the tree is traversed in this way: left, root, right.

The algorithm approach can be stated as:

We first recursively visit the left child and go on till we find a leaf node.
Then we print that node value.
Then we recursively visit the right child.
If we encounter a node pointing to NULL, we simply return to its parent.

Time Complexity: O(N).
Reason: We are traversing N nodes and every node is visited exactly once.

Space Complexity: O(N)
Reason: Space is needed for the recursion stack. In the worst case (skewed tree), space complexity can be O(N).

'''


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res
