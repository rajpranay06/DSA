'''

Solution 1: Iterative

Intuition: In preorder traversal, the tree is traversed in this way: root, left, right. When we visit a node, we print its value, and then we want to visit the left child followed by the right child. 
The fundamental problem we face in this scenario is that there is no way that we can move from a child to a parent. To solve this problem, we use an explicit stack data structure. 
While traversing we can insert node values to the stack in such a way that we always get the next node value at the top of the stack.

Time Complexity: O(N).
Reason: We are traversing N nodes and every node is visited exactly once.

Space Complexity: O(N)
Reason: In the worst case, (a tree with every node having a single right child and left-subtree, follow the video attached below to see the illustration), the space complexity can be considered as O(N).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return None
        st = [root]

        while st:
            node = st.pop()
            res.append(node.val)
            
            # Stack is LIFO, so add right first and left second
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        
        return res

'''

Solution 2: Recursive

Intuition: In preorder traversal, the tree is traversed in this way: root, left, right. When we visit a node, we print its value, and then we want to visit the left child followed by the right child. 
The fundamental problem we face in this scenario is that there is no way that we can move from a child to a parent. 
To solve this problem, we use recursion and the recursive call stack to locate ourselves back to the parent node when execution at a child node is completed.

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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return res
