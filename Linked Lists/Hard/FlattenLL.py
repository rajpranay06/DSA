'''

Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.

Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
Note: The flattened list will be printed using the bottom pointer instead of the next pointer.

Approach:

Since each list, followed by the bottom pointer, are in sorted order. Our main aim is to make a single list in sorted order of all nodes. So, we can think of a merge algorithm of merge sort.

The process to flatten the given linked list is as follows:-

We will recurse until the head pointer moves null. The main motive is to merge each list from the last.
Merge each list chosen using the merge algorithm. The steps are
Create a dummy node. Point two pointers, i.e, temp and res on dummy node. res is to keep track of dummy node and temp pointer is to move ahead as we build the flattened list.
We iterate through the two chosen. Move head from any of the chosen lists ahead whose current pointed node is smaller. 
Return the new flattened list found.

'''

class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.

def mergeLL(l1, l2):
    temp = Node(-1)
    dummy = temp

    while l1 and l2:
        if l1.data < l2.data:
            temp.child = l1
            l1 = l1.child
        else:
            temp.child = l2
            l2 = l2.child
        temp = temp.child
    
    if l1:
        temp.child = l1
    if l2:
        temp.child = l2

    return dummy.child

def flattenLinkedList(head: Node) -> Node:
    # Write your code here
    if not head or not head.next:
        return head

    head.next = flattenLinkedList(head.next)

    head = mergeLL(head, head.next)

    return head


'''

Time Complexity: O(N), where N is the total number of nodes present

Reason: We are visiting all the nodes present in the given list.

Space Complexity: O(1)

Reason: We are not creating new nodes or using any other data structure.

'''
