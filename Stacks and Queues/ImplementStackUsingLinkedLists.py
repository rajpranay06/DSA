'''

Problem statement
You must implement the Stack data structure using a Singly Linked List.
Create a class named 'Stack' which supports the following operations(all in O(1) time):

getSize: Returns an integer. Gets the current size of the stack
isEmpty: Returns a boolean. Gets whether the stack is empty
push: Returns nothing. Accepts an integer. Puts that integer at the top of the stack
pop: Returns nothing. Removes the top element of the stack. It does nothing if the stack is empty.
getTop: Returns an integer. Gets the top element of the stack. Returns -1 if the stack is empty.

'''

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    # Write your code here
    def __init__(self):
    # Write your code here
        this.head = Node(-1)
        this.temp = this.head
        this.prev = this.head
        this.c = 0  # length
        pass
        
    def getSize(self):
        return this.c

    def isEmpty(self):
        return this.c == 0

    def push(self, data):
        # Write your code here
        this.prev = this.temp
        this.temp.next = Node(data)
        this.temp = temp.next
        c += 1
        
    def pop(self):
        # Write your code here
        if prev:
            this.temp = this.prev
            this.temp.next = None
            c -= 1
             
    def getTop(self):
        # Write your code here
        return temp.data
