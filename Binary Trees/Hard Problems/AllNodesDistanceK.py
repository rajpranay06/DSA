'''

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findParent(self, root, parentMap):
        queue = []
        queue.append(root)
        while queue:
            curr = queue.pop(0)
            if curr.left:
                queue.append(curr.left)
                # Setting the parent node to left child
                parentMap[curr.left] = curr
            if curr.right:
                queue.append(curr.right)
                # Setting the parent node to right child
                parentMap[curr.right] = curr
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Set parent nodes to each node, inorder to move upwards
        parentMap = {}
        parentMap[root] = None
        self.findParent(root, parentMap)
        
        # A visited map, to store visited nodes, inorder to not traverse them again
        visited = defaultdict(lambda: False)
        # Queue to traverse nodes in the given traget node path
        queue = []
        queue.append(target)
        visited[target] = True
        currLevel = 0  # To store level
        while queue:
            size = len(queue)
            if currLevel == k:
                break  # We will have the output values in queue, no need to traverse anymore
            for i in range(size):
                curr = queue.pop(0)
                # If left and left is not visisted push into queue
                if curr.left and not visited[curr.left]:
                    queue.append(curr.left)
                    visited[curr.left] = True
                # If right and right is not visisted push into queue
                if curr.right and not visited[curr.right]:
                    queue.append(curr.right)
                    visited[curr.right] = True
                # Go to parent, if parent not visited add into queue
                if parentMap[curr] and not visited[parentMap[curr]]:
                    queue.append(parentMap[curr])
                    visited[parentMap[curr]] = True
                    
            currLevel += 1
        
        # Add the nodes in queue into res, as the level is matched with k
        res = []
        for node in queue:
            res.append(node.val)
        return res

'''

Time Complexity - O(N) + O(N) -> For finding parent and traversing upto k level nodes.
Space Complexity - O(N) + O(N) + O(N) -> for parent and visisted map, and for queue.

'''
