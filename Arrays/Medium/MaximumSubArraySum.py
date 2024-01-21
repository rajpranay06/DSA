'''
Intuition:

The intuition of the algorithm is not to consider the subarray as a part of the answer if its sum is less than 0. 
A subarray with a sum less than 0 will always reduce our answer and so this type of subarray cannot be a part of the subarray with maximum sum.

Here, we will iterate the given array with a single loop and while iterating we will add the elements in a sum variable. 
Now, if at any point the sum becomes less than 0, we will set the sum as 0 as we are not going to consider any subarray with a negative sum. 
Among all the sums calculated, we will consider the maximum one.

'''

class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        max_sum = float("-inf")
        s = 0
        start, ansStart, ansEnd = 0,-1,-1
        for i in range(len(a)):

            if s == 0:
                start = i

            s += a[i]
            if s > max_sum:
                max_sum = s
                ansStart = start
                ansEnd = i
              
            # If sum < 0: discard the sum calculated
            if s < 0:
                s = 0

        print(ansStart,ansEnd)
        return max_sum

'''
Follow up question

Intuition
There might be more than one subarray with the maximum sum. We need to print any of them.

Intuition: Our approach is to store the starting index and the ending index of the subarray. Thus we can easily get the subarray afterward without actually storing the subarray elements.

If we carefully observe our algorithm, we can notice that the subarray always starts at the particular index where the sum variable is equal to 0, and at the ending index, the sum always crosses the previous maximum sum(i.e. maxi).

So, we will keep a track of the starting index inside the loop using a start variable.
We will take two variables ansStart and ansEnd initialized with -1. And when the sum crosses the maximum sum, we will set ansStart to the start variable and ansEnd to the current index i.e. i.

'''

import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    sum = 0

    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(n):

        if sum == 0:
            start = i  # starting index

        sum += arr[i]

        if sum > maxi:
            maxi = sum

            ansStart = start
            ansEnd = i

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0

    # printing the subarray:
    print("The subarray is: [", end="")
    for i in range(ansStart, ansEnd + 1):
        print(arr[i], end=" ")
    print("]")

    # To consider the sum of the empty subarray
    # uncomment the following check:

    # if maxi < 0:
    #     maxi = 0

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)


'''
Time Complexity: O(N), where N = size of the array.
Reason: We are using a single loop running N times.

Space Complexity: O(1) as we are not using any extra space.

'''
