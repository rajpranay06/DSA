'''

Implement the Min Heap data structure. For information about Heap click here.
Min heap is a tree data structure where the root element is the smallest of all the elements in the heap. Also, the children of every node are smaller than or equal to the root node. 
The insertion and removal of elements from the heap take log('N'), where 'N' is the number of nodes in the tree. 

Implement the “minHeap” class. You will be given the following types of queries:-

0 extractMinElement(): Remove the minimum element present in the heap, and return it.
1 deleteElement( i ): Delete the element present at the 'i' th index.
2 insert( key ): Insert the value 'key' in the heap.

For queries of types 0 and 1, at least one element should be in the heap.

Sample Input 1 :
3
2 2
2 1
0
Sample Output 1 :
1
Explanation Of Sample Input 1 :
Insert 2 in the heap, and currently, 2 is the smallest element in the heap.

Insert 1 in the heap and now the smallest element is 1.

Return the smallest element, which is 1.
Sample Input 2 :
5
2 5
2 43
2 15
1 2
0


Time Complexity - O( N * log( N )), Where ‘N’ is the number of queries.
We are iterating over each query which is ‘N’ and for each insert or remove we do heapify operation where we each time go to child or parent, 
which is at its double or half of the current position respectively and max, we will go to the height of the tree which is log ( N ).
Hence the time complexity will be O( N * log( N )).

Space Complexity - O( N ), Where ‘N’ is the number of queries.
We are creating a heap array of size ‘N’.
Hence the space complexity will be O( N ).

'''

class MinHeap:
    def __init__(self, test):
        # Constructor
        self.heap = []

    def heapifyUp(self, pos):
        while pos > 0:
            parent = (pos - 1) // 2
            if self.heap[parent] > self.heap[pos]:
                # Swap if the current element is smaller than its parent
                self.heap[parent], self.heap[pos] = self.heap[pos], self.heap[parent]
                pos = parent
            else:
                break 

    def heapifyDown(self, pos):
        n = len(self.heap)
        while True:
            left = pos*2 + 1
            right = pos*2 + 2
            smallest = pos

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
                
            if smallest != pos:
                # Swap if current element is larger than the smallest child
                self.heap[pos], self.heap[smallest] = self.heap[smallest], self.heap[pos]
                pos = smallest
            
            else:
                break

    def extractMinElement(self):
        # Implement the function to remove the minimum element
        if not self.heap:
            return -1
        # Swap the root with the last element
        res = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        # Heapify Down to maintain heap property
        self.heapifyDown(0)
        return res


    def deleteElement(self, ind):
        # Implement the function to delete an element
        #print(self.heap)
        if ind < 0 or ind >= len(self.heap):
            return
        res = self.heap[ind]
        self.heap[ind] = self.heap[-1]
        self.heap.pop()
        # Heapify up and Down to maintain heap property
        self.heapifyUp(ind)
        self.heapifyDown(ind)


    def insert(self, val):
        # Implement the function to insert 'val' in the heap
        self.heap.append(val)
        
        # Heapify Up to maintain heap property
        self.heapifyUp(len(self.heap) - 1)
        
