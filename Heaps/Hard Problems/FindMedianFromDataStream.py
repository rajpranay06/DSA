'''

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Solution: MaxHeap to store a half of low numbers, MinHeap to store a half of high numbers

The idea is to divide numbers into 2 balanced halves, one half low stores low numbers, the other half high stores high numbers. 
To access the median in O(1), we need a data structure that give us the maximum of low half and the minimum of high half in O(1). That's where maxHeap and minHeap come into play.
We use maxHeap to store a half of low numbers, top of the maxHeap is the highest number among low numbers.
We use minHeap to store a half of high numbers, top of the minHeap is the lowest number among high numbers.
We need to balance the size between maxHeap and minHeap while processing. Hence after adding k elements,
If k = 2 * i then maxHeap.size = minHeap.size = i
If k = 2 * i + 1, let maxHeap store 1 element more than minHeap, then maxHeap.size = minHeap.size + 1.
When adding a new number num into our MedianFinder:
Firstly, add num to the maxHeap, now maxHeap may contain the big element (which should belong to minHeap). So we need to balance, by removing the highest element from maxHeap, and offer it to minHeap.
Now, the minHeap might hold more elements than maxHeap, in that case, we need to balance the size, by removing the lowest element from minHeap and offer it back to maxHeap.

When doing findMedian():
If maxHeap.size > minHeap.size return top of the maxHeap, which is the highest number amongs low numbers.
Else if maxHeap.size == minHeap return the (maxHeap.top() + minHeap.top()) / 2.

Complexity

Time:
Constructor: O(1)
addNum: O(logN)
findMedian: O(1)

Space: O(N)

'''

class MedianFinder:

    def __init__(self):
        # Using two heaps, store first half of stream into maxHeap and next half into minHeap
        # We will have the max element of first half at root of maxHeap and min element of second half at root of minHeap
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # Push num into maxHeap
        heapq.heappush(self.maxHeap, -num)
        # Push the popped num from maxHeap, as we shuld store max elements in second half in minheap
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        # If both heaps length is same, push popped num from minHepa into maxHeap, so we will return root element of maxHeap if length is odd
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


'''

For better beats

'''

from heapq import heappush, heappushpop

class MedianFinder:

    def __init__(self):
        self.small = [] # store -ve value to access the largest
        self.large = []
        self.balanced = True
        self.empty = True

    def addNum(self, num: int) -> None:
        self.empty = False
        
        if self.balanced:
            # push value to small, pop smallest, and push that value to large
            heappush(self.large, -heappushpop(self.small, -num))
            self.balanced = False
            
            # large will have one more than small
        else:
            # push to small
            heappush(self.small, -heappushpop(self.large, num))
            self.balanced = True
        

    def findMedian(self) -> float:
        if self.empty:
            return
        if self.balanced:
            return (self.large[0] - self.small[0])/2
        else:
            return self.large[0]
