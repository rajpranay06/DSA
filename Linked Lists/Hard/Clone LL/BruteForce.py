'''

Given a Linked list that has two pointers in each node and one of which points to the first node and the other points to any random node. Write a program to clone the LinkedList.

Input:
	head = [[1,3],[2,0],[3,null],[4,1]]
Output:
	head = [[1,3],[2,0],[3,null],[4,1]]

Approach:

Use hashMap to store node and its depe copy. Traverse the LL again and set next and random pointers to deep copy. 

Time Complexity: O(N)+O(N)

Reason: Two iterations over the entire list. Once for inserting in the map and other for linking nodes with next and random pointer.

Space Complexity: O(N)

Reason: Use of hashmap for storing entire data.

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head
        
        temp = head

        # Hashmap to store node and its deep copy
        hashMap = {}

        while temp:
            # Creating deep copy for nodes
            node = Node(temp.val)
            # Inserting nodes into hashMap
            hashMap[temp] = node
            temp = temp.next
        
        temp = head

        while temp:
            node = hashMap[temp]
            # Setting next and random pointers to deep copy node
            node.next = hashMap[temp.next] if temp.next else None
            node.random = hashMap[temp.random] if temp.random else None
            temp = temp.next

        return hashMap[head]
