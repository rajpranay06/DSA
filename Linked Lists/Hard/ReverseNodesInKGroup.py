'''

Given the head of a singly linked list of `n` nodes and an integer `k`, where k is less than or equal to `n`. 
Your task is to reverse the order of each group of `k` consecutive nodes, if `n` is not divisible by `k`, then the last group of remaining nodes should remain unchanged.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

The approach simplifies reversing linked list nodes by breaking the list into segments of K nodes and reversing each segment individually. 
Starting from the head, the algorithm traverses the list to identify segments of K nodes. Upon finding a segment, it reverses it, returning the modified list. 
If a segment has less than K nodes left (ie. remaining nodes at the end), they are left unaltered. 

To implement this (complex) algorithm we can break down the process into three parts:

`reverseLinkedList`: This function takes the head of a segment as input and reverses the linked list formed by that segment. 
It operates by utilizing the classic iterative 3-pointer method to reverse the direction of pointers within the segment. Read about this algorithm in detail here Reverse Linked List.

`getKthNode`: The purpose of this function is to identify the end of a segment of K nodes in the linked list. 
Given a starting node, it traverses K nodes in the list and returns the Kth node, allowing the segmentation of the list into smaller parts for reversal.

`kReverse`: The main function orchestrates the reversal process. It iterates through the linked list and identifies segments of K nodes using getKthNode. 
For each identified segment, it utilizes reverseLinkedList to reverse the nodes within that segment. This iterative approach efficiently reverses the linked list nodes in groups of K.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        new_node = Solution.reverseList(head.next)

        front = head.next
        front.next = head
        head.next = None

        return new_node

    def findKthNode(temp, k):
        # Decrement K as we already
        # start from the 1st node
        k -= 1

        # Decrement K until it reaches
        # the desired position
        while temp and k > 0:
            k -= 1
            temp = temp.next
        
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        temp = head

        # Initialize a pointer to track the
        # last node of the previous group
        prevNode = None

        while temp:
            # Get the Kth node of the current group
            kthNode = Solution.findKthNode(temp,k)

            # If the Kth node is NULL
            # (not a complete group)
            if not kthNode:
                # If there was a previous group,
                # link the last node to the current node
                if prevNode:
                    prevNode.next = temp
                break
            
            # Store the next node
            # after the Kth node
            nextNode = kthNode.next

            # Disconnect the Kth node
            # to prepare for reversal
            kthNode.next = None

            Solution.reverseList(temp)
            
            # Adjust the head if the reversal
            # starts from the head
            if temp == head:
                head = kthNode
            else:
                # Link the last node of the previous
                # group to the reversed group
                prevNode.next = kthNode

            # Update the pointer to the
            # last node of the previous group
            prevNode = temp

            # Move to the next group
            temp = nextNode

        return head

'''

Time Complexity: O(2N) The time complexity consists of actions of reversing segments of K and finding the Kth node which operates in linear time. Thus, O(N) + O(N) = O(2N), which simplifies to O(N).

Space Complexity: O(1) The space complexity is O(1) as the algorithm operates in place without any additional space requirements.

'''
