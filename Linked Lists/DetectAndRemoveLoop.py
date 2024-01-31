'''

Given a singly linked list, you have to detect the loop and remove the loop from the linked list, if present. You have to make changes in the given linked list itself and return the updated linked list.

Use floyd detection cycle to detect the cycle in the linked list
Move the slow pointer to the head node.
Now move the fast and the slow pointer with the same speed.
Wherever they meet, that is the starting node of the cycle.
Change the next pointer of the previous node to point to NULL thus breaking the cycle present in the linked list.

Time Complexity: O(N)

Space Complexity: O(1)

'''

from typing import *

# Following is the structure of  Node
# Do not update or change the structure 

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

def removeLoop(head :Node) -> Node :

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    
    if slow != fast:
        return head
    
    # Loop Removal Algorithm
    slow = head

    # checking for intersection of two pointers
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # loop termination
    fast.next = None

    return head
