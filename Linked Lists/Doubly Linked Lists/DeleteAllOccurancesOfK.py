'''

A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.

You’re given a doubly-linked list and a key 'k'.

Delete all the nodes having data equal to ‘k’.


Example:
Input: Linked List: 10 <-> 4 <-> 10 <-> 3 <-> 5 <-> 20 <-> 10 and ‘k’ = 10

Output: Modified Linked List: 4 <-> 3 <-> 5 <-> 20

Explanation: All the nodes having ‘data’ = 10 are removed from the linked list.

Time Complexity - O(N)
Space Complexity - O(1)

'''

def deleteAllOccurrences(head: Node, k: int) -> Node:
    # Write your code here

    temp = head

    while temp:
        if temp.data == k:
            if temp == head:
                head = head.next
            
            prevNode = temp.prev
            nextNode = temp.next

            if prevNode:
                prevNode.next = nextNode
            if nextNode:
                nextNode.prev = prevNode
        
        temp = temp.next
    
    return head

