'''

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

'''

'''

Approach 1: Using Two Queues

When push, put element into q2, put all the elements one by one from q1 into q2. Swap q1 and q2.
When pop, return q1.get()
when top, return q1.queue[0]

Time Complexity: O(N)

Space Complexity: O(N + N)

'''

from queue import Queue 

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.put(x)

        # Put all the elements from Q1 to Q2
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        
        # Swap Q1 and Q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.q1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


'''

Approach 2: Using one queue

Instead of using a second queue, when push, put the element in a queue, run a loop till q.length-1, put the elements from the same queue again in the queue.

If initial queue is 4, 2, 1
Push(3) -> 4, 2, 1, 3 
Now run a lopp till 3, get all the elements and put in the same queue
i = 0 -> 2, 1, 3, 4
i = 1 -> 1, 3, 4, 2
i = 2 -> 3, 4, 2, 1  -> final queue

Time Complexity: O(N)

Space Complexity: O(N)

'''

from queue import Queue 

class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        s = self.q.qsize()
        self.q.put(x)
        
        # Put all the elements from Q1 to Q2
        for i in range(s):
            self.q.put(self.q.get())

    def pop(self) -> int:
        return self.q.get()

    def top(self) -> int:
        return self.q.queue[0]

    def empty(self) -> bool:
        return self.q.empty()

