'''

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input:
	head = [1,2,3,4,5] 
	k = 2
Output:
 head = [4,5,1,2,3]
Explanation:
 We have to rotate the list to the right twice.

Steps to the algorithm:-

Calculate the length of the list.
Connect the last node to the first node, converting it to a circular linked list.
Iterate to cut the link of the last node and start a node of k%length of the list rotated list.

'''

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while not head or not head.next or k == 0:
            return head

        temp = head
        n = 1

        while temp.next:
            n += 1
            temp = temp.next
        
        temp.next = head

        k = k%n
        end = n - k

        for i in range(end):
            temp = temp.next
        
        head = temp.next
        temp.next = None

        return head

'''

Time Complexity: O(length of list) + O(length of list – (length of list%k))

Reason: O(length of the list) for calculating the length of the list. O(length of the list – (length of list%k)) for breaking link.

Space Complexity: O(1)

'''
