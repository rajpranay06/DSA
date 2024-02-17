'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Approach 1:
Using pairs to store the value and minimum element till now. 
The first element in the pair will store the value and the second element will store the minimum element till now.

Time Complexity: O(1)
Space Complexity: O(2N)

'''

class MinStack:

    def __init__(self):
        self.st = []
        self.minVal = None

    def push(self, val: int) -> None:
        if not self.st:
            self.minVal = val
        else:
            self.minVal = min(val, self.st[-1][1])
        self.st.append([val, self.minVal])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


'''

Approach 2:

Let’s take a variable that stores the minimum number. So whenever a push operation comes in just take that number put it in the stack and update the variable to the number.

Push operation:
Now if there is a push operation just check whether that number is less than the min number. 
If it is smaller than min we will push a modified value which is a push(2 * Val – min) into the stack and will update min to the value of the original number. 
If it’s not then we will just push it as it is.

getMin() operation:
We will just return the value of min.

Top operation:
While returning the top value we know that it is a modified value. We will check if the top value is lesser than min, If it is then we will return the min as the top value.

Pop operation:
While making pop we will check if the top value is lesser than min, If it is then we must update our min to its previous value. 
In order to do that min = (2 * min) – (modified value) and we will pop the element.


Time Complexity: O(1)
Space Complexity: O(N)

'''

class MinStack:

    def __init__(self):
        self.st = []
        self.minVal = None

    def push(self, val: int) -> None:
        if not self.st:
            self.minVal = val
            self.st.append(val)
        else:
            if self.minVal > val:
                modifiedVal = 2*val - self.minVal
                self.minVal = val
                self.st.append(modifiedVal)
            else:
                self.st.append(val)

    def pop(self) -> None:
        if self.st[-1] < self.minVal:
            modifiedMin = 2*self.minVal - self.st[-1]
            self.minVal = modifiedMin
        self.st.pop()

    def top(self) -> int:
        if self.st[-1] < self.minVal:
            return self.minVal
        return self.st[-1]

    def getMin(self) -> int:
        return self.minVal

