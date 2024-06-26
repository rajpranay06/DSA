'''

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        flag = 1
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
                # Using flag varibale to get level which need to be reversed
                if flag == 1:
                    ans = ans[::-1]
                    flag = 0
                else:
                    flag = 1
                res.append(ans)
            
        return res
