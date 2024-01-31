'''

Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.

Optimal Approach 1 - Iterative

The main idea is to flip the order of connections in the linked list, which changes the direction of the arrows.
When this happens, the last element becomes the new first element of the list. This in-place reversal allows us to efficiently transform the original list without using extra space.

Time Complexity: O(N) The code traverses the entire linked list once, where ‘n’ is the number of nodes in the list. This traversal has a linear time complexity, O(N).

Space Complexity: O(1) The code uses only a constant amount of additional space, regardless of the linked list’s length. 
This is achieved by using three pointers (prev, temp and front) to reverse the list without any significant extra memory usage, resulting in constant space complexity, O(1).


'''

def reverseLinkedList(head):
    
    # Initialize 'temp' at the
    # head of the linked list
    temp = head
    
    # Initialize 'prev' to None,
    # representing the previous node 
    prev = None
    
    while temp is not None:
        # Store the next node in 'front'
        # to preserve the reference
        front = temp.next
        # Reverse the direction of the current
        # node's 'next' pointer to point to 'prev'
        temp.next = prev
        # Move 'prev' to the current 
        # node, for the next iteration
        prev = temp
        # Move 'temp' to 'front' node
        # advancing traversal
        temp = front

    # Return the new head
    # of the reversed linked list
    return prev


'''

Optimal Approach 2 - Recursive

In this case, tackling the larger problem involves reversing a linked list with N = 4 nodes. Recursion allows us to break this task down into progressively smaller subproblems, 
starting with the case of 3 nodes, then the last 2 nodes, and ultimately reaching the base case where only 1 node remains. 
In the base case, reversing the linked list is straightforward, as a list with just one node is already in its reversed form, and we can simply return it as is.

Algorithm:

Base Case:
Check if the linked list is empty or contains only one node. Return the head as it’s already reversed in these cases.

Recursive Function:
The core of the algorithm lies in implementing a recursive function responsible for reversing the linked list. This function operates based on the following principle:

If the base case conditions are not met, the function invokes itself recursively. 
This recursion continues until it reaches the base case, gradually reversing the linked list starting from the second node (node after it) onward.

Return

Following the recursion, the function returns the new head of the reversed linked list. This head marks the last node of the original list before reversal, now the first node in the reversed sequence.

Time Complexity: O(N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and update the linked list. Both traversals take O(N) time.

Space Complexity : O(1) No additional space is used explicitly for data structures or allocations during the linked list reversal process. 
However, it’s important to note that there is an implicit use of stack space due to recursion. 
This recursive stack space stores function calls and associated variables during the recursive traversal and reversal of the linked list. 
Despite this, no extra memory beyond the program’s existing execution space is allocated, hence maintaining a space complexity of O(1).

'''

def reverse_linked_list(head):
    # Base case:
    # If the linked list is empty or has only one node,
    # return the head as it is already reversed.
    if head is None or head.next is None:
        return head
    
    # Recursive step:
    # Reverse the linked list starting from the second node (head.next).
    new_head = reverse_linked_list(head.next)
    
    # Save a reference to the node following
    # the current 'head' node.
    front = head.next
    
    # Make the 'front' node point to the current
    # 'head' node in the reversed order.
    front.next = head
    
    # Break the link from the current 'head' node
    # to the 'front' node to avoid cycles.
    head.next = None
    
    # Return the 'new_head,' which is the new
    # head of the reversed linked list.
    return new_head
