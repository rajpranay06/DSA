'''

Given a singly linked list of 'N' nodes. Your task is to delete the middle node of this list and return the head of the modified list.

However, if the list has an even number of nodes, we delete the second middle node

Example:
If given linked list is 1->2->3->4 then it should be modified to 1->2->4.

Approach:

We know slow will be at mid if we traverse LL using slow and fast pointers. But we need node before mid to remove mid node. Just skip one slow traverse.
To do this start fast at head.next.next and slow at head.

Time Complexity - O(N/2)
Space Complexity - O(1)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next

        return head
      
            
