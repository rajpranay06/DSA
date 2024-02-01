'''

You have been given a singly Linked List of 'N' nodes with integer data and an integer 'K'.
Your task is to remove the 'K'th node from the end of the given Linked List and return the head of the modified linked list.

To enhance efficiency, we will involve two pointers, a fast pointer and a slow pointer. The fast-moving pointer will initially be exactly N nodes ahead of the slow-moving pointer. 
After which, both of them will move one step at a time. When the fast pointer reaches the last node, i.e., the L-th node, the slow is guaranteed to be at the (L-N)-th node, 
where L is the total length of the linked list.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        # Move the fast pointer N nodes ahead
        for i in range(n):
            fast = fast.next

        # If fast becomes None, the Nth node from the end is the head
        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Delete the Nth node from the end
        slow.next = slow.next.next

        return head

'''

Time Complexity: O(N) since the fast pointer will traverse the entire linked list, where N is the length of the linked list.

Space Complexity: O(1), as we have not used any extra space.

'''
