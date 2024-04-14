'''

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), 
where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Approach:

Intuition:
To determine the maximum width of a tree, an effective strategy would be to assign and identify indexes for the leftmost and rightmost nodes at each level. 
Using these indexes, we can calculate the width for each level by subtracting the index of the leftmost node from that of the rightmost node.


Start by assigning an index to the root node as 0. For each level, the left child gets an index equal to 2 * parent index, and the right child gets an index equal to 2 * parent index + 1. 
Using a level order traversal, we use the leftmost and rightmost nodes at each level and using their indices, get the width at that level. Keep track of the maximum width encountered during the traversal. 
Whenever a wider level is found, update the maximum width.


Algorithm:

Step 1:Initialize a variable `ans` to store the maximum width. If the root is null, return 0 as the width of an empty tree is zero.

Step 2: Create a queue to perform level-order traversal and each element of this queue would be a pair containing a node and its vertical index. Push the root node and its position (initially 0) into the queue.

Step 3: While the queue is not empty, perform the following steps:

Get the number of nodes at the current level (size).
Get the position of the front node in the current level which is the leftmost minimum index at that level.
Initialize variables first and last to store the first and last positions of nodes in the current level.

Step 4: Backtracking: For each node in the current level:

Calculate the current position relative to the minimum position in the level.
Get the current node (node) from the front of the queue.
If this is the first node in the level, update the first variable.
If this is the last node in the level, update the last variable.
Enqueue the left child of the current node with index: 2 x current index - 1.
Enqueue the right child of the current node with index: 2 x current index + 1.

Step 5: Update the maximum width (ans) by calculating the difference between the first and last positions, and adding 1.

Step 6: Repeat the level-order traversal until all levels are processed. The final value of `ans` represents the maximum width of the binary tree, return it.


Complexity Analysis
Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. 
Processing each node takes constant time operations which contributes to the overall linear time complexity.

Space Complexity: O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree, 
the last level could at most hold N/2 nodes hence the space complexity of the queue is proportional to O(N).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0

        q = [[root, 0]]

        while q:
            mmin = q[0][1] - 1  # Using min to subtract rom indices, to stop overflowing
            n = len(q)
            first, last = None, None

            for i in range(n):
                currNode = q.pop(0)
                cur_id = currNode[1] - mmin  # To control overflowing of numbers
                node = currNode[0]

                #Get the first and last indices of the level
                if i == 0:
                    first = cur_id
                if i == n-1:
                    last = cur_id
                
                # Go to left and right nodes, set their indices by mutiplying with 2 as it is a bianry tree
                if node.left:
                    q.append([node.left, 2*cur_id + 1])
                
                if node.right:
                    q.append([node.right, 2*cur_id + 2])
            
            # Get the max width
            res = max(res, last - first + 1)

        return res
