'''

You're given a positive integer represented in the form of a singly linked-list of digits. The length of the number is 'n'.
Add 1 to the number, i.e., increment the given number by one.
The digits are stored such that the most significant digit is at the head of the linked list and the least significant digit is at the tail of the linked list.

Example:
Input: Initial Linked List: 1 -> 5 -> 2

Output: Modified Linked List: 1 -> 5 -> 3

Explanation: Initially the number is 152. After incrementing it by 1, the number becomes 153.

Approach:

We can use recursion to add carry from reverse. Create a recursive function passing head, if head reaches null return 1 as carry. Add the carry to the next nodes and return remaining carry. 

If carry == 1 after recursion add a new node to head. 

Time Complexity - O(N) 
Space Complexity - O(N) -> recursive stack space

'''

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.

def findCarry(temp):

    # Edge case, adding carry
    if not temp:
        return 1

    # Going to next node
    carry = findCarry(temp.next)

    # Adding the carry to node data
    temp.data += carry

    # setting temp.data acc to carry
    if temp.data < 10:
        return 0
    
    temp.data = 0

    return 1

    '''
    Or can also use the following code to return carry

    val = temp.data//10
    temp.data %= 10

    return val

    '''

def addOne(head: Node) -> Node:
    # write your code here

    # Recursive function to add carry
    carry = findCarry(head)

    # For edge cases like 999 Extra node to be added
    if carry == 1:
        newNode = Node(1)
        newNode.next = head
        return newNode
    
    return head
    
    
