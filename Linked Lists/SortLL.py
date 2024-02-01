'''

Given the head of a linked list, return the list after sorting it in ascending order.

Approach:

Apply merge sort on LL. Find the mid by using slow and fast pointer approach. Divide the LL based on mid, merge the two LLs using dummy node. 

Time Complexity - O(logN + N + N/2) 
Space Complexity - O(1)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def findMid(head):
        slow = head
        fast = head.next  # Starting from head.next to get middle element at left for even length

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeTwoLists(list1, list2):

        # Creating a dummy node to store sorted LL
        dummyNode = ListNode(-1)
        temp = dummyNode

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next
            else:
                temp.next = list2
                temp = list2
                list2 = list2.next
        
        # Extra nodes 
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        return dummyNode.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        # Find the mid node
        mid = Solution.findMid(head)

        # Setting left and right heads of LL
        left = head
        right = mid.next
        mid.next = None

        # Sorting the left and right LLs
        left = self.sortList(left)
        right = self.sortList(right)

        # Merging left and right LLs
        return Solution.mergeTwoLists(left, right)
