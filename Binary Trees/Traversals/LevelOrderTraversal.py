'''

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return None
        q = [root]
        res.append([root.val])
        while q:
            ans = []
            k = len(q)
            
            # Run a loop for each level, based on queue length
            for i in range(k):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    ans.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    ans.append(node.right.val)
                    
            if ans:
                res.append(ans)
            
        return res


'''

Time Complexity: O(N)

Space Complexity: O(N)

'''
