'''

You have to implement the pop function of Max Priority Queue and implement using a heap.

Functions :
a) push(int x) : 'x' has to be inserted in the priority queue. This has been implemented already
b) pop() : return the maximum element in the priority queue, if priority queue is empty then return '-1'.

Example:
We perform the following operations on an empty priority queue:
When operation push(5) is performed, we insert 1 in the priority queue.
When operation push(2) is performed, we insert 2 in the priority queue. 
When operation pop() is performed, we remove the maximum element from the priority queue and print which is 5.
When operation push(3) is performed, we insert 1 in the priority queue.
When operation pop() is performed, we remove the maximum element from the priority queue and print which is 3.

Sample Input 1 :
8
1 4
1 9
2 
1 5
2 
1 10
1 1
2 

Sample Output 1 :
9
5
10

Explanation For Sample Output 1 :
After processing 1 4
The elements in the priority queue are 4

After processing 1 9
The elements in the priority queue are 4,9

After processing 2
The largest element which is 9 is printed and removed from the queue
The elements in the priority queue are 4

After processing 1 5
The elements in the priority queue are 4,5

After processing 2
The largest element which is 5 is printed and removed from the queue

After processing 1 10
The elements in the priority queue are 4,10

After processing 1 1
The elements in the priority queue are 1,4,10

After processing 2
The largest element which is 10 is printed and removed from the queue
The elements in the priority queue are 1,4

Approach:
The main idea is to remove the element at the peak. As its empty we replace it by the element at the end of the heap(bottommost element). 
Now to maintain the heap property that the element is larger that both its children, we continuously move the element replacing it with the greater child.

Algorithm:

Save the element in the peak of heap
remove the last element and place it at the peak
assign the position of this element to a variable say ‘pos’ which is 0
run a loop indefinitely
if element  at ‘pos’ is larger than both its children
break the loop
else replace it with the larger child and assign ‘pos’ with the position it replaced to.

Time Complexity - O(log(n)) where ‘n’ is the size of the heap
We traverse the heap level wise and as there are log(n) levels in a binary heap the Time Complexity is O(log(n)).

Space Complexity - O(1)
We are not using any extra space in any operation.

'''

from typing import List

def pop(heap: List[int]) -> int:
    # Write your code here.
    if len(heap) == 0:
        return -1
    
    # The answer will be at top of the tree
    res = heap[0]

    # Swap top with bottom before popping
    heap[0] = heap[-1]
    heap.pop()

    n = len(heap)

    # Edge case
    if n == 0:
        return res

    # Shifting the current element down until its correct position.
    pos = 0
    while True:
        # Finding left and right child
        left = 2*pos + 1
        right = 2*pos + 2
        leftVal, rightVal = 0, 0
        if left < n:
            leftVal = heap[left]
        if right < n:
            rightVal = heap[right]
        
        # If parent is > children pos is correctly placed 
        if leftVal <= heap[pos] and rightVal <= heap[pos]:
            break
        
        # Swap pos with the greatest of two childs and set pos to it
        if leftVal >= rightVal:
            heap[pos], heap[left] = heap[left], heap[pos]
            pos = left
        
        else:
            heap[pos], heap[right] = heap[right], heap[pos]
            pos = right
    
    return res

'''
    def push(self, x):
        self.heap.app
        end(x)
        pos = len(self.heap) - 1
        while pos > 0:
            parent = (pos - 1) // 2
            if self.heap[pos] > self.heap[parent]:
                self.heap[pos], self.heap[parent] = self.heap[parent], self.heap[pos]
                pos = parent
            else:
                break
'''
