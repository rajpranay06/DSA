'''

Approach - 1 
Use HeapifyUp concept

Time Compelxity - O(NlogN) 
Space Compexity - O(1)

'''

from typing import List

def minToMaxHeap(n: int, heap: List[int]) -> List[int]:
    # write your code here
    for pos in range(1, n):
        while True:
            parent = (pos - 1) // 2
            if parent >= 0:
                if heap[parent] < heap[pos]:
                    # Swap if the current element is smaller than its parent
                    heap[parent], heap[pos] = heap[pos], heap[parent]
                    pos = parent
                else:
                    break
            else:
                break
    
    return heap


'''

Heapify Approach
The main idea is to build max-heap for the given input array just like in heapsort. It will convert the input array into a max heap. 
We will perform the heapify(Refer Heap Sort Algorithm) process to the given input array to build the heap. 
In a max heap, if arr[ i ] is less than it’s it children node arr[2*i+1] and arr[2*i+2] then replace it with children and call heapfiy on the corresponding child node.
Heapify can only be applied to a node only when its children are heapified. Hence it must be performed in bottom-up order.

Time Complexity - O(n) where ‘n’ is the size of the array.
The time complexity due to the heapify process in the heap sort algorithm is of O(n) time complexity.

Space Complexity - O(1)
We are using constant space to solve this.

'''

from typing import List

def heapify(a, n, pos):
    largest = pos

    left = pos*2 + 1
    right = pos*2 + 2

    # If left child is greater than replace it with node
    if left < n and a[left] > a[largest]:
        largest = left
    # If right child is greater than replace it with node
    if right < n and a[right] > a[largest]:
        largest = right
    
    # If any child has more value call heapify on corresponding sub-tree.
    if largest != pos:

        a[largest], a[pos] = a[pos], a[largest]
        heapify(a, n, largest)


def minToMaxHeap(n: int, a: List[int]) -> List[int]:
    # write your code here
    n = len(a)
    # Calling heapify process in bottom-up manner.
    for pos in range(n//2, -1, -1):
        heapify(a, n, pos)
    
    return a
