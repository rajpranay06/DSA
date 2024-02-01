'''

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

To implement the in-order reversal of the second half and its comparison with the first half has to be done in phases. 
The first step is dividing the first and second half of the linked list by recognizing the middle node using the Tortoise and Hare Algorithm.

Time Complexity: O (2* N) The algorithm traverses the linked list twice, dividing it into halves. During the first traversal, it reverses one-half of the list, and during the second traversal, 
it compares the elements of both halves. As each traversal covers N/2 elements, the time complexity is calculated as O(N/2 + N/2 + N/2 + N/2), which simplifies to O(2N), ultimately representing O(N). 

Space Complexity: O(1) The approach uses a constant amount of additional space regardless of the size of the input linked list. 
It doesn’t allocate any new data structures that depend on the input size, resulting in a space complexity of O(1).

'''

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def reverse_linked_list(head):
    # Check if the list is empty
    # or has only one node
    if head is None or head.next is None:
        
        # No change is needed;
        # return the current head
        return head

    # Recursive step: Reverse the remaining part
    # of the list and obtain the new head
    new_head = reverse_linked_list(head.next)

    # Store the next node in 'front' to reverse the link
    front = head.next

    # Update the 'next' pointer of 'front' to 
    # point to the current head, effectively
    # reversing the link direction
    front.next = head

    # Set the 'next' pointer of the current
    # head to 'None' to break the original link
    head.next = None

    # Return the new head obtained
    # from the recursion
    return new_head

def isPalindrome(head):
    # write your code here
    if head is None or head.next is None:
        # It's a palindrome by definition
        return True

    # Initialize two pointers, slow and fast,
    # to find the middle of the linked list
    slow = head
    fast = head

    # Traverse the linked list to find the
    # middle using slow and fast pointers
    while fast.next is not None and fast.next.next is not None:
        # Move slow pointer one step at a time
        slow = slow.next

        # Move fast pointer two steps at a time
        fast = fast.next.next

    # Reverse the second half of the
    # linked list starting from the middle
    new_head = reverse_linked_list(slow.next)

    # Pointer to the first half
    first = head

    # Pointer to the reversed second half
    second = new_head
    while second is not None:
        # Compare data values of
        # nodes from both halves

        # If values do not match,
        # the list is not a palindrome
        if first.data != second.data:
            # Reverse the second half
            # back to its original state
            reverse_linked_list(new_head)
            # Not a palindrome
            return False

        # Move the first pointer
        first = first.next

        # Move the second pointer
        second = second.next

    # Reverse the second half
    # back to its original state
    reverse_linked_list(new_head)

    # The linked list is a palindrome
    return True

