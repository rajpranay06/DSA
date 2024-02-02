'''

Problem Statement: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Approach:

We will reduce the search length. This can be done by searching the length of the shorter linked list. How? Let’s see the process.

Find the length of both lists.
Find the positive difference between these lengths.
Move the dummy pointer of the larger list by the difference achieved. This makes our search length reduced to a smaller list length.
Move both pointers, each pointing two lists, ahead simultaneously if both do not collide.

Time Complexity:

O(2max(length of list1,length of list2))+O(abs(length of list1-length of list2))+O(min(length of list1,length of list2))

Reason: Finding the length of both lists takes max(length of list1, length of list2) because it is found simultaneously for both of them. Moving the head pointer ahead by a difference of them. The next one is for searching.

Space Complexity: O(1)

'''

def getDifference(head1, head2):
    len1 = 0
    len2 = 0
    while head1 != None or head2 != None:
        if head1 != None:
            len1 += 1
            head1 = head1.next
        if head2 != None:
            len2 += 1
            head2 = head2.next
    # if difference is neg-> length of list2 > length of list1 else vice-versa
    return len1 - len2




# utility function to check presence of intersection
def intersectionPresent(head1, head2):
    diff = getDifference(head1, head2)
    if diff < 0:
        while diff != 0:
            head2 = head2.next
            diff += 1
    else:
        while diff != 0:
            head1 = head1.next
            diff -= 1
    while head1 != None:
        if head1 == head2:
            return head1
        head2 = head2.next
        head1 = head1.next
    return head1


'''

Solution 2: Optimised 

Approach:

The difference of length method requires various steps to work on it. Using the same concept of difference of length, a different approach can be implemented. The process is as follows:-

Take two dummy nodes for each list. Point each to the head of the lists.
Iterate over them. If anyone becomes null, point them to the head of the opposite lists and continue iterating until they collide.

Time Complexity: O(2*max(length of list1,length of list2))

Reason: Uses the same concept of the difference of lengths of two lists.

Space Complexity: O(1)

'''


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1 = headA
        d2 = headB

        while d1 != d2:
            d1 = headB if d1 == None else d1.next
            d2 = headA if d2 == None else d2.next
        
        return d1

  
