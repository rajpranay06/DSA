'''

This gap method is based on a sorting technique called shell sort. The intuition of this method is simple. 

Intuition:
Similar to optimal approach 1, in this approach, we will use two pointers i.e. left and right, and swap the elements if the element at the left pointer is greater than the element at the right pointer. 

But the placing of the pointers will be based on the gap value calculated. The formula to calculate the initial gap is the following:

Initial gap = ceil((size of arr1[] + size of arr2[]) / 2)

Assume the two arrays as a single continuous array and initially, we will place the left pointer at the first index and the right pointer at the (left+gap) index of that continuous array.

Now, we will compare the elements at the left and right pointers and move them by 1 place each time after comparison. 
While comparing we will swap the elements if the element at the left pointer > the element at the right pointer. After some steps, the right pointer will reach the end and the iteration will be stopped.

After each iteration, we will decrease the gap and will follow the same procedure until the iteration for gap = 1 gets completed. Now, after each iteration, the gap will be the following:

gap = ceil( previous gap / 2)

The whole process will be applied to the imaginary continuous array constructed using arr1[] and arr2[].

'''

class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:

        # len of the imaginary single array:
        l = m+n

        # Initial gap:
        gap = l//2 + l%2
        while gap > 0:

            # Place 2 pointers:
            left = 0
            right = gap
            while right < l:

                # case 1: left in arr1[]
                # and right in arr2[]:
                if left < m and right >= m:
                    if arr1[left] > arr2[right-m]:
                        arr1[left], arr2[right-m] = arr2[right-m], arr1[left]

                # case 2: both pointers in arr2[]:
                elif left >= m:
                    if arr2[left-m] > arr2[right-m]:
                        arr2[left-m], arr2[right-m] = arr2[right-m], arr2[left-m]

                # case 3: both pointers in arr1[]:
                else:
                    if arr1[left] > arr1[right]:
                        arr1[left], arr1[right] = arr1[right], arr1[left]
                left += 1
                right += 1

            # break if iteration gap=1 is completed:
            if gap == 1:
                break

            # Otherwise, calculate new gap:
            gap = gap//2 + gap%2

        # Adding arr2 to arr1 acc to problem
        for i in range(m,m+n):
            arr1[i] = arr2[i-m]
        
'''

Time Complexity: O((n+m)*log(n+m)), where n and m are the sizes of the given arrays.
Reason: The gap is ranging from n+m to 1 and every time the gap gets divided by 2. So, the time complexity of the outer loop will be O(log(n+m)). 
Now, for each value of the gap, the inner loop can at most run for (n+m) times. So, the time complexity of the inner loop will be O(n+m). So, the overall time complexity will be O((n+m)*log(n+m)).

Space Complexity: O(1) as we are not using any extra space.

'''

        
