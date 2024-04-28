'''

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""

        if not root:
            return ""
        
        queue = [root]
        res += str(root.val) + ","
        while queue:
            k = len(queue)
            for i in range(k):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    res += str(node.left.val) + ","
                else:
                    res += '#,'
                if node.right:
                    queue.append(node.right)
                    res += str(node.right.val) + ","
                else:
                    res += '#,'
        print(res)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        # Convert string into list
        data = data.split(",")

        index = 1
        # Root node
        root = TreeNode(int(data[0]))
        queue = [root]

        while queue:
            curr = queue.pop(0)

            if data[index] == '#':
                curr.left = None
            else:
                curr.left = TreeNode(int(data[index]))
                queue.append(curr.left)
            
            if data[index+1] == '#':
                curr.right = None
            else:
                curr.right = TreeNode(int(data[index+1]))
                queue.append(curr.right)
            
            index += 2
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

'''

Complexity Analysis

Time Complexity: O(N)

serialize function: O(N), where N is the number of nodes in the tree. This is because the function performs a level-order traversal of the tree, visiting each node once.
deserialize function: O(N), where N is the number of nodes in the tree. Similar to the serialize function, it processes each node once while reconstructing the tree.

Space Complexity: O(N)

serialize function: O(N), where N is the maximum number of nodes at any level in the tree. In the worst case, the queue can hold all nodes at the last level of the tree.
deserialize function: O(N), where N is the maximum number of nodes at any level in the tree. The queue is used to store nodes during the reconstruction process, and in the worst case, 
it may hold all nodes at the last level.

'''
