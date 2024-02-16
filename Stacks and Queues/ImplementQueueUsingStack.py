'''

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false


Approach 1: Using two Stacks where push operation is O(N)

-> Push all elements from S1 to S2
-> Push x to S1
-> Again push all elements from S2 to S1

Time Complexity: O(N)  
Space Complexity: O(2N)

'''

from queue import LifoQueue
# using LifoQueue which is a stack in python

class MyQueue:

    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()

    def push(self, x: int) -> None:
        while not self.s1.empty():
            self.s2.put(self.s1.get())
        
        self.s1.put(x)

        while not self.s2.empty():
            self.s1.put(self.s2.get())

    def pop(self) -> int:
        if self.s1.empty():
            return 0
        return self.s1.get()

    def peek(self) -> int:
        if self.s1.empty():
            return 0
        return self.s1.queue[-1]

    def empty(self) -> bool:
        return self.s1.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


'''

Approach 2: Using two Stacks where push operation is O(1)

-> Use input and output stacks
-> When push, push to input
-> when pop or top, if ouput is empty push all elements from iput to output and return output.pop() else return output.pop()

Time Complexity: O(1) Amortized - Amortized because few operations take O(N) Time Compexity.

Space Complexity: O(2N)

'''

from queue import LifoQueue
# using LifoQueue which is a stack in python

class MyQueue:

    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()

    def push(self, x: int) -> None:
        self.input.put(x)

    def pop(self) -> int:
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())

        return self.output.get()

    def peek(self) -> int:
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
      
        return self.output.queue[-1]

    def empty(self) -> bool:
        return self.output.empty() and self.input.empty()
    
