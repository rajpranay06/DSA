'''

Step 1: Initialise two pointers that are needed for the reversal. Initialize a current pointer to the head of the linked list. This pointer will traverse the list as we reverse it. 
Initialize a second pointer last to null. This pointer will be used for temporary storage during pointer swapping, as we need a third variable while swapping two data.

Step 2: Traverse through the DLL by looping over all the nodes..

Step 3: While iterating over all nodes in the linked list, we make changes to set the backward pointer of a node to the next changing its previous link. 
Along with this, the forward pointer is adjusted to point to the previous node, reversing the next link. To prevent losing the last node in this process, we use a reference to the last node to retain it.

Update the current node’s back pointer to point to the next node (current->back = current->next). This step reverses the direction of the backward pointer.

Update the current node’s next pointer to point to the previous node (current->next = last). This step reverses the direction of the forward pointer.

Move the current pointer one step forward (current = current->back). This allows us to continue the reversal process.
Step 4: After completing the traversal, the last node ends up at the second node in the reversed doubly linked list. 
To obtain the new head of the reversed list, we simply use the backward pointer of the last node, which points to the new head.

To ensure that we handle the case where the traversal ended at the original list’s end (i.e., the last pointer is not null), 
we update the head pointer to point to the new head of the reversed list, which is stored in the last pointer.

Finally, we return the head pointer, now pointing to the head of the fully reversed doubly linked list.

Time Complexity : O(N) We only have to traverse the doubly linked list once, hence our time complexity is O(N).

Space Complexity : O(1), as the reversal is done in place.

'''


'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''

def reverseDLL(head):
    # Write your code here

    # Check if the list is empty
    # or has only one node
    if not head or not head.next:
        return head

    # Initialize a pointer to
    # the temp node
    temp = None

    # Initialize a pointer
    # to the current node
    curr = head

    while curr:
        
        # Store a reference to
        # the temp node
        temp = curr.prev

        # Swap the previous and next pointers
        curr.prev = curr.next

        # This step reverses the links
        curr.next = temp

        # Move to the next node
        # in the original list
        curr = curr.prev

    # The final node in the original list
    # becomes the new head after reversal
    return temp.prev

