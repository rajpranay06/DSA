'''

A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.

You are given a sorted doubly linked list of size 'n', consisting of distinct positive integers, and a number 'k'.

Find out all the pairs in the doubly linked list with sum equal to 'k'.


Example :
Input: Linked List: 1 <-> 2 <-> 3 <-> 4 <-> 9 and 'k' = 5

Output: (1, 4) and (2, 3)

Explanation: There are 2 pairs in the linked list having sum 'k' = 5.

2-Pointer approach

Time Complexity - O(N)
Space Complecity - O(N)

'''

def findPairs(head: Node, k: int) -> [[int]]:

    # Write your code here.
    # Return boolean true or false.
    low = head

    high = head

    while high.next:
        high = high.next
    
    res = []
    while low.data < high.data:
        s = low.data + high.data
        if s == k:
            res.append([low.data, high.data])
            low = low.next
            high = high.prev
        elif s < k:
            low = low.next
        else:
            high = high.prev

    return res
