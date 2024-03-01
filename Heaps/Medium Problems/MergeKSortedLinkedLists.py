'''

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

Approach: Similar to Merge K sorted arrays, just modify to Linked lists

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode(-1)
        temp = head
        
        # Add all the nodes into minheap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        while heap:
            # Pop the min heap, as first element will be min
            curr = heapq.heappop(heap)

            # Add it to head LL
            node = curr[2]
            temp.next = node
            temp = temp.next
            
            # Go to next node of the popped LL, add it to the heap
            if node.next:
                i += 1
                heapq.heappush(heap, (node.next.val, i, node.next)) 
        
        return head.next
