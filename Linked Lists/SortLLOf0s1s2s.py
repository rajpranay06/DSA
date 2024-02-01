'''

Given a linked list of 'N' nodes, where each node has an integer value that can be 0, 1, or 2. You need to sort the linked list in non-decreasing order and the return the head of the sorted list.

Example:
Given linked list is 1 -> 0 -> 2 -> 1 -> 2. 
The sorted list for the given linked list will be 0 -> 1 -> 1 -> 2 -> 2.

Approach:

	We can change the links of 0, 1 and 2 nodes using dummy nodes. 

Time Complexity - O(N)
Space Complexity - O(1)

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def sortList(head):
    # Write your code here
    list0 = Node(-1)
    list1 = Node(-1)
    list2 = Node(-1)

    temp0 = list0
    temp1 = list1
    temp2 = list2

    while head:
        if head.data == 0:
            temp0.next = head
            temp0 = head
        elif head.data == 1:
            temp1.next = head
            temp1 = head
        else:
            temp2.next = head
            temp2 = head
        head = head.next
    if list1.next:
        temp0.next = list1.next
    else:
        temp0.next = list2.next
    temp1.next = list2.next
    temp2.next = None
    
    return list0.next
    
