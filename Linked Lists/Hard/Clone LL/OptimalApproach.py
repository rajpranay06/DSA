'''

The optimisation will be in removing the extra spaces, i.e, the hashmap used in brute force. This approach can be broken down into three steps. 

Create deep nodes of all nodes. Instead of storing these nodes in a hashmap, we will point it to the next of the original nodes.
Take a pointer, say itr, point it to the head of the list. This will help us to point random pointers as per the original list. 
This can be achieved by itr->next->random = itr->random->next
Use three pointers. One dummy node whose next node points to the first deep node. itr pointer at the head of the original list and fast which is two steps ahead of the itr. 
This will be used to separate the original linked list with the deep nodes list.

Time Complexity: O(N)+O(N)+O(N)

Reason: Each step takes O(N) of time complexity.

Space Complexity: O(1)

Reason: No extra data structure was used for computation.

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

        # Step 1
        while temp:
            # Inserting deep copy nodes next to original node
            node = Node(temp.val)
            node.next = temp.next
            temp.next = node

            temp = temp.next.next
        
        # Step 2
        temp = head
        while temp:
            # Setting random pointer to deep copy nodes
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        # Step 3
        dummy = Node(-1)
        temp = dummy

        itr = head

        while itr:
            # Setting next pointer using dummy node
            front = itr.next.next
            temp.next = itr.next
            
            itr.next = front
            temp = temp.next

            itr = front
        
        return dummy.next
