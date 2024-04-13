'''

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. 
There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

Approach:

Intuition
We can assign a vertical and level to every node. This will help us in categorising nodes based on their position in the binary tree. 
Vertical Coordinates (x): The vertical coordinate, denoted as 'x', represents the vertical column in the tree. It essentially signifies the horizontal position of a node in relation to its parent. 
Nodes with the same 'x' value are aligned vertically, forming a column. Level Coordinates (y): The level coordinate, denoted as 'y', represents the depth or level of a node in the tree. 
It signifies the vertical position of a node within the hierarchy of levels. As we traverse down the tree, the 'y' value increases, indicating a deeper level.

We create a map that serves as our organisational structure. The map is based on the vertical and level information of each node. 
The vertical information, represented by 'x', signifies the vertical column, while the level information, denoted as 'y', acts as the key within the nested map. 
This nested map utilises a multiset to ensure that node values are stored in a unique and sorted order. With our map structure in place, we initiate a level order BFS traversal using a queue. 
Each element in the queue is a pair containing the current node and its corresponding vertical and level coordinates. Starting with the root node, we enqueue it with initial vertical and level values (0, 0). 
During traversal, for each dequeued node, we update the map by inserting the node value at its corresponding coordinates and enqueue its left and right children with adjusted vertical and level information. 
When traversing to the left child, the vertical value decreases by 1 and the level increases by 1, while traversal to the right child leads to an increase in both vertical and level by 1.

After completing the BFS traversal, we prepare the final result vector. We iterate through the map, creating a column vector for each vertical column. 
This involves gathering node values from the multiset and inserting them into the column vector. 
These column vectors are then added to the final result vector, resulting in a 2D representation of the vertical order traversal of the binary tree.


Complexity Analysis

Time Complexity: O(N * log2N * log2N * log2N) where N represents the number of nodes in the Binary Tree.

Postorder Traversal performed using BFS as a time complexity of O(N) as we are visiting each and every node once.
Multiset Operations to insert overlapping nodes at a specific vertical and horizontal level also takes O(log2N) complexity.
Map operations involve insertion and retrieval of nodes with their vertical and level as their keys. Since there are two nested maps, the total time complexity becomes O(log2N)*O(log2N).

Space Complexity: O(N + N/2) where N represents the number of nodes in the Binary Tree.

The map for storing nodes based on their vertical and level information occupies an additional space complexity of O(N) as it stores all N nodes of the Binary Tree.
The queue for breadth first traversal occupies a space proportional to the maximum level of the tree which can be O(N/2) in the worst case of a balanced tree.

'''

# Code 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Map for storing node values acc to their vertical and level index
        nodesMap = defaultdict(lambda: defaultdict(lambda: list()))

        # Inserting node, verticalIndex and Level Index into queue
        queue = deque([(root, (0, 0))])

        while queue:
            # Pop the queue
            node, (x,y) = queue.popleft()

            # Set the node val to its corresponding vertical and level index
            nodesMap[x][y].append(node.val)

            # Go to left node, -1 vertical index +1 level index
            if node.left:
                queue.append((node.left, (x-1, y+1)))
            # Go to right node, +1 vertical index +1 level index
            if node.right:
                queue.append((node.right, (x+1, y+1)))
        
        # Sort the dictonary to get nodes from left side
        nodesMap = dict(sorted(nodesMap.items()))
        res = []
        for verticalIndex, y_vals in nodesMap.items():
            col = []
            for levelIndex, nodeVal in y_vals.items():
                # Add all the nodes of the particular level into col, need to be sorted
                col.extend(sorted(nodeVal))
            # Add the values to res
            res.append(col)
        
        return res


# Code 2

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: 
            return

        res = defaultdict(list)
        # Inserting node, verticalIndex and Level Index into queue
        q = deque([(0, 0, root)])
        l = []
        while q:
            # Pop the queue
            col, row, node = q.popleft()
            
            # Set the node val to its corresponding vertical and level index
            l.append((col, row, node.val))

            # Go to left node, -1 vertical index +1 level index
            if node.left: 
                q.append((col-1, row+1, node.left))
            
            # Go to right node, +1 vertical index +1 level index
            if node.right: 
                q.append((col+1, row+1, node.right))

        for col, row, node in sorted(l):
            # Append the node vals to its vertical index
            res[col].append(node)
        
        return res.values()


        
